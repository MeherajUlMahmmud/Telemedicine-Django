# Generated by Django 3.2.13 on 2022-05-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OTScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('', 'Select Status'), ('Pending', 'Pending'), ('Approved', 'Approved'), ('Completed', 'Completed'), ('In Progress', 'In Progress'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'OT Schedule',
                'verbose_name_plural': 'OT Schedules',
            },
        ),
    ]
