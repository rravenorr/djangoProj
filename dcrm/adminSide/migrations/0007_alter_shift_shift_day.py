# Generated by Django 5.1.3 on 2024-12-05 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminSide', '0006_employee_password1_employee_password2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='shift_day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=50),
        ),
    ]