# Generated by Django 4.0.6 on 2022-07-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_birth_options_alter_death_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birth',
            name='photo',
            field=models.ImageField(height_field='400', upload_to='birth', width_field='400'),
        ),
    ]
