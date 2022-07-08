# Generated by Django 4.0.6 on 2022-07-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_death_death_reason_divorce_divorce_reason'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='birth',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterModelOptions(
            name='death',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterModelOptions(
            name='divorce',
            options={'ordering': ['husband_first_name', 'wife_first_name']},
        ),
        migrations.AlterModelOptions(
            name='marriage',
            options={'ordering': ['husband_first_name', 'wife_first_name']},
        ),
        migrations.AlterField(
            model_name='birth',
            name='photo',
            field=models.ImageField(height_field='400px', upload_to='birth'),
        ),
    ]
