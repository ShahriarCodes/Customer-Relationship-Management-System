from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    # for signals
    def ready(self):
        import accounts.signals
