"""Export one Studio conversation set from the worksheet named Conversations."""
import argparse
import csv
from pathlib import Path

HEADER = ("conversationNumber", "question", "response")


def validate(rows):
    if not rows or tuple(rows[0]) != HEADER:
        raise ValueError("Expected header: " + ",".join(HEADER))
    counts = {}
    output = []
    previous = None
    for line, row in enumerate(rows[1:], 2):
        if not any(value is not None and value != "" for value in row):
            continue
        if len(row) != 3:
            raise ValueError(f"Row {line}: expected three columns")
        number, question, response = row
        number = str(number)
        if not number.isascii() or not number.isdecimal() or int(number) < 1 or str(int(number)) != number:
            raise ValueError(f"Row {line}: use a positive integer conversation number")
        if number != previous and number in counts:
            raise ValueError(f"Row {line}: keep turns of each chat together")
        if not isinstance(question, str) or not question.strip() or len(question) > 1000:
            raise ValueError(f"Row {line}: question must contain 1 to 1000 characters")
        counts[number] = counts.get(number, 0) + 1
        if counts[number] > 6 or len(counts) > 20:
            raise ValueError(f"Row {line}: exceeds the bundled Studio template limits")
        output.append((number, question, "" if response is None else str(response)))
        previous = number
    if not output:
        raise ValueError("Add at least one question")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", nargs="?", type=Path, help="CSV destination; omit to validate only")
    args = parser.parse_args()
    if args.input.suffix.lower() == ".xlsx":
        from openpyxl import load_workbook
        book = load_workbook(args.input, read_only=True)
        sheet = book["Conversations"]
        rows = []
        for row in sheet.iter_rows():
            if any(cell.data_type == "f" for cell in row):
                raise ValueError("Enter literal values in Conversations; formula cells are ambiguous")
            rows.append([cell.value for cell in row])
        book.close()
    else:
        with args.input.open(encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.reader(stream, strict=True))
        while rows and len(rows[0]) == 1 and rows[0][0].startswith("#"):
            rows.pop(0)
    output = validate(rows)
    if args.output:
        if args.output.suffix.lower() != ".csv" or args.output.resolve() == args.input.resolve():
            raise ValueError("Choose a separate .csv destination")
        with args.output.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(HEADER)
            writer.writerows(output)
    print(f"{len(set(row[0] for row in output))} conversations, {len(output)} user turns")


if __name__ == "__main__":
    main()
