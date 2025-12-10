from pathlib import Path

input_lines = list(
  line
  for line in Path(__file__).parent.joinpath("input").read_text().splitlines()
  if line
)


def max_subsequence(s: str, k: int = 12) -> int:
  n = len(s)

  result = []
  start = 0
  for k_index in range(k):
    remaining = k - k_index - 1

    end = n - remaining

    best_pos = start
    for i in range(start, end):
      if s[i] > s[best_pos]:
        best_pos = i
        if s[i] == "9":
          break
    result.append(s[best_pos])

    start = best_pos + 1

  return int("".join(result))


if __name__ == "__main__":
  password = 0
  for line in input_lines:
    password += max_subsequence(line, 12)
  print(password)
