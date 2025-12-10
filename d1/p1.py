from pathlib import Path

if __name__ == "__main__":
  rotations = Path(__file__).parent.joinpath("input").read_text().splitlines()
  dial = 50

  password = 0
  rotations: list[str]
  for r in rotations:
    dial = (dial + (1 if r.startswith("R") else -1) * int(r[1:])) % 100
    if dial == 0:
      password += 1

  print(password)
