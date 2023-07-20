from django.apps import AppConfig

from config.base_container import BaseContainer


class DesignerServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'designer_server'

    def ready(self):
        container = BaseContainer()
        container.wire(modules=[".adapter._in.login_hrm_api_controller"])
