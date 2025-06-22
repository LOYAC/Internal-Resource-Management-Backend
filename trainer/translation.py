from modeltranslation.translator import translator, TranslationOptions
from .models import Trainer


class TrainerTranslationOptions(TranslationOptions):
    fields = ("first_name", "last_name", "bio")
    required_languages = {
        "en": ("first_name", "last_name", "bio"),
        "ar": ("first_name", "last_name", "bio"),
    }


translator.register(Trainer, TrainerTranslationOptions)
