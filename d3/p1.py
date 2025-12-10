from pathlib import Path

input_lines = list(
  line
  for line in Path(__file__).parent.joinpath("input").read_text().splitlines()
  if line
)

if __name__ == "__main__":
  print(
    sum(
      max(10 * int(d) + max(map(int, line[i + 1 :])) for i, d in enumerate(line[:-1]))
      for line in input_lines
    )
  )
