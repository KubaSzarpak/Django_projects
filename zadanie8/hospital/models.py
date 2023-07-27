from django.db import models


# Create your models here.

class Medicament(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    due_date = models.DateField()


class PrescriptionMedicament(models.Model):
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='prescriptions')
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='medicaments')
    dose = models.PositiveIntegerField()
    details = models.CharField(max_length=255)
