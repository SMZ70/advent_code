from pathlib import Path
import re
import itertools

lines = list(
  line.strip()
  for line in Path(__file__).parent.joinpath("input").read_text().splitlines()
  if line
)

if __name__ == "__main__":
  grid = [[ch for ch in s] for s in lines]
  password = 0

  there_is_removable = True
  while there_is_removable:
    new_grid = grid.copy()
    there_is_removable = False
    for i, line in enumerate(grid):
      for j, ch in enumerate(line):
        if ch != "@":
          continue
        n = 0
        for v in itertools.product([-1, 0, 1], [-1, 0, 1]):
          if v[0] == v[1] == 0:
            continue
          if (0 <= i + v[0] < len(grid)) and (0 <= j + v[1] < len(line)):
            to_check = grid[i + v[0]][j + v[1]]
            if to_check == "@":
              n += 1
              if n >= 4:
                break
        else:
          new_grid[i][j] = "."
          password += 1
          there_is_removable = True
    grid = new_grid.copy()
  print(password)
