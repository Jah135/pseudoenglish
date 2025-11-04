def intput(prompt: str, default: int | None = None) -> int:
	while True:
		try:
			text = input(prompt)

			if text == "" and default != None:
				return default

			return int(text)
		except:
			print("Invalid integer.")