# Generated by Django 4.1.7 on 2023-02-27 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0014_alter_customuser_is_staff_usersubscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name=('staff status',)),
        ),
        migrations.AlterField(
            model_name='usersubscription',
            name='status',
            field=models.BooleanField(choices=[(False, False), (True, True)], default=True),
        ),
    ]
