from django.apps import AppConfig


class DfirtrackMainConfig(AppConfig):
    name = 'dfirtrack_main'

    def ready(self):
        import dfirtrack_main.signals
