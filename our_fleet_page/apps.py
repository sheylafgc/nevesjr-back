from django.apps import AppConfig


class OurFleetPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'our_fleet_page'

    def ready(self):
        import our_fleet_page.signals