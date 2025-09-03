import json

from openai import AsyncOpenAI

from urfu.infrastructure.adapters.openai.prompts import USER_TAGS_PROMPT


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

        return response.choices[0].message.content

    async def create_tags_from_user_input(
        self, user_input: str, model: str | None = None
    ) -> list[str]:
        response = await self._make_completion(USER_TAGS_PROMPT, user_input, model)
        return json.loads(response)
