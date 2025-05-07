import pytest
from n_queens.backtracking import NQueensSolver

@pytest.mark.parametrize("n,expected_count", [
    (1, 1),
    (2, 0),
    (3, 0),
    (4, 2),
    (5, 10),
    (6, 4),
    (7, 40),
    (8, 92),
])
def test_solution_counts(n, expected_count):
    """Test that the solver finds the correct number of solutions."""
    solver = NQueensSolver(n)
    solutions = solver.solve()
    assert solver.get_solution_count() == expected_count

def test_solution_validity():
    """Test that all returned solutions are valid."""
    n = 5
    solver = NQueensSolver(n)
    solutions = solver.solve()
    
    for solution in solutions:
        # Check each solution is valid
        queens = []
        for row in range(n):
            col = solution[row].index('Q')
            queens.append((row, col))
        
        # Check no two queens share same column or diagonal
        for i in range(len(queens)):
            for j in range(i + 1, len(queens)):
                row1, col1 = queens[i]
                row2, col2 = queens[j]
                
                # Same column (rows are already unique)
                assert col1 != col2, f"Queens in same column: {queens[i]}, {queens[j]}"
                
                # Same diagonal
                assert abs(row1 - row2) != abs(col1 - col2), \
                    f"Queens on same diagonal: {queens[i]}, {queens[j]}"