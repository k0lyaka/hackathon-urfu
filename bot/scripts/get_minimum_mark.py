import json  # noqa: INP001
from collections import defaultdict

with open("data.json", encoding="utf-8") as fp:
    data = json.load(fp)

with open("data.csv") as fp:
    lines = [row.split("\t") for row in fp.read().split("\n")]

excluded_entrants = set()

sort_by_spec = defaultdict(list)

for i in data:
    if (
        i["competition"] != "main"
        or i["compensation"] != "budget"
        or i["familirization"] != "Очная"
    ):
        excluded_entrants.add(i["entrant_id"])

for line in lines[1:]:
    entrant_id, a, _, _, z, _, _, spec = line

    if "68" in a or not z:
        continue

    sort_by_spec[spec.split(" ")[0]].append(entrant_id)


for key, entrants in sort_by_spec.items():
    print(
        key,
        min(
            (e["total_mark"], e["entrant_id"])
            for e in data
            if str(e["entrant_id"]) in entrants
            and e["status"] == "Участвует в конкурсе"
            and e["compensation"] == "budget"
            and e["total_mark"] > 0
            and e["competition"] == "main"
            and e["entrant_id"] not in excluded_entrants
            and e["speciality"].startswith(key)
        ),
    )
