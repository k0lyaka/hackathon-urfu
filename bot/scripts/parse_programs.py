import asyncio
import os

from httpx import AsyncClient, Timeout
from pydantic import BaseModel

SCORES_2025 = {
    "10.03.01": 238,
    "09.03.01": 233,
    "11.03.03": 202,
    "11.05.01": 173,
    "29.03.03": 188,
    "09.03.04": 264,
    "09.03.03": 229,
    "11.03.02": 214,
    "10.05.02": 217,
    "11.03.01": 201,
    "10.05.04": 225,
    "27.03.04": 219,
}

BASE_API_URL = os.getenv("API_URL") or "http://localhost:8888"


class ProgramItem(BaseModel):
    slug: str
    isTop: bool | None
    name: str
    code: str
    manager: str

    duration: int | float
    passingScore: int | None
    budgetSeatsCount: int | None

    description: str | None = None

    level: str


class Response(BaseModel):
    items: list[ProgramItem]


class Parser:
    def __init__(self) -> None:
        self.client = AsyncClient(
            base_url="https://priem-rtf.urfu.ru", timeout=Timeout(60)
        )

    async def get_programs(self) -> Response:
        response = await self.client.get("/data/cms-programs.json-1.json")
        data = response.json()
        return Response(**data)

    async def get_program_description(self, slug: str) -> str:
        response = await self.client.get(f"/page-data/program/{slug}/page-data.json")
        data = response.json()

        return str(
            data["result"]["data"]["strapiProgrammy"]["description"]["data"][
                "description"
            ]
        ).replace("\n", " ")

    async def parse(self) -> list[ProgramItem]:
        programs = (await self.get_programs()).items

        for program in programs:
            print(program.slug)
            try:
                program.description = await self.get_program_description(program.slug)
            except:
                print("FAIL")
                continue

        return list(filter(lambda x: x.level in ("bachelor", "specialist"), programs))


async def main() -> None:
    inst = Parser()
    results = await inst.parse()

    client = AsyncClient(timeout=Timeout(120))

    for program in results:
        payload = {
            "name": program.name,
            "code": program.code,
            "institute": "ИРИТ-РТФ",
            "description": program.description,
            "scores": [
                {"year": 2025, "minimal_score": SCORES_2025[program.code]},
                {"year": 2024, "minimal_score": program.passingScore},
            ],
        }

        await client.post(
            f"{BASE_API_URL}/specialization",
            json=payload,
            headers={
                "Authorization": str(os.getenv("TOKEN")),
            },
        )

        print(f"uploaded {program.name}")


if __name__ == "__main__":
    asyncio.run(main())
