from dishka import Provider, Scope, provide

from urfu.application.usecases.users.create_or_update import CreateOrUpdateUser


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    # users
    create_or_update_user = provide(CreateOrUpdateUser)
