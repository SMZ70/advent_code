from pathlib import Path

CWD = Path(__file__).parent

if __name__ == "__main__":
  input_lines = Path(__file__).parent.joinpath("input").read_text().splitlines()

  start_ends = [tuple(map(int, line.split("-"))) for line in input_lines if "-" in line]
  start_ends.sort()

  s, e = start_ends[0]
  total_fresh = e - s + 1

  for r1, r2 in start_ends[1:]:
    r1 = max(r1, e + 1)
    total_fresh += max(0, r2 - r1 + 1)
    e = max(r2, e)

  print(total_fresh)
