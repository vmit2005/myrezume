from django.contrib import admin
from .models import  Rezume, Acad, Arbeit, Proggg
from telebot.models import Telesettings

admin.site.register(Rezume)
admin.site.register(Acad)
admin.site.register(Arbeit)
admin.site.register(Proggg)
admin.site.register(Telesettings)

# Register your models here.
