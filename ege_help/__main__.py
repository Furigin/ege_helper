import argparse

from .help import get_task, list_tasks


def build_parser():
    parser = argparse.ArgumentParser(
        description="Шпаргалка по заданиям ЕГЭ по информатике.",
    )
    parser.add_argument(
        "task",
        nargs="?",
        type=int,
        help="Номер задания (1-27).",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Показать список доступных заданий.",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.list:
        print(
            "Доступные задания: "
            + ", ".join(str(num) for num in list_tasks())
        )
        return

    if args.task is None:
        parser.print_help()
        return

    task = get_task(args.task)
    task()


if __name__ == "__main__":
    main()
