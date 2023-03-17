from django.apps import AppConfig


class WitnessConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "witness"

    def ready(self):
        import witness.signals
