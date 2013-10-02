from modeltranslation.translator import translator, TranslationOptions
from .models import Ebentua


class EbentuaTranslationOptions(TranslationOptions):
    fields = ('ebentua', 'lekua',)


translator.register(Ebentua, EbentuaTranslationOptions)

