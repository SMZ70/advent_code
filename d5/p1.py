from pathlib import Path
import re

CWD = Path(__file__).parent

if __name__ == "__main__":
  input_lines = Path(__file__).parent.joinpath("input").read_text().splitlines()

  fresh_ranges = list(
    range(int(line.split("-")[0]), int(line.split("-")[1]) + 1)
    for line in input_lines
    if "-" in line
  )

  product_ids = list(
    int(line.strip()) for line in input_lines if re.match(r"^\d+$", line.strip())
  )

  print(
    sum(
      1
      for product_id in product_ids
      if any(product_id in fresh_range for fresh_range in fresh_ranges)
    )
  )
