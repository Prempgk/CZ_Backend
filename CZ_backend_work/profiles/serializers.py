from django.contrib.auth import authenticate
from oauth2_provider.oauth2_validators import RefreshToken

from rest_framework import serializers
from .models import *
from .models import staff_profile
from django.contrib.auth.models import User, update_last_login


class staff_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = staff_profile
        fields = (
            'id', 'staff_id', 'First_name', 'Middle_name', 'Last_name', 'Dob','Gender', 'Scar', 'Mole', 'Blood_group', 'Religion', 'Nationality', 'Caste', 'Community',
            'Aadhaar_no', 'Mobile_no', 'Alt_mob_no', 'Mail_id', 'Martial_status', 'Spouse_name', 'Spouse_occupation', 'Mother_name', 'Mother_occupation',
            'Father_name', 'Father_occupation', 'Guardian_name', 'Guardian_occupation', 'Medical_History', 'Languages_known', 'Mother_tongue', 'Skills', 'Hobbies',
            'Awards', 'Recognitions', 'Bank_name', 'Branch_name', 'Ifsc_code', 'Account_no', 'Pan_no', 'Designation',  'Date_of_joining', 'Nature_of_appointment',
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


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.user
            refresh_token = str(refresh)
            access_token = str(refresh)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'username': user.username,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")