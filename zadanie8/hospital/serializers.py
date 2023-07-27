from rest_framework import serializers
from .models import Doctor, Medicament, Patient, Prescription, PrescriptionMedicament


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'email']


class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = ['id', 'name', 'description', 'type']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'birthdate']


class SimplePrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionMedicament
        fields = ['patient', 'doctor', 'date']


class PrescriptionMedicamentSerializer(serializers.ModelSerializer):
    medicament = MedicamentSerializer(many=True)
    prescription = SimplePrescriptionSerializer()

    class Meta:
        model = PrescriptionMedicament
        fields = ['medicament', 'prescription', 'dose', 'details']


class SimplePrescriptionMedicamentSerializer(serializers.ModelSerializer):
    medicament = MedicamentSerializer()

    class Meta:
        model = PrescriptionMedicament
        fields = ['medicament', 'dose', 'details']


class PrescriptionSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()
    medicaments = SimplePrescriptionMedicamentSerializer(many=True)

    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'date', 'due_date', 'medicaments']



