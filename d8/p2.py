import polars as pl
from pathlib import Path
from scipy.spatial import distance_matrix
import numpy as np

PATH = Path(__file__).parent

if __name__ == "__main__":
  mat = pl.read_csv(PATH.joinpath("input"), has_header=False).to_numpy()
  n_points = len(mat)

  dist_mat = distance_matrix(mat, mat)
  for n in range(n_points):
    dist_mat[n, n] = np.inf

  arcs = list(
    {
      (float(dist_mat[n1, n2]), n1, n2)
      for n1 in range(n_points)
      for n2 in range(n1 + 1, n_points)
    }
  )
  arcs.sort()

  circuits: list[set[int]] = [{n} for n in range(n_points)]
  last_jb: tuple[int, int]
  for _, n1, n2 in arcs:
    already_connected = any(c for c in circuits if n1 in c and n2 in c)
    if already_connected:
      continue
    sel_circuits = [c for c in circuits if c.intersection({n1, n2})]
    new_circuit = set()
    for c in sel_circuits:
      circuits.remove(c)
      new_circuit = new_circuit.union(c)

    if len(new_circuit) == n_points:
      last_jb = (n1, n2)
      break

    circuits.append(new_circuit)

  print(mat[last_jb[0], 0] * mat[last_jb[1], 0])
