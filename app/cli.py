import argparse
import json
import os

from app.prep import run_prep
from app.kb import init_db, snapshot


def scenario_b():
    runs = [
        [5, 8],
        [6, 8, 9],
        [8]
    ]

    for i, sections in enumerate(runs, 1):
        result = run_prep(sections)

        folder = f"outputs/scenario_b_iter{i}"
        os.makedirs(folder, exist_ok=True)

        with open(f"{folder}/questions_iter{i}.json", "w") as f:
            json.dump(result, f, indent=2)

        with open(f"{folder}/kb_snapshot_iter{i}.json", "w") as f:
            json.dump(snapshot(), f, indent=2)

        print(f"saved iteration {i}")


if __name__ == "__main__":
    init_db()

    parser = argparse.ArgumentParser()
    parser.add_argument("--sections", nargs="+", type=int)
    parser.add_argument("--scenario_b", action="store_true")

    args = parser.parse_args()

    if args.scenario_b:
        scenario_b()

    elif args.sections:
        result = run_prep(args.sections)
        print(json.dumps(result, indent=2))