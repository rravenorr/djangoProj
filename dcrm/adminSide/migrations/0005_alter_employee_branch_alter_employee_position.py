# Generated by Django 5.1.3 on 2024-12-05 03:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminSide', '0004_remove_employee_name_employee_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminSide.branch'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Employee', 'Employee')], default='Employee', max_length=50),
        ),
    ]
