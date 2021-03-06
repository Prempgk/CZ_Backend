# Generated by Django 4.0.3 on 2022-03-31 06:52

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff_profile',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=100)),
                ('Middle_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=50)),
                ('Dob', models.DateField()),
                ('Gender', models.CharField(max_length=50)),
                ('Scar', models.CharField(max_length=1000)),
                ('Mole', models.CharField(max_length=1000)),
                ('Blood_group', models.CharField(max_length=50)),
                ('Religion', models.CharField(max_length=50)),
                ('Nationality', models.CharField(max_length=100)),
                ('Caste', models.CharField(max_length=20)),
                ('Community', models.CharField(max_length=500)),
                ('Aadhaar_no', models.CharField(max_length=12)),
                ('Mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Alt_mob_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Mail_id', models.EmailField(max_length=254)),
                ('Martial_status', models.CharField(max_length=20)),
                ('Spouse_name', models.CharField(max_length=100)),
                ('Spouse_occupation', models.CharField(max_length=100)),
                ('Mother_name', models.CharField(max_length=100)),
                ('Mother_occupation', models.CharField(max_length=200)),
                ('Father_name', models.CharField(max_length=100)),
                ('Father_occupation', models.CharField(max_length=200)),
                ('Guardian_name', models.CharField(max_length=100)),
                ('Guardian_occupation', models.CharField(max_length=200)),
                ('Medical_History', models.CharField(max_length=1000)),
                ('Temporary_Address', models.CharField(max_length=1000)),
                ('Permanent_Address', models.CharField(max_length=1000)),
                ('Languages_known', models.CharField(max_length=200)),
                ('Mother_tongue', models.CharField(max_length=200)),
                ('Skills', models.CharField(max_length=1000)),
                ('Hobbies', models.CharField(max_length=1000)),
                ('Awards', models.CharField(max_length=1000)),
                ('Recognitions', models.CharField(max_length=1000)),
                ('Designation', models.CharField(max_length=100)),
                ('Date_of_join', models.DateField()),
                ('staff_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='staff_qualification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Degree_name', models.CharField(max_length=50)),
                ('Specialization', models.CharField(max_length=100)),
                ('Year_of_passing', models.CharField(max_length=10)),
                ('Percentage', models.CharField(max_length=10)),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.staff_profile')),
            ],
        ),
        migrations.CreateModel(
            name='staff_experience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Designation', models.CharField(max_length=100)),
                ('Name_of_institution', models.CharField(max_length=100)),
                ('Experience_from', models.DateField()),
                ('Experience_to', models.DateField()),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.staff_profile')),
            ],
        ),
    ]
