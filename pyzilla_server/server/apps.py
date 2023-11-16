from django.apps import AppConfig


class PyzillaServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pyzilla_server'

    # def ready(self):
    #     from server import server
    #     server.start()