import json
from typing import cast

from openai import AsyncOpenAI

from urfu.infrastructure.adapters.openai.prompts import (
    PROGRAM_TAGS_PROMPT,
    USER_TAGS_PROMPT,
)

TOP_TRACK_CODES = ("09.03.03", "09.03.04")
ALGO_TRACK_CODES = ("09.03.04",)


class AiAdapter:
    DEFAULT_MODEL: str = "deepseek-chat"

    def __init__(
        self, access_token: str, base_url: str = "https://api.deepseek.com"
    ) -> None:
        self._client = AsyncOpenAI(
            api_key=access_token,
            base_url=base_url,
        )

    async def _make_completion(
        self, prompt: str, user_input: str, model: str | None = None
    ) -> str:
        model = model or self.DEFAULT_MODEL

        response = await self._client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input},
            ],
            stream=False,
        )

        return cast(str, response.choices[0].message.content)

    async def create_tags_from_user_input(
        self, user_input: str, model: str | None = None, **kwargs: str
    ) -> list[str]:
        response = await self._make_completion(
            USER_TAGS_PROMPT.format(**kwargs), user_input, model
        )
        return cast(list[str], json.loads(response))

    async def create_tags_from_program_description(
        self,
        program_name: str,
        program_code: str,
        program_description: str,
        model: str | None = None,
    ) -> list[str]:
        program_description = (
            f"Наименование программы: {program_name}\n"
            f"Код программы: {program_code}\n"
            f"Институт: ИРИТ-РТФ, УрФУ\n\n"
        ) + program_description

        if program_code in TOP_TRACK_CODES:
            program_description += "\nМОЖНО ПОСТУПИТЬ НА ТОП-ТРЕК"
        if program_code in ALGO_TRACK_CODES:
            program_description += "\nМОЖНО ПОСТУПИТЬ НА АЛГО-ТРЕК"

        response = await self._make_completion(
            PROGRAM_TAGS_PROMPT, program_description, model
        )

        print(response)

        return cast(list[str], json.loads(response))
