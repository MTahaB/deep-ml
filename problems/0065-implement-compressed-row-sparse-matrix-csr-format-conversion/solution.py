import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	matrix = np.asarray(dense_matrix)

	rows, columns = np.nonzero(matrix)
	values = matrix[rows, columns]

	counts = np.count_nonzero(matrix, axis=1)
	row_pointer = np.concatenate(([0], np.cumsum(counts)))

	return values.tolist(), columns.tolist(), row_pointer.tolist()