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
    First_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=100,null=True)
    Last_name = models.CharField(max_length=50)
    Dob = models.DateField()
    Gender = models.CharField(max_length=50)
    Scar = models.CharField(max_length=1000)
    Mole = models.CharField(max_length=1000)
    Blood_group = models.CharField(max_length=50)
    Religion = models.CharField(max_length=50)
    Nationality = models.CharField(max_length=100)
    Caste = models.CharField(max_length=20,null=True)
    Community = models.CharField(max_length=500,null=True)
    Aadhaar_no = models.CharField(max_length=12)
    Mobile_no = PhoneNumberField(unique=True, null=False, blank=False)
    Alt_mob_no = PhoneNumberField(unique=True, null=False, blank=False)
    Mail_id = models.EmailField()
    Martial_status = models.CharField(max_length=20)
    Spouse_name = models.CharField(max_length=100,null=True)
    Spouse_occupation = models.CharField(max_length=100,null=True)
    Mother_name = models.CharField(max_length=100)
    Mother_occupation = models.CharField(max_length=200)
    Father_name = models.CharField(max_length=100)
    Father_occupation = models.CharField(max_length=200)
    Guardian_name = models.CharField(max_length=100,null=True)
    Guardian_occupation = models.CharField(max_length=200,null=True)
    Medical_History = models.CharField(max_length=1000,null=True)
    Languages_known = models.CharField(max_length=200)
    Mother_tongue = models.CharField(max_length=200)
    Skills = models.CharField(max_length=1000)
    Hobbies = models.CharField(max_length=1000)
    Awards = models.CharField(max_length=1000,null=True)
    Recognitions = models.CharField(max_length=1000,null=True)
    # Profile_pic = models.ImageField(upload_to=user_directory_path,default='posts/default.jpg')
    def __int__(self):
        return self.staff_id

class staff_qualification(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=10)
    Degree_name = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=100)
    Year_of_passing = models.CharField(max_length=10)
    Percentage = models.CharField(max_length=10)

class staff_experience(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=10)
    Designation = models.CharField(max_length=100)
    Name_of_institution = models.CharField(max_length=100)
    Experience_from = models.DateField()
    Experience_to = models.DateField()

class staff_current_address(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=10,unique=True,null=False,blank=False)
    Door_no = models.CharField(max_length=20)
    Street = models.CharField(max_length=50)
    Village = models.CharField(max_length=100)
    District = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=20)

class staff_permanent_address(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=10,unique=True,null=False,blank=False)
    Door_no = models.CharField(max_length=20)
    Street = models.CharField(max_length=50)
    Village = models.CharField(max_length=100)
    District = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=20)

class staff_joining_details(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=10,unique=True,null=False,blank=False)
    Designation = models.CharField(max_length=50)
    Date_of_joining = models.DateField()
    Nature_of_appointment = models.CharField(max_length=50)
    staff_status = models.CharField(max_length=10)

class staff_bank_details(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=10,unique=True,null=False,blank=False)
    Bank_name = models.CharField(max_length=100)
    Branch_name = models.CharField(max_length=50)
    Ifsc_code = models.CharField(max_length=50)
    Account_no = models.CharField(max_length=30)
    Pan_no = models.CharField(max_length=20)
