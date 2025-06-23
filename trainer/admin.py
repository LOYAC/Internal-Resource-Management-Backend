from django.contrib import admin
from .models import Trainer


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone")
    exclude = ["first_name", "last_name", "bio"]

    def full_name(self, obj):
        return obj.get_full_name
