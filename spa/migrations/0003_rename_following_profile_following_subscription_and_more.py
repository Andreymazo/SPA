# Generated by Django 4.1.7 on 2023-03-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0002_alter_customuser_is_staff_alter_lesson_preview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='following',
            new_name='following_subscription',
        ),
        migrations.AddField(
            model_name='profile',
            name='following_payment',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers_payments', to='spa.payment', verbose_name='Платежи'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name=('staff status',)),
        ),
    ]