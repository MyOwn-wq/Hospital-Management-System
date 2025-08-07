from django.db import models
from django.core.validators import RegexValidator
from api.authentication.models import User


class Specialization(models.Model):
    """
    Medical specializations
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'specializations'
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'
    
    def __str__(self):
        return self.name


class Doctor(models.Model):
    """
    Doctor model with professional information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    doctor_id = models.CharField(max_length=20, unique=True, blank=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='doctors')
    license_number = models.CharField(max_length=50, unique=True)
    experience_years = models.PositiveIntegerField(default=0)
    education = models.TextField()
    certifications = models.TextField(blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'doctors'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
    
    def __str__(self):
        return f"Dr. {self.user.get_full_name()} ({self.specialization.name})"
    
    def save(self, *args, **kwargs):
        if not self.doctor_id:
            # Generate doctor ID
            last_doctor = Doctor.objects.order_by('-id').first()
            if last_doctor:
                last_number = int(last_doctor.doctor_id[3:]) if last_doctor.doctor_id else 0
                self.doctor_id = f"DOC{str(last_number + 1).zfill(6)}"
            else:
                self.doctor_id = "DOC000001"
        super().save(*args, **kwargs)


class DoctorAvailability(models.Model):
    """
    Doctor availability schedule
    """
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'doctor_availabilities'
        verbose_name = 'Doctor Availability'
        verbose_name_plural = 'Doctor Availabilities'
        unique_together = ['doctor', 'day']
    
    def __str__(self):
        return f"{self.doctor.user.get_full_name()} - {self.get_day_display()} ({self.start_time} - {self.end_time})"


class DoctorLeave(models.Model):
    """
    Doctor leave management
    """
    LEAVE_TYPE_CHOICES = [
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('annual', 'Annual Leave'),
        ('emergency', 'Emergency Leave'),
        ('other', 'Other'),
    ]
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='leaves')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leaves')
    approved_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'doctor_leaves'
        verbose_name = 'Doctor Leave'
        verbose_name_plural = 'Doctor Leaves'
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.doctor.user.get_full_name()} - {self.get_leave_type_display()} ({self.start_date} to {self.end_date})"
