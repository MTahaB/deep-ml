def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == "row":
		return [sum(row) / len(row) for row in matrix]
	elif mode == "column":
		return [sum(column) / len(column) for column in zip(*matrix)]
	else:
		raise ValueError("Mode must be 'row' or 'column'.")