# Generated by Django 2.2 on 2020-01-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlour', '0007_auto_20200121_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='AppoinmentTine',
            field=models.TimeField(null=True),
        ),
    ]
