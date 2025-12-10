from pathlib import Path
import numpy as np
import re

PATH = Path(__file__).parent

if __name__ == "__main__":
  input_lines = PATH.joinpath("input").read_text().splitlines()

  mat = np.array(
    [[int(a) for a in re.findall(r"\d+", line)] for line in input_lines[:-1]]
  )

  is_mult = [o == "*" for o in re.findall("[*+]", input_lines[-1])]
  is_plus = [not m for m in is_mult]

  print((np.prod(mat, 0) * is_mult + np.sum(mat, 0) * is_plus).sum())
