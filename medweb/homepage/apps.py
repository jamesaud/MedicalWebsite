from django.apps import AppConfig


class HomepageConfig(AppConfig):
    name = 'medweb.homepage'
    verbose_name = "homepage"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
