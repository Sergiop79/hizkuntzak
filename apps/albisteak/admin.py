from django.contrib import admin
from .models import Albistea
from modeltranslation.admin import TranslationAdmin


class AlbisteaAdmin(TranslationAdmin):
    pass

    class Media:
        js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textarea.js')


admin.site.register(Albistea, AlbisteaAdmin)
