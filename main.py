from random import choices, randint

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
	score = randint(-5, 0)

	max_length = min(len(reference), len(pattern))
	min_pattern = pattern[-max_length:]
	min_reference = reference[-max_length:]
	
	if min_pattern == min_reference:
		score += 400

	for index in range(max_length):
		ref_char = min_reference[index]
		pattern_char = min_pattern[index]
		
		alpha = (index / max_length)

		if ref_char == pattern_char:
			score += 100 * alpha
		elif ref_char.lower() == pattern_char.lower():
			score += 40 * alpha

	return score
def determine_closest_pattern(pattern_list: dict[str, dict[str, int]], pattern: str) -> str:
	best = pattern
	record = -1

	for reference in pattern_list:
		score = score_pattern(reference, pattern)

		# print(f"score: {score:-3} | ref: {reference!r} | pat: {pattern!r}")

		if score > record:
			record = score
			best = reference
	
	return best

def analyze_text(text: str, pattern_width: int, association_width: int) -> dict[str, dict[str, int]]:
	output_patterns = {}
	
	for index in range(pattern_width, len(text) - association_width + 1):
		pattern = text[index-pattern_width:index]
		associated_text = text[index:index+association_width]

		if pattern not in output_patterns:
			output_patterns[pattern] = {}

		pattern_dict = output_patterns[pattern]
		
		if associated_text not in pattern_dict:
			pattern_dict[associated_text] = 1
		else:
			pattern_dict[associated_text] += 1

	return output_patterns
def generate_pseudo_english(patterns: dict[str, dict[str, int]], seed: str, length: int, pattern_width: int) -> str:
	output = seed

	while len(output) < length:
		cursor = len(output)

		readback_pattern = output[max(cursor-pattern_width, 0):cursor]
		closest_pattern = determine_closest_pattern(patterns, readback_pattern)


		associations = patterns[closest_pattern]

		next_token = choose_random_weighted(associations)
		
		print(f"{cursor:3}:|R: {readback_pattern!r:9}|C: {closest_pattern!r:9}| -> {next_token!r:7} >+> {readback_pattern+next_token!r}")

		output += next_token
	
	return output.strip()

INPUT_DATA = ""
PATTERN_SIZE = 6
READBACK_SIZE = 6
TOKEN_SIZE = 3

# with open("grant_data.txt", "r") as f:
#   test_data += f.read()

with open("whitman_data.txt", "+r") as f:
	INPUT_DATA += f.read()

pattern_associations = analyze_text(INPUT_DATA, PATTERN_SIZE, TOKEN_SIZE)

print(f"Input Data Size: {len(INPUT_DATA)}\nAssociation Count: {len(pattern_associations)}\n\nPattern Size: {PATTERN_SIZE}\nReadback Size: {READBACK_SIZE}\nToken Size: {TOKEN_SIZE}\n")
# print("pattern associations:\n", pattern_associations)

while True:
	seed = input("Input seed: ")

	output_text = generate_pseudo_english(pattern_associations, seed, 500, READBACK_SIZE)
	print(f"{'-' * 50}\n{output_text}\n{'-' * 50}")