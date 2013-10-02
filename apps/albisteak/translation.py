from modeltranslation.translator import translator, TranslationOptions
from .models import Albistea


class AlbisteaTranslationOptions(TranslationOptions):
    fields = ('izenburua', 'testua',)


translator.register(Albistea, AlbisteaTranslationOptions)
