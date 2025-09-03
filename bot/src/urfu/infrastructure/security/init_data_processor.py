from aiogram.utils.web_app_signature import safe_check_webapp_init_data_from_signature

from urfu.application.common.security.token_processor import TokenProcessor
from urfu.domain.value_objects.user import UserId


class InitDataProcessor(TokenProcessor):
    def create(self, user_id: UserId) -> str:
        raise NotImplementedError

    def verify(self, token: str, **kwargs: str | int) -> int:
        bot_id = kwargs.pop("bot_id")

        if not bot_id:
            raise ValueError("InitDataProcessor requires bot token")

        data = safe_check_webapp_init_data_from_signature(int(bot_id), token)

        if not data.user:
            raise ValueError("initData requires user object")

        return data.user.id
