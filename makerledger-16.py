# === Stage 16: Add argparse support for the most common commands ===
# Project: MakerLedger
import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        prog="makerledger",
        description="Workshop build ledger CLI.",
    )
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("list-materials", help="List all materials.")
    p.set_defaults(func=cmd_list_materials)

    p = sub.add_parser("add-material", help="Add a material to the ledger.")
    p.add_argument("--name", required=True)
    p.add_argument("--category", default=None)
    p.add_argument("--cost", type=float, default=0.0)
    p.set_defaults(func=cmd_add_material)

    p = sub.add_parser("list-tasks", help="List all tasks.")
    p.set_defaults(func=cmd_list_tasks)

    p = sub.add_parser("add-task", help="Add a task to the ledger.")
    p.add_argument("--title", required=True)
    p.add_argument("--status", choices=["planned", "in-progress", "done"], default="planned")
    p.set_defaults(func=cmd_add_task)

    p = sub.add_parser("list-costs", help="List all costs.")
    p.set_defaults(func=cmd_list_costs)

    p = sub.add_parser("add-cost", help="Add a cost to the ledger.")
    p.add_argument("--description", required=True)
    p.add_argument("--amount", type=float, required=True)
    p.set_defaults(func=cmd_add_cost)

    p = sub.add_parser("list-experiments", help="List all experiments.")
    p.set_defaults(func=cmd_list_experiments)

    p = sub.add_parser("add-experiment", help="Add an experiment to the ledger.")
    p.add_argument("--name", required=True)
    p.add_argument("--result", default="")
    p.set_defaults(func=cmd_add_experiment)

    p = sub.add_parser("list-snapshots", help="List all project snapshots.")
    p.set_defaults(func=cmd_list_snapshots)

    p = sub.add_parser("add-snapshot", help="Add a project snapshot.")
    p.add_argument("--title", required=True)
    p.add_argument("--note", default="")
    p.set_defaults(func=cmd_add_snapshot)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
