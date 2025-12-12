import polars as pl
from pathlib import Path
from scipy.spatial import distance_matrix
import numpy as np
import itertools

PATH = Path(__file__).parent

if __name__ == "__main__":
  print(
    max(
      (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
      for (x1, y1), (x2, y2) in itertools.combinations(
        pl.read_csv(PATH.joinpath("input"), has_header=False).to_numpy(), 2
      )
    )
  )
