import os
import argparse
import re
import datetime


def get_start_date():
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    last_21st = datetime.date(last_month.year, last_month.month, 21)

    return last_21st


def remove_special_characters(line):
    line = re.sub("[\t\n\r]", "", line)
    line = re.sub("[^A-Za-z0-9\s_-]+", "", line)

    return line


def create_commitfile(username, start_date, end_date):
    ctdline = (
        'git log --pretty=format:"%ad - %an: %s"'
        f" --after={start_date} --until={end_date} --author=\"{username}\" --oneline >"
        " commit_history.txt"
    )
    os.system(ctdline)


def create_evidence():
    with open("commit_history.txt", "r") as ch:
        lines = ch.readlines()
        for line in lines:
            commit = remove_special_characters(line)
            commit_number = line.split()[0]
            lcommit = commit.split(" ")
            diff_name = "-".join(lcommit) + ".diff"
            save_diff_cmd = f"git show {commit_number} > {diff_name}"
            os.system(save_diff_cmd)


def parse_args_init():
    parser = argparse.ArgumentParser(
        description=(
            "Prepare evidence for CTD in format `<short_commit_id>-<commit_name>.diff`."
        )
    )
    parser.add_argument("--name", help="Your github username", type=str, default=None)
    parser.add_argument(
        "--start_date",
        help="Start date. Default: 21st of previous month.",
        type=str,
        default=get_start_date(),
    )
    parser.add_argument(
        "--end_date",
        help="End date. Default: today's date",
        type=str,
        default=datetime.date.today(),
    )
    parser.add_argument(
        "--outdir", help="Output directory.", type=str, default="CTD_evidences"
    )

    return parser


if __name__ == "__main__":
    parser = parse_args_init()
    args = parser.parse_args()

    result_dir = os.path.join(
        args.outdir, str(args.start_date) + "_" + str(args.end_date)
    )
    os.makedirs(result_dir, exist_ok=True)
    os.chdir(result_dir)

    create_commitfile(args.name, args.start_date, args.end_date)
    create_evidence()
