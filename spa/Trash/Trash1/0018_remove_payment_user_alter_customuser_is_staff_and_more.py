# Generated by Django 4.1.7 on 2023-03-01 12:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0017_alter_customuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name=('staff status',)),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Персональная ссылка')),
                ('bio', models.TextField(blank=True, max_length=500, verbose_name='Информация о себе')),
                ('avatar', models.ImageField(blank=True, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg'))], verbose_name='Аватар профиля')),
                ('date_birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('following', models.ManyToManyField(blank=True, related_name='followers', to='spa.profile', verbose_name='Подписки')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили пользователей',
                'ordering': ('user',),
            },
        ),
        migrations.AddField(
            model_name='course',
            name='pro_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spa.profile'),
        ),
        migrations.AddField(
            model_name='payment',
            name='pro_filee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='spa.profile', verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='usersubscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spa.profile'),
        ),
    ]