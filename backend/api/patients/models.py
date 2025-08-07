from django.db import models
from django.core.validators import RegexValidator
from api.authentication.models import User


class Patient(models.Model):
    """
    Patient model with medical information
    """
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    patient_id = models.CharField(max_length=20, unique=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    emergency_contact = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        blank=True,
        null=True
    )
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)
    current_medications = models.TextField(blank=True, null=True)
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    insurance_number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'patients'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.patient_id})"
    
    def save(self, *args, **kwargs):
        if not self.patient_id:
            # Generate patient ID
            last_patient = Patient.objects.order_by('-id').first()
            if last_patient:
                last_number = int(last_patient.patient_id[3:]) if last_patient.patient_id else 0
                self.patient_id = f"PAT{str(last_number + 1).zfill(6)}"
            else:
                self.patient_id = "PAT000001"
        super().save(*args, **kwargs)


class MedicalHistory(models.Model):
    """
    Medical history for patients
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_histories')
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescription = models.TextField(blank=True, null=True)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='medical_histories')
    visit_date = models.DateTimeField()
    next_visit = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'medical_histories'
        verbose_name = 'Medical History'
        verbose_name_plural = 'Medical Histories'
        ordering = ['-visit_date']
    
    def __str__(self):
        return f"{self.patient.user.get_full_name()} - {self.diagnosis[:50]}"


class LabReport(models.Model):
    """
    Laboratory reports for patients
    """
    REPORT_TYPE_CHOICES = [
        ('blood', 'Blood Test'),
        ('urine', 'Urine Test'),
        ('xray', 'X-Ray'),
        ('mri', 'MRI'),
        ('ct', 'CT Scan'),
        ('ultrasound', 'Ultrasound'),
        ('other', 'Other'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='lab_reports')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    test_name = models.CharField(max_length=200)
    test_date = models.DateTimeField()
    result_date = models.DateTimeField(blank=True, null=True)
    results = models.TextField()
    normal_range = models.TextField(blank=True, null=True)
    is_normal = models.BooleanField(default=True)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='lab_reports')
    report_file = models.FileField(upload_to='lab_reports/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'lab_reports'
        verbose_name = 'Lab Report'
        verbose_name_plural = 'Lab Reports'
        ordering = ['-test_date']
    
    def __str__(self):
        return f"{self.patient.user.get_full_name()} - {self.test_name}"
