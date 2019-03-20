from django.apps import AppConfig


class UserinfoConfig(AppConfig):
    name = 'UserInfo'

    def ready(self):
    	import UserInfo.signals
