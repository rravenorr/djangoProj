# Generated by Django 5.1.3 on 2024-12-05 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminSide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('shift_id', models.AutoField(primary_key=True, serialize=False)),
                ('shift_start', models.TimeField()),
                ('shift_end', models.TimeField()),
                ('shift_day', models.CharField(max_length=50)),
                ('shift_branch', models.CharField(max_length=50)),
                ('employees', models.ManyToManyField(related_name='shifts', to='adminSide.employee')),
            ],
        ),
    ]
