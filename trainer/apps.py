from django.apps import AppConfig


class TrainerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "trainer"

    def ready(self):
        # Import the translation registration on app ready
        import trainer.translation
