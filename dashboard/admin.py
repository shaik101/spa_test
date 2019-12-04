from django.contrib import admin

# Register your models here.
from  beautyapp.models import Appointment
from .models import Addstaff,Guest

admin.site.register(Appointment)
admin.site.register(Addstaff)
admin.site.register(Guest)

