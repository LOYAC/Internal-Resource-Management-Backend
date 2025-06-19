from modeltranslation.translator import translator, TranslationOptions
from .models import Trainer


class TrainerTranslationOptions(TranslationOptions):
    fields = ("firstName", "lastName", "bio")
    required_languages = {
        "en": ("firstName", "lastName"),
        "ar": ("firstName", "lastName"),
    }


translator.register(Trainer, TrainerTranslationOptions)
