#!/usr/bin/python3
import unittest

"""Module for matrix_divided method."""

def matrix_divided(matrix, div):

        """Divide all elements of matrix by div

    Args:
        matrix: list of lists contain int or float
        div: number to divide matrix by

    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.

    Returns:
        list: List of lists representing divided matrix.
    """

    if not isinstance(matrix, list) or  (len(matrix) == 0):
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
        
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError ("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError ("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    return [[(round(x / div, 2)) for x in row] for row in matrix]




class testing_fn(unittest.TestCase):
    def test_notempty(self):
        self.assertRaises(TypeError, matrix_divided, None, 2)

    def test_notinteger(self):
        self.assertRaises(TypeError, matrix_divided, (1,2,3,4), 2)

    def test_rowLength(self):
        self.assertRaises(TypeError, matrix_divided, [[1,2,3], [1,2,3,4]], 2)
    
    def test_div(self):
        self.assertRaises(TypeError, matrix_divided, [[1,2,3,4],[1,2,3,5]], 'a')

    def test_divZero(self):
        self.assertRaises(ZeroDivisionError, matrix_divided, [[1,2,3,4],[1,2,3,5]], 0)

if __name__ == "__main__":
    unittest.main()
