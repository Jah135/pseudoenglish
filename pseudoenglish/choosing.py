from random import choices
from .types import Occurrences

def choose_random_weighted(occurrences: Occurrences) -> str:
	options = []
	weights = []

	for key, weight in occurrences.items():
		options.append(key)
		weights.append(weight)

	return choices(options, weights=weights, k=1)[0]
def choose_random(occurrences: Occurrences) -> str:
	options = []

	for key in occurrences:
		options.append(key)
	
	return choices(options, k=1)[0]

def choose_best(occurrences: Occurrences) -> str:
	best = ""
	record = 0
	
	for key, count in occurrences.items():
		if count > record:
			best = key
			record = count
	
	return best
def choose_worst(occurrences: Occurrences) -> str:
	worst = ""
	record = 1e9

	for key, count in occurrences.items():
		if count < record:
			worst = key
			record = count
	
	return worst