from random import choices

def choose_random_weighted(list: dict[str, int]):
  options = []
  weights = []

  for key, weight in list.items():
    options.append(key)
    weights.append(weight)

  return choices(options, weights=weights, k=1)[0]

def choose_best(list: dict[str, int]) -> str:
  best = ""
  record = 0
  
  for key, count in list.items():
    if count > record:
      best = key
      record = count
  
  return best

def score_pattern(reference: str, pattern: str) -> int:
  score = 0

  if pattern.lower() == reference.lower():
    score += 400 # arbitrarily good score, because it directly matches

  for index in range(min(len(reference), len(pattern))):
    ref_char = reference[index]
    pat_char = pattern[index]

    if ref_char == pat_char:
      score += 70
    elif ref_char.lower() == pat_char.lower():
      score += 40

  return score

def determine_best_pattern(references: dict[str, dict[str, int]], pattern: str) -> str:
  best = ""
  record = 0

  for reference in references:
    score = score_pattern(reference, pattern)

    if score > record:
      record = score
      best = reference
  
  return best

def extract_pattern(text: str, index: int, width: int) -> str:
  return text[index - width:index]

def analyze_text(text: str, pattern_width: int, association_width: int) -> dict[str, dict[str, int]]:
  output_patterns = {}
  
  for index in range(pattern_width, len(text) - association_width + 1):
    pattern = extract_pattern(text, index, pattern_width)
    association = text[index:index+association_width]

    if pattern not in output_patterns:
      output_patterns[pattern] = {}

    pattern_dict = output_patterns[pattern]
    
    if association not in pattern_dict:
      pattern_dict[association] = 1
    else:
      pattern_dict[association] += 1

  return output_patterns

def generate_pseudo_english(patterns: dict[str, dict[str, int]], seed: str, length: int, pattern_width: int) -> str:
  output = seed

  i = 0

  while i < length:
    current_pattern = extract_pattern(output, i + pattern_width, pattern_width)
    best_pattern = determine_best_pattern(patterns, current_pattern)

    print(current_pattern, best_pattern)

    associations = patterns[best_pattern]

    next_token = choose_random_weighted(associations)

    output += next_token
    i += len(next_token)
  
  return output.strip()

INPUT_DATA = ""
PATTERN_SIZE = 5


# with open("grant_data.txt", "r") as f:
#   test_data += f.read()

with open("whitman_leaves_of_grass.txt", "+r") as f:
  INPUT_DATA += f.read()

pattern_associations = analyze_text(INPUT_DATA, PATTERN_SIZE, 4)

print(f"input data length: {len(INPUT_DATA)}\n")
# print("pattern associations:\n", pattern_associations)

while True:
  seed = input("Seed: ")
  output_text = generate_pseudo_english(pattern_associations, seed, 500, PATTERN_SIZE)

  print(f"{'-' * 60}\n{output_text}\n{'-' * 60}")