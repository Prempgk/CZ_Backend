from rest_framework import serializers
from .models import *

class staff_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = staff_profile
        fields = (
            'id', 'staff_id', 'First_name', 'Middle_name', 'Last_name', 'Dob','Gender', 'Scar', 'Mole', 'Blood_group', 'Religion', 'Nationality', 'Caste', 'Community',
            'Aadhaar_no', 'Mobile_no', 'Alt_mob_no', 'Mail_id', 'Martial_status', 'Spouse_name', 'Spouse_occupation', 'Mother_name', 'Mother_occupation',
            'Father_name', 'Father_occupation', 'Guardian_name', 'Guardian_occupation', 'Medical_History', 'Temporary_Address', 'Permanent_Address',
            'Languages_known', 'Mother_tongue', 'Skills', 'Hobbies', 'Awards', 'Recognitions'
        )

class staff_qual_serializer(serializers.ModelSerializer):
    class Meta:
        model = staff_qualification
        fields = (
            'id', 'Degree_name', 'Specialization', 'Year_of_passing', 'Percentage','staff_id'
        )

class staff_exp_serializer(serializers.ModelSerializer):
    class Meta:
        model = staff_experience
        fields = (
              'id', 'Designation', 'Name_of_institution', 'Experience_from', 'Experience_to','staff_id'
        )

class staff_curr_address_serializer(serializers.ModelSerializer):
    class Meta:
        model = staff_current_address
        fields = (
            'id', 'staff_id', 'Door_no', 'Street', 'Village', 'District', 'State', 'Pincode'
        )

class staff_permanent_address_serializer(serializers.ModelSerializer):
    class Meta:
        model = staff_permanent_address
        fields = (
            'id', 'staff_id', 'Door_no', 'Street', 'Village', 'District', 'State', 'Pincode'
        )

class staff_joining_serializer(serializers.ModelSerializer):
    class Meta:
        model = staff_joining_details
        fields = (
            'id', 'staff_id', 'Designation', 'Date_of_joining', 'Nature_of_appointment', 'staff_status'
        )

class staff_bank_serializer(serializers.ModelSerializer):
    class Meta:
        model = staff_bank_details
        fields = (
            'id', 'staff_id', 'Bank_name', 'Branch_name', 'Ifsc_code', 'Account_no', 'Pan_no'
        )