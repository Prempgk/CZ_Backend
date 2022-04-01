from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import base64
import json
from django.utils.crypto import get_random_string
# Create your models here.
#def new_file_name(instance,filename):
   ## return 'images/{0}{1}'.format(get_random_string(length=10),filename)

#def user_directory_path(instance,filename):
    #return 'images/{0}/'.format(filename)


class staff_profile(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=10, unique=True, null=False, blank=False)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=20, null=True, blank=True)
    Last_name = models.CharField(max_length=5)
    Dob = models.DateField()
    Gender = models.CharField(max_length=10)
    Scar = models.CharField(max_length=200, null=True, blank=True)
    Mole = models.CharField(max_length=200, null=True, blank=True)
    Blood_group = models.CharField(max_length=20)
    Religion = models.CharField(max_length=20)
    Nationality = models.CharField(max_length=20)
    Caste = models.CharField(max_length=50, null=True, blank=True)
    Community = models.CharField(max_length=30, null=True, blank=True)
    Aadhaar_no = models.CharField(max_length=12)
    Mobile_no = PhoneNumberField(unique=True, null=False, blank=False)
    Alt_mob_no = PhoneNumberField(unique=True, null=True, blank=False)
    Mail_id = models.EmailField(unique=True)
    Martial_status = models.CharField(max_length=10)
    Spouse_name = models.CharField(max_length=30, null=True, blank=True)
    Spouse_occupation = models.CharField(max_length=30, null=True, blank=True)
    Mother_name = models.CharField(max_length=20)
    Mother_occupation = models.CharField(max_length=30, null=True, blank=True)
    Father_name = models.CharField(max_length=20)
    Father_occupation = models.CharField(max_length=30, null=True, blank=True)
    Guardian_name = models.CharField(max_length=20, null=True, blank=True)
    Guardian_occupation = models.CharField(max_length=30, null=True, blank=True)
    Medical_History = models.CharField(max_length=50, null=True, blank=True)
    Languages_known = models.CharField(max_length=100)
    Mother_tongue = models.CharField(max_length=20)
    Skills = models.CharField(max_length=100,null=True, blank=True)
    Hobbies = models.CharField(max_length=100,null=True, blank=True)
    Awards = models.CharField(max_length=1000,null=True, blank=True)
    Recognitions = models.CharField(max_length=100,null=True, blank=True)
    Bank_name = models.CharField(max_length=50)
    Branch_name = models.CharField(max_length=30)
    Ifsc_code = models.CharField(max_length=20)
    Account_no = models.CharField(max_length=30, unique=True)
    Pan_no = models.CharField(max_length=10, unique=True)
    Designation = models.CharField(max_length=20)
    Date_of_joining = models.DateField()
    Nature_of_appointment = models.CharField(max_length=20)
    staff_status = models.CharField(max_length=10)
    Temporary_Address = models.CharField(max_length=250, default=False)
    Permanent_Address = models.CharField(max_length=250, default=False)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    # Profile_pic = models.ImageField(upload_to=user_directory_path,default='posts/default.jpg')
    def __int__(self):
        return self.staff_id

class staff_qualification(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=10)
    Degree_name = models.CharField(max_length=10)
    Specialization = models.CharField(max_length=100)
    Year_of_passing = models.CharField(max_length=4)
    Percentage = models.CharField(max_length=4)

class staff_experience(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=10)
    Designation = models.CharField(max_length=20)
    Name_of_institution = models.CharField(max_length=100)
    Experience_from = models.DateField()
    Experience_to = models.DateField()

