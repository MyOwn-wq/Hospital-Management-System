from django.db import models
from api.authentication.models import User


class Appointment(models.Model):
    """
    Appointment model for patient-doctor scheduling
    """
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ]
    
    APPOINTMENT_TYPE_CHOICES = [
        ('consultation', 'Consultation'),
        ('follow_up', 'Follow Up'),
        ('emergency', 'Emergency'),
        ('routine_checkup', 'Routine Checkup'),
        ('surgery', 'Surgery'),
        ('other', 'Other'),
    ]
    
    appointment_id = models.CharField(max_length=20, unique=True, blank=True)
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='appointments')
    appointment_type = models.CharField(max_length=20, choices=APPOINTMENT_TYPE_CHOICES, default='consultation')
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()
    duration = models.PositiveIntegerField(default=30, help_text='Duration in minutes')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    symptoms = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_appointments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'appointments'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        ordering = ['-scheduled_date', '-scheduled_time']
    
    def __str__(self):
        return f"{self.patient.user.get_full_name()} - Dr. {self.doctor.user.get_full_name()} ({self.scheduled_date})"
    
    def save(self, *args, **kwargs):
        if not self.appointment_id:
            # Generate appointment ID
            last_appointment = Appointment.objects.order_by('-id').first()
            if last_appointment:
                last_number = int(last_appointment.appointment_id[3:]) if last_appointment.appointment_id else 0
                self.appointment_id = f"APT{str(last_number + 1).zfill(6)}"
            else:
                self.appointment_id = "APT000001"
        super().save(*args, **kwargs)


class AppointmentReminder(models.Model):
    """
    Appointment reminders for notifications
    """
    REMINDER_TYPE_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('push', 'Push Notification'),
    ]
    
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='reminders')
    reminder_type = models.CharField(max_length=20, choices=REMINDER_TYPE_CHOICES)
    reminder_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'appointment_reminders'
        verbose_name = 'Appointment Reminder'
        verbose_name_plural = 'Appointment Reminders'
        ordering = ['-reminder_time']
    
    def __str__(self):
        return f"Reminder for {self.appointment} - {self.get_reminder_type_display()}"


class AppointmentNote(models.Model):
    """
    Notes for appointments
    """
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointment_notes')
    note = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment_notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'appointment_notes'
        verbose_name = 'Appointment Note'
        verbose_name_plural = 'Appointment Notes'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Note for {self.appointment} by {self.created_by.get_full_name()}"
