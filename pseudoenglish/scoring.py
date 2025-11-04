from .types import Patterns, ScoringMethod

def default_score_method(reference: str, pattern: str) -> int:
	score = 0

	max_length = min(len(reference), len(pattern))
	min_pattern = pattern[-max_length:]
	min_reference = reference[-max_length:]

	if min_pattern == min_reference:
		score += 400

	for index in range(max_length):
		ref_char = min_reference[index]
		pattern_char = min_pattern[index]

		if ref_char == pattern_char:
			score += 100
		elif ref_char.lower() == pattern_char.lower():
			score += 40

	return score

def determine_closest_pattern(pattern: str, other_patterns: Patterns, scoring_method: ScoringMethod = default_score_method) -> str:
	best = ""
	record = -1

	for reference in other_patterns:
		score = scoring_method(reference, pattern)

		if score > record:
			record = score
			best = reference
	
	return best