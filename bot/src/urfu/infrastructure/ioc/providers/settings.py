from dishka import Provider, Scope, provide

from urfu.infrastructure.settings import AppSettings, get_settings


class SettingsProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_app_settings(self) -> AppSettings:
        return get_settings()
