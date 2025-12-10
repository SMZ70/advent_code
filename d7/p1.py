from pathlib import Path

file_content = Path(__file__).parent.joinpath("input").read_text()

if __name__ == "__main__":
  rows = [r for r in file_content.splitlines() if r.strip()]

  beams = {next(i for (i, c) in enumerate(rows[0]) if c == "S")}
  total_splits = 0
  for r, row in enumerate(rows[2:], start=2):
    split_points = [i for (i, c) in enumerate(row) if c == "^"]
    for s in split_points:
      if s in beams:
        total_splits += 1
        beams.remove(s)
        if s - 1 >= 0:
          beams.add(s - 1)
        if s + 1 < len(rows[0]):
          beams.add(s + 1)

  print(total_splits)
