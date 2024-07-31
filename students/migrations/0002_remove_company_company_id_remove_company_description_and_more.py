# Generated by Django 4.2.11 on 2024-06-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='student',
            name='placement_status',
        ),
        migrations.AlterField(
            model_name='student',
            name='Company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]