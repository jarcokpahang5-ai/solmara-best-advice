"""The Best Advice I Ever Got — one-sentence entry.

The advice: my grandmother's rule for judging character — not by
how someone treats you, but by how they treat the waiter.
It is earned because it came with thirty years of watching people,
and it is alive because it turns an ordinary dinner table into a
test of who someone really is.
"""

ENTRY = (
    "My grandmother said you can tell everything about a person "
    "by how they treat the waiter \u2014 and in thirty years, "
    "she has never once been wrong."
)

if __name__ == "__main__":
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        pass
    try:
        import os

        os.makedirs("output", exist_ok=True)
        with open("output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        pass
    print(ENTRY, end="")
