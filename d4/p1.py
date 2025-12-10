from pathlib import Path
import re
import itertools

lines = list(
  line.strip()
  for line in Path(__file__).parent.joinpath("sample_input").read_text().splitlines()
  if line
)

if __name__ == "__main__":
  password = 0
  for i, line in enumerate(lines):
    for j, ch in enumerate(line):
      if ch != "@":
        continue
      n = 0
      for v in itertools.product([-1, 0, 1], [-1, 0, 1]):
        if (0 <= i + v[0] < len(lines)) and (0 <= j + v[1] < len(line)):
          to_check = lines[i + v[0]][j + v[1]]
          if to_check == "@":
            n += 1
        if n > 4:
          break
      else:
        password += 1
  print(password)
