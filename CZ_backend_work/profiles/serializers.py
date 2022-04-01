from rest_framework import serializers
from .models import *
from .models import staff_profile
class staff_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = staff_profile
        fields = (
            'id', 'staff_id', 'First_name', 'Middle_name', 'Last_name', 'Dob','Gender', 'Scar', 'Mole', 'Blood_group', 'Religion', 'Nationality', 'Caste', 'Community',
            'Aadhaar_no', 'Mobile_no', 'Alt_mob_no', 'Mail_id', 'Martial_status', 'Spouse_name', 'Spouse_occupation', 'Mother_name', 'Mother_occupation',
            'Father_name', 'Father_occupation', 'Guardian_name', 'Guardian_occupation', 'Medical_History', 'Languages_known', 'Mother_tongue', 'Skills', 'Hobbies',
            'Awards', 'Recognitions', 'Bank_name', 'Branch_name', 'Ifsc_code', 'Account_no', 'Pan_no', 'Designation', 'Date_of_joining', 'Nature_of_appointment',
            'staff_status', 'Temporary_Address', 'Permanent_Address', 'Description'
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
