from django.apps import AppConfig


class OurServicesPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'our_services_page'

    def ready(self):
        import our_services_page.signals