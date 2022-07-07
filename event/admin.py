from ast import Div
from django.contrib import admin
from .models import Birth, Death, Divorce, Marriage
# Register your models here.


admin.site.register(Birth)
admin.site.register(Death)
admin.site.register(Divorce)
admin.site.register(Marriage)