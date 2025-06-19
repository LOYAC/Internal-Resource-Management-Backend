from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Trainer


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone")
    exclude = ["firstName", "lastName", "bio"]

    def full_name(self, obj):
        return "{} {}".format(obj.firstName, obj.lastName)
