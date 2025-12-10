from pathlib import Path
import numpy as np

INPUT_FILE = "input"
file_content = Path(__file__).parent.joinpath(INPUT_FILE).read_text()

if __name__ == "__main__":
  grid = [r for r in file_content.splitlines() if r.strip()]
  n_rows = len(grid)
  n_cols = len(grid[0])

  c_s = next(c for (c, ch) in enumerate(grid[0]) if ch == "S")

  G = np.zeros((n_rows + 1, n_cols), dtype=np.int64)
  G[0, c_s] = 1

  for r in range(1, n_rows + 1):
    for c in range(n_cols):
      if G[r - 1, c] == 0:
        continue

      if grid[r - 1][c] == "^":
        if c - 1 >= 0:
          G[r, c - 1] += G[r - 1, c]
        if c + 1 < n_cols:
          G[r, c + 1] += G[r - 1, c]
      else:
        G[r, c] += G[r - 1, c]

  total_timelines = G[n_rows, :].sum()
  print(G[n_rows, :])
  print(total_timelines)
