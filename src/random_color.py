import random

def random_Color() -> str:
  rgb = random.sample(range(255), 3)
  return f"#{rgb[2]}{rgb[1]}{rgb[0]}"