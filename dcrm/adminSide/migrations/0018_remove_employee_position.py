# Generated by Django 5.1.3 on 2024-12-05 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminSide', '0017_alter_employee_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
    ]
