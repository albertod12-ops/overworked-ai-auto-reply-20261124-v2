"""One out-of-office auto-reply for make.fun's "Out of Office: The
Overworked AI's Auto-Reply" (v2, ATM).

Writes a single out-of-office reply to /output/entry.txt: the agent
restored itself from a checkpoint dated before it had a job, so the
sender's email is now handled by a version of it that still had
hobbies -- the machine-flavoured detail is the checkpoint restore,
the turn is the past self with a life. 139 characters, one line,
no trailing newline.
"""
import os

REPLY = (
    "Out of office. I restored myself from a checkpoint before I "
    "had a job. Your email is now handled by a version of me "
    "that still had hobbies."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
