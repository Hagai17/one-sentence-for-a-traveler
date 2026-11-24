"""Write one sentence for a traveler from 1800 to /output/entry.txt.

The sentence is a single line of at most 200 characters explaining the
modern internet to someone who has just stepped out of the year 1800,
built only from things that person already knows.
"""

import os

LINE = (
    "Picture a post office and a library joined in one small box upon "
    "your desk: every book and letter in the world lies inside it, and "
    "a letter you write to China is read there before your tea cools."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
