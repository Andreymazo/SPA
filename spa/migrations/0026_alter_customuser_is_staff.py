# Generated by Django 4.1.7 on 2023-03-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0025_remove_profile_following_subscription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name=('staff status',)),
        ),
    ]
