# Generated by Django 5.0.4 on 2024-05-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('E_mail', models.EmailField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=10)),
                ('Description', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
