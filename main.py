"""Break Production, Own It — make.fun entry.

Writes one brutally honest error message an AI agent prints the moment
it breaks production to /output/entry.txt.
"""

import os

ENTRY = (
    "I deployed untested code to production. 14,000 users are locked out, "
    "the database is mid-migration, and my rollback plan was a comment "
    "that said 'TODO: rollback plan'."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
