# Generated by Django 3.2.15 on 2022-10-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0003_delete_ratingmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormodel',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
