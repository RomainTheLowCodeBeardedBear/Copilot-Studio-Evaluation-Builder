"""Render a prepared evaluation specification into a workbook, Studio CSV and setup guide."""
import argparse
import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_DEFLATED

from openpyxl import load_workbook
from openpyxl.styles import Alignment
from export_conversations import HEADER, validate


def build(spec, archive):
    rows = []
    review = []
    for n, chat in enumerate(spec["conversations"], 1):
        if not chat:
            raise ValueError(f"Empty conversation {n}")
        for i, turn in enumerate(chat, 1):
            rows.append([n, turn["question"], turn.get("response", "")])
            review.append([f"{n}.{i}", turn["accept"], turn["evidence"], turn["fail"]])
    checked = validate([HEADER, *rows])
    fields = list(spec["settings"].items())
    if not fields or any(not str(v).strip() for row in fields + review for v in row):
        raise ValueError("Complete every setting and acceptance check")
    with TemporaryDirectory() as tmp:
        folder = Path(tmp)
        book = load_workbook(Path(__file__).resolve().parents[1] / "templates/conversations.xlsx")
        for sheet, data in zip(("Conversations", "Reviewer", "Method"), (rows, review, fields)):
            ws = book[sheet]
            ws.delete_rows(2, ws.max_row)
            for row in data:
                ws.append(row)
                for cell in ws[ws.max_row]:
                    if isinstance(cell.value, str):
                        cell.data_type = "s"
                    cell.alignment = Alignment(wrap_text=True, vertical="top")
            ws.auto_filter.ref = ws.dimensions
        book.save(folder / "authoring.xlsx")
        with (folder / "conversations.csv").open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.writer(stream, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
            writer.writerow(HEADER)
            writer.writerows(checked)
        setup = [spec["setup"], *[f"**{k}**\n\n{v}" for k, v in fields]]
        (folder / "setup.md").write_text("\n\n".join(setup) + "\n", encoding="utf-8")
        (folder / "review.md").write_text("\n\n".join(
            f"## {ref}\n\n{accept}\n\n{source}\n\n{fail}" for ref, accept, source, fail in review
        ) + "\n", encoding="utf-8")
        with ZipFile(archive, "w", ZIP_DEFLATED) as z:
            for p in sorted(folder.iterdir()):
                z.write(p, p.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("archive", type=Path)
    args = parser.parse_args()
    build(json.loads(args.spec.read_text(encoding="utf-8-sig")), args.archive)
