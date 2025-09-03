from dishka import Provider, Scope, provide

from urfu.application.usecases.exam_scores.add_exam_scores import AddExamScores
from urfu.application.usecases.users.create_or_update import CreateOrUpdateUser
from urfu.application.usecases.users.get import GetUser
from urfu.application.usecases.users.update_interests import UpdateInterests


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    # users
    get_user = provide(GetUser)
    create_or_update_user = provide(CreateOrUpdateUser)
    update_user_interests = provide(UpdateInterests)

    # exam scores
    add_exam_scores = provide(AddExamScores)
