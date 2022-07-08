from ast import Div
from django.contrib import admin
from .models import Birth, Death, Divorce, Marriage
# Register your models here.

admin.site.site_header = "Adama City Civil & Vital Registration"
admin.site.index_title = "Admin"


@admin.register(Birth)
class BirthAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name']


@admin.register(Death)
class DeathAdmin(admin.ModelAdmin):
    pass


@admin.register(Divorce)
class DivorceAdmin(admin.ModelAdmin):
    pass


@admin.register(Marriage)
class MarriageAdmin(admin.ModelAdmin):
    pass
