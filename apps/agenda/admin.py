from django.contrib import admin
from .models import Ebentua
from modeltranslation.admin import TranslationAdmin


class EbentuaAdmin(TranslationAdmin):
    pass


admin.site.register(Ebentua, EbentuaAdmin)
