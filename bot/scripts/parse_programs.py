import asyncio
import pprint

from httpx import AsyncClient, Timeout
from pydantic import BaseModel


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
    pprint.pprint(await inst.parse())


if __name__ == "__main__":
    asyncio.run(main())
