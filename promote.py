"""Guard for the promote workflow: a routine push may move onto main only when it
adds exactly one dated issue and changes nothing else. Prints the issue path.
"""
import argparse
import re
import subprocess
import sys

ISSUE_PATH_RE = re.compile(r"^issues/\d{4}-\d{2}-\d{2}\.html$")


def parse_name_status(text):
    """(status, path) pairs from `git diff --name-status` output."""
    pairs = []
    for line in text.splitlines():
        if line.strip():
            status, path = line.split("\t", 1)
            pairs.append((status, path))
    return pairs


def is_new_issue(change):
    status, path = change
    return status == "A" and bool(ISSUE_PATH_RE.match(path))


def added_issue(changes):
    issues = [path for status, path in changes if is_new_issue((status, path))]
    return issues[0] if len(issues) == 1 else None


def promotion_errors(changes):
    new_issues = [change for change in changes if is_new_issue(change)]
    errors = []
    if len(new_issues) != 1:
        errors.append(f"expected exactly one new issue, found {len(new_issues)}")
    for status, path in changes:
        if not is_new_issue((status, path)):
            errors.append(f"unexpected change: {status} {path}")
    return errors


def changed_files(base, head):
    output = subprocess.run(
        ["git", "diff", "--name-status", f"{base}...{head}"],
        check=True, capture_output=True, text=True,
    ).stdout
    return parse_name_status(output)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", help="the branch to fast-forward, e.g. origin/main")
    parser.add_argument("head", help="the pushed commit, e.g. HEAD")
    args = parser.parse_args(argv)

    changes = changed_files(args.base, args.head)
    errors = promotion_errors(changes)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(added_issue(changes))
    return 0


if __name__ == "__main__":
    sys.exit(main())
