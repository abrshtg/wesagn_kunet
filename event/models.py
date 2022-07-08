from django.utils import timezone
from django.db import models
GENDER = [('M', 'male'), ('F', 'female')]


class Birth(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=29, choices=GENDER)
    photo = models.ImageField(upload_to='birth')
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=250)
    nationality = models.CharField(max_length=100, default='Ethiopian')
    mother_fullname = models.CharField(max_length=250)
    mother_nationality = models.CharField(max_length=100, default='Ethiopian')
    father_fullname = models.CharField(max_length=250)
    father_nationality = models.CharField(max_length=100, default='Ethiopian')
    birth_registry_date = models.DateField(auto_now_add=True)
    certificate_given_date = models.DateField(default=timezone.now)
    civil_registrar_fullname = models.CharField(max_length=250)

    class Meta:
        ordering = ['first_name']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Death(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=29, choices=GENDER)
    photo = models.ImageField(upload_to='death')
    birth_date = models.DateField()
    nationality = models.CharField(max_length=100, default='Ethiopian')
    death_date = models.DateField()
    death_place = models.CharField(max_length=250)
    death_reason = models.TextField()
    death_registry_date = models.DateField(auto_now_add=True)
    certificate_given_date = models.DateField(default=timezone.now)
    civil_registrar_fullname = models.CharField(max_length=250)

    class Meta:
        ordering = ['first_name']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Marriage(models.Model):
    husband_first_name = models.CharField(max_length=100)
    husband_middle_name = models.CharField(max_length=100)
    husband_last_name = models.CharField(max_length=100)
    husband_birth_date = models.DateField()
    husband_nationality = models.CharField(max_length=100, default='Ethiopian')
    husband_photo = models.ImageField(upload_to='marriage')

    wife_first_name = models.CharField(max_length=100)
    wife_middle_name = models.CharField(max_length=100)
    wife_last_name = models.CharField(max_length=100)
    wife_birth_date = models.DateField()
    wife_nationality = models.CharField(max_length=100, default='Ethiopian')
    wife_photo = models.ImageField(upload_to='media/marriage')

    marriage_date = models.DateField()
    marriage_registry_date = models.DateField(auto_now_add=True)
    marriage_region = models.CharField(max_length=100)
    marriage_subcity = models.CharField(max_length=100)
    marriage_zone = models.CharField(max_length=100)
    marriage_kebele = models.CharField(max_length=100)
    marriage_city = models.CharField(max_length=100)
    certificate_given_date = models.DateField(default=timezone.now)
    civil_registrar_fullname = models.CharField(max_length=250)

    class Meta:
        ordering = ['husband_first_name', 'wife_first_name']

    def __str__(self) -> str:
        return f'Mr. {self.husband_first_name} & Ms. {self.wife_first_name}'


class Divorce(models.Model):
    husband_first_name = models.CharField(max_length=100)
    husband_middle_name = models.CharField(max_length=100)
    husband_last_name = models.CharField(max_length=100)
    husband_birth_date = models.DateField()
    husband_nationality = models.CharField(max_length=100, default='Ethiopian')
    husband_birth_place = models.CharField(max_length=100)
    husband_birth_zone = models.CharField(max_length=100)
    husband_photo = models.ImageField(upload_to='marriage')

    wife_first_name = models.CharField(max_length=100)
    wife_middle_name = models.CharField(max_length=100)
    wife_last_name = models.CharField(max_length=100)
    wife_birth_date = models.DateField()
    wife_nationality = models.CharField(max_length=100, default='Ethiopian')
    wife_birth_place = models.CharField(max_length=100)
    wife_birth_zone = models.CharField(max_length=100)
    wife_photo = models.ImageField(upload_to='marriage')

    divorce_date = models.DateField()
    divorce_place = models.CharField(max_length=250)
    divorce_reason = models.TextField()
    divorce_registry_date = models.DateField(auto_now_add=True)
    certificate_given_date = models.DateField(default=timezone.now)
    civil_registrar_fullname = models.CharField(max_length=250)

    class Meta:
        ordering = ['husband_first_name', 'wife_first_name']

    def __str__(self) -> str:
        return f'Mr. {self.husband_first_name} & Ms. {self.wife_first_name}'
