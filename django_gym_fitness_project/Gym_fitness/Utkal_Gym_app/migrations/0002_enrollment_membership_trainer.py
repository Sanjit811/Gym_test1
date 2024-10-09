# Generated by Django 5.0.4 on 2024-05-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Utkal_Gym_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('Enrollment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Enrollment_Full_Name', models.CharField(max_length=100)),
                ('Enrollment_Email', models.EmailField(max_length=100)),
                ('Enrollment_Gender', models.CharField(max_length=100)),
                ('Enrollment_Number', models.CharField(max_length=100)),
                ('Enrollment_DOB', models.CharField(max_length=100)),
                ('Enrollment_Selecte_membership_plan', models.CharField(max_length=100)),
                ('Enrollment_Selected_Trainer', models.CharField(max_length=100)),
                ('Enrollment_Reference', models.CharField(max_length=100)),
                ('Enrollment_Address', models.TextField(max_length=1000)),
                ('Enrollment_Payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('Enrollment_price', models.CharField(max_length=100, null=True)),
                ('Enrollment_DueDate', models.DateTimeField(blank=True, null=True)),
                ('Enrollment_JoiningDate', models.DateTimeField(auto_now_add=True)),
                ('is_Active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('Plan_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Plan_Name', models.CharField(max_length=150)),
                ('plan_price', models.IntegerField()),
                ('is_Active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('Trainer_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Trainer_Name', models.CharField(max_length=150)),
                ('Trainer_Gender', models.CharField(max_length=15)),
                ('Trainer_Phone', models.CharField(max_length=10)),
                ('Trainer_salary', models.IntegerField()),
                ('Trainer_JoiningDate', models.DateTimeField(auto_now_add=True)),
                ('is_Active', models.BooleanField()),
            ],
        ),
    ]
