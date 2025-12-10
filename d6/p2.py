from pathlib import Path
import numpy as np
import re

PATH = Path(__file__).parent

if __name__ == "__main__":
  input_lines = PATH.joinpath("input").read_text().splitlines()
  is_space = np.array(
    [[ch == " " for ch in line] for line in input_lines if re.match(r"^[\d\s]+", line)]
  )
  sep_poses = np.where(is_space.sum(0) == len(is_space))[0]

  mat = []
  for row in input_lines:
    if re.match(r"[\d\s]+", row):
      num_strs = []
      last_pos = 0
      for sep_pos in sep_poses:
        num_strs.append(row[last_pos:sep_pos].rjust(5))
        last_pos = sep_pos + 1
      num_strs.append(row[last_pos:].rjust(5))
      mat.append(num_strs)

  ops_line = next(line for line in input_lines if re.match(r"[*+]", line))
  is_mult = [o == "*" for o in re.findall("[*+]", ops_line)]
  is_plus = [not m for m in is_mult]

  mat = np.array([[list(s) for s in row] for row in mat]).transpose([1, 2, 0])
  mat = np.array(
    [
      [
        int("".join(col)) if any(c != " " for c in col) else 1 * is_mult[r]
        for col in row
      ]
      for r, row in enumerate(mat)
    ]
  )

  print((np.prod(mat, 1) * is_mult + np.sum(mat, 1) * is_plus).sum())
