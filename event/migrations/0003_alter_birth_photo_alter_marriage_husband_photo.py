# Generated by Django 4.0.6 on 2022-07-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_birth_photo_alter_marriage_husband_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birth',
            name='photo',
            field=models.ImageField(upload_to='birth'),
        ),
        migrations.AlterField(
            model_name='marriage',
            name='husband_photo',
            field=models.ImageField(upload_to='marriage'),
        ),
    ]