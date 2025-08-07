from django.db import models
from api.authentication.models import User


class Prescription(models.Model):
    """
    Medical prescriptions
    """
    PRESCRIPTION_TYPE_CHOICES = [
        ('medication', 'Medication'),
        ('test', 'Laboratory Test'),
        ('procedure', 'Medical Procedure'),
        ('diet', 'Diet Plan'),
        ('exercise', 'Exercise Plan'),
        ('other', 'Other'),
    ]
    
    prescription_id = models.CharField(max_length=20, unique=True, blank=True)
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='prescriptions')
    appointment = models.ForeignKey('appointments.Appointment', on_delete=models.CASCADE, related_name='prescriptions', blank=True, null=True)
    prescription_type = models.CharField(max_length=20, choices=PRESCRIPTION_TYPE_CHOICES, default='medication')
    diagnosis = models.TextField()
    prescription_text = models.TextField()
    instructions = models.TextField(blank=True, null=True)
    prescribed_date = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'prescriptions'
        verbose_name = 'Prescription'
        verbose_name_plural = 'Prescriptions'
        ordering = ['-prescribed_date']
    
    def __str__(self):
        return f"Prescription {self.prescription_id} - {self.patient.user.get_full_name()}"
    
    def save(self, *args, **kwargs):
        if not self.prescription_id:
            # Generate prescription ID
            last_prescription = Prescription.objects.order_by('-id').first()
            if last_prescription:
                last_number = int(last_prescription.prescription_id[3:]) if last_prescription.prescription_id else 0
                self.prescription_id = f"PRS{str(last_number + 1).zfill(6)}"
            else:
                self.prescription_id = "PRS000001"
        super().save(*args, **kwargs)


class Medication(models.Model):
    """
    Medications in prescriptions
    """
    MEDICATION_TYPE_CHOICES = [
        ('tablet', 'Tablet'),
        ('capsule', 'Capsule'),
        ('syrup', 'Syrup'),
        ('injection', 'Injection'),
        ('cream', 'Cream'),
        ('drops', 'Drops'),
        ('other', 'Other'),
    ]
    
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=200)
    medication_type = models.CharField(max_length=20, choices=MEDICATION_TYPE_CHOICES)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'medications'
        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'
    
    def __str__(self):
        return f"{self.name} - {self.dosage}"


class MedicalDocument(models.Model):
    """
    Medical documents and files
    """
    DOCUMENT_TYPE_CHOICES = [
        ('prescription', 'Prescription'),
        ('lab_report', 'Laboratory Report'),
        ('xray', 'X-Ray'),
        ('mri', 'MRI'),
        ('ct_scan', 'CT Scan'),
        ('ultrasound', 'Ultrasound'),
        ('discharge_summary', 'Discharge Summary'),
        ('medical_certificate', 'Medical Certificate'),
        ('insurance_form', 'Insurance Form'),
        ('other', 'Other'),
    ]
    
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='medical_documents')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='medical_documents', blank=True, null=True)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='medical_documents/')
    file_size = models.PositiveIntegerField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_documents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'medical_documents'
        verbose_name = 'Medical Document'
        verbose_name_plural = 'Medical Documents'
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.title} - {self.patient.user.get_full_name()}"
    
    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)


class MedicalNote(models.Model):
    """
    Medical notes and observations
    """
    NOTE_TYPE_CHOICES = [
        ('progress', 'Progress Note'),
        ('assessment', 'Assessment'),
        ('plan', 'Treatment Plan'),
        ('observation', 'Observation'),
        ('instruction', 'Instruction'),
        ('other', 'Other'),
    ]
    
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='medical_notes')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='medical_notes')
    note_type = models.CharField(max_length=20, choices=NOTE_TYPE_CHOICES, default='progress')
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'medical_notes'
        verbose_name = 'Medical Note'
        verbose_name_plural = 'Medical Notes'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.patient.user.get_full_name()}"
