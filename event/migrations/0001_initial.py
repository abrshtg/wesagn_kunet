# Generated by Django 4.0.6 on 2022-07-07 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=29)),
                ('photo', models.ImageField(upload_to='')),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(max_length=250)),
                ('nationality', models.CharField(default='Ethiopian', max_length=100)),
                ('mother_fullname', models.CharField(max_length=250)),
                ('mother_nationality', models.CharField(default='Ethiopian', max_length=100)),
                ('father_fullname', models.CharField(max_length=250)),
                ('father_nationality', models.CharField(default='Ethiopian', max_length=100)),
                ('birth_registry_date', models.DateField(auto_now_add=True)),
                ('certificate_given_date', models.DateField(default=django.utils.timezone.now)),
                ('civil_registrar_fullname', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=29)),
                ('birth_date', models.DateField()),
                ('nationality', models.CharField(default='Ethiopian', max_length=100)),
                ('death_date', models.DateField()),
                ('death_place', models.CharField(max_length=250)),
                ('death_registry_date', models.DateField(auto_now_add=True)),
                ('certificate_given_date', models.DateField(default=django.utils.timezone.now)),
                ('civil_registrar_fullname', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Divorce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('husband_first_name', models.CharField(max_length=100)),
                ('husband_middle_name', models.CharField(max_length=100)),
                ('husband_last_name', models.CharField(max_length=100)),
                ('husband_birth_date', models.DateField()),
                ('husband_nationality', models.CharField(default='Ethiopian', max_length=100)),
                ('husband_birth_place', models.CharField(max_length=100)),
                ('husband_birth_zone', models.CharField(max_length=100)),
                ('wife_first_name', models.CharField(max_length=100)),
                ('wife_middle_name', models.CharField(max_length=100)),
                ('wife_last_name', models.CharField(max_length=100)),
                ('wife_birth_date', models.DateField()),
                ('wife_nationality', models.CharField(default='Ethiopian', max_length=100)),
                ('wife_birth_place', models.CharField(max_length=100)),
                ('wife_birth_zone', models.CharField(max_length=100)),
                ('divorce_date', models.DateField()),
                ('divorce_place', models.CharField(max_length=250)),
                ('divorce_registry_date', models.DateField(auto_now_add=True)),
                ('certificate_given_date', models.DateField(default=django.utils.timezone.now)),
                ('civil_registrar_fullname', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Marriage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('husband_first_name', models.CharField(max_length=100)),
                ('husband_middle_name', models.CharField(max_length=100)),
                ('husband_last_name', models.CharField(max_length=100)),
                ('husband_birth_date', models.DateField()),
                ('husband_nationality', models.CharField(default='Ethiopian', max_length=100)),
                ('husband_photo', models.ImageField(upload_to='')),
                ('wife_first_name', models.CharField(max_length=100)),
                ('wife_middle_name', models.CharField(max_length=100)),
                ('wife_last_name', models.CharField(max_length=100)),
                ('wife_birth_date', models.DateField()),
                ('wife_nationality', models.CharField(default='Ethiopian', max_length=100)),
                ('wife_photo', models.ImageField(upload_to='')),
                ('marriage_date', models.DateField()),
                ('marriage_registry_date', models.DateField(auto_now_add=True)),
                ('marriage_region', models.CharField(max_length=100)),
                ('marriage_subcity', models.CharField(max_length=100)),
                ('marriage_zone', models.CharField(max_length=100)),
                ('marriage_kebele', models.CharField(max_length=100)),
                ('marriage_city', models.CharField(max_length=100)),
                ('certificate_given_date', models.DateField(default=django.utils.timezone.now)),
                ('civil_registrar_fullname', models.CharField(max_length=250)),
            ],
        ),
    ]
