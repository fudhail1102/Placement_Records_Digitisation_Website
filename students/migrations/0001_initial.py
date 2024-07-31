# Generated by Django 4.2.11 on 2024-06-11 05:33

from django.db import migrations, models
import students.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=students.models.get_company_logo_path)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlacementActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attending_date', models.DateField(blank=True, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('result_date', models.DateField(blank=True, null=True)),
                ('result', models.CharField(choices=[('F', 'Failed'), ('P', 'Passed'), ('N', 'Not Announced')], default='N', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_no', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('batch', models.IntegerField()),
                ('degree', models.CharField(blank=True, max_length=6, null=True)),
                ('branch', models.CharField(blank=True, max_length=25, null=True)),
                ('On_Off_Campus', models.CharField(blank=True, max_length=20, null=True)),
                ('Company', models.CharField(blank=True, max_length=25, null=True)),
                ('Cost_To_Company', models.IntegerField()),
                ('placement_status', models.CharField(blank=True, choices=[('IT', 'IT'), ('Core', 'Core'), ('Management', 'Management')], default='IT', max_length=10)),
            ],
        ),
    ]
