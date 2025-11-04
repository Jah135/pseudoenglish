from typing import Callable

Occurrences = dict[str, int]
Patterns = dict[str, Occurrences]

ScoringMethod = Callable[[str, str], int]
ChoosingMethod = Callable[[Occurrences], str]