# Generated by Django 4.1.7 on 2023-02-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0015_alter_customuser_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name=('staff status',)),
        ),
    ]
