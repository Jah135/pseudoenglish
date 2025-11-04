from .types import Patterns, ScoringMethod, ChoosingMethod
from .scoring import determine_closest_pattern, default_score_method
from .choosing import choose_random_weighted

def generate_text(patterns: Patterns, seed: str = "", readback_size: int = 5, output_len: int = 500, scoring_method: ScoringMethod = default_score_method, choosing_method: ChoosingMethod = choose_random_weighted) -> str:
	output = seed

	while len(output) < output_len:
		cursor = len(output)

		readback_pattern = output[max(cursor - readback_size, 0) : cursor]
		closest_pattern = determine_closest_pattern(readback_pattern, patterns, scoring_method=scoring_method)

		occurrences = patterns[closest_pattern]
		next_token = choosing_method(occurrences)

		output += next_token

	return output.strip()
