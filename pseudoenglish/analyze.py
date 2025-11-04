def analyze_text_patterns(input_text: str, pattern_size: int, token_size: int) -> dict[str, dict[str, int]]:
	output_patterns = {}

	for index in range(pattern_size, len(input_text) - token_size + 1):
		pattern = input_text[index - pattern_size : index]
		associated_text =input_text[index : index + token_size]

		if pattern not in output_patterns:
			output_patterns[pattern] = {}

		pattern_dict = output_patterns[pattern]

		if associated_text not in pattern_dict:
			pattern_dict[associated_text] = 1
		else:
			pattern_dict[associated_text] += 1
	
	return output_patterns
