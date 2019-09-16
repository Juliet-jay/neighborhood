from django.apps import AppConfig


class HoodConfig(AppConfig):
    name = 'hood'
    
    def ready(self):
        print('readdddddddddddddy')
        import hood.signals
