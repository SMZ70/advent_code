from pathlib import Path
import re

if __name__ == "__main__":
  print(
    sum(
      n
      for rng in map(
        lambda r: tuple(map(int, r.split("-"))),
        Path(__file__).parent.joinpath("input").read_text().split(","),
      )
      for n in range(rng[0], rng[1] + 1)
      if re.match(r"^(\d+)(\1){1,}$", str(n))
    )
  )
