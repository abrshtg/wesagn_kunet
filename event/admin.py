from ast import Div
from django.contrib import admin
from .models import Birth, Death, Divorce, Marriage
# Register your models here.

admin.site.site_header = "Adama City Civil & Vital Registration"
admin.site.index_title = "Admin"


@admin.register(Birth)
class BirthAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'gender', 'birth_date', 'birth_place', 'birth_registry_date', 'certificate_given_date']
    search_fields = ['first_name']

@admin.register(Death)
class DeathAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'gender', 'death_date', 'death_place', 'death_registry_date', 'certificate_given_date']
    search_fields = ['first_name']

@admin.register(Divorce)
class DivorceAdmin(admin.ModelAdmin):
    list_display = ['husband_first_name', 'husband_middle_name', 'wife_first_name', 'wife_middle_name', 'divorce_date', 'divorce_reason', 'divorce_registry_date', 'certificate_given_date']
    search_fields = ['husband_first_name', 'wife_first_name']
    
@admin.register(Marriage)
class MarriageAdmin(admin.ModelAdmin):
    list_display = ['husband_first_name', 'husband_middle_name', 'wife_first_name', 'wife_middle_name', 'marriage_date', 'marriage_city', 'marriage_registry_date', 'certificate_given_date']
    search_fields = ['husband_first_name', 'wife_first_name']

