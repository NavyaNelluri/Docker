import pytest
from SparseMatrix import SparseMatrix
#@pytest.fixture


# Test set and get methods
def test_set_get():
    matrix = SparseMatrix(rows=2, cols=2)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    assert matrix.get(0, 0) == 1
    assert matrix.get(1, 1) == 2
    assert matrix.get(0, 1) == 0

# Test recommend method
def test_recommend():
    matrix = SparseMatrix(rows=2, cols=2)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    vector = [1, 0]
    recommendations = matrix.recommend(vector)
    assert recommendations == [1, 0] 

# Test add_movie method
def test_add_movie():
    matrix1 = SparseMatrix(rows=2, cols=2)
    matrix1.set(0, 0, 1)
    matrix1.set(1, 1, 2)

    matrix2 = SparseMatrix(rows=2, cols=2)
    matrix2.set(0, 1, 3)

    result_matrix = matrix1.add_movie(matrix2)
    print(result_matrix)
    # Check if the resulting matrix has the expected values
    assert result_matrix.get(0, 0) == 1
    assert result_matrix.get(0, 1) == 3
    assert result_matrix.get(1, 1) == 2

# Test to_dense method
def test_to_dense():
    matrix = SparseMatrix(rows=2, cols=2)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[1, 0], [0, 2]]

#Testing exception case of adding '0' to sparse matrix   
def test_set_invalidvalue():
    matrix = SparseMatrix(rows=2, cols=2)
    with pytest.raises(ValueError) as context:
        matrix.set(0, 0, 0)

    # Check if the correct error message is raised
    assert str(context.value) == "Invalid value: Dictionary cannot store value '0' "

#Testing exception case by giving invalid column length to sparse matrix   
def test_set_invalidRowColumn():
    matrix = SparseMatrix(rows=2, cols=2)
    
    with pytest.raises(ValueError) as context:
        matrix.set(0, -1, 0)
    
    # Check if the correct error message is raised
    assert str(context.value) == "Invalid row or column index"
if __name__ == "__main__":
    pytest.main()
