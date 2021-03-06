# Generated by Django 3.1 on 2020-09-29 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(default='default.jpg', upload_to='profile_pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Please Enter Your Valid Phone Number.', max_length=128, null=True, region=None)),
                ('house_number', models.CharField(blank=True, help_text='Your Village Name And House Number', max_length=32, null=True)),
                ('division', models.CharField(blank=True, choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Barisal', 'Barisal'), ('Khulna', 'Khulna'), ('Mymensingh', 'Mymensingh'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet')], max_length=15, null=True)),
                ('effective_delivery', models.CharField(blank=True, choices=[('H', 'Home'), ('O', 'Office')], default='H', max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('zone', models.CharField(blank=True, max_length=30, null=True)),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
