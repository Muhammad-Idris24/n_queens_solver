import numpy as np
from typing import List, Optional

class NQueensSolver:
    """Solve the N-Queens problem using backtracking."""
    
    def __init__(self, n: int):
        """Initialize the solver with board size n x n."""
        self.n = n
        self.solutions = []
        
    def solve(self) -> List[List[str]]:
        """Find all solutions to the N-Queens problem.
        
        Returns:
            List of solutions where each solution is represented
            as a list of strings (each string is a row of the board).
        """
        self.solutions = []
        board = [-1] * self.n  # Each index represents a row, value is column
        self._solve_util(board, 0)
        return self._format_solutions()
    
    def _solve_util(self, board: List[int], row: int) -> None:
        """Recursive utility function to solve N-Queens.
        
        Args:
            board: Current board state (1D array where index=row, value=column)
            row: Current row being processed
        """
        if row == self.n:
            self.solutions.append(board.copy())
            return
        
        for col in range(self.n):
            if self._is_safe(board, row, col):
                board[row] = col
                self._solve_util(board, row + 1)
                board[row] = -1  # Backtrack
    
    def _is_safe(self, board: List[int], row: int, col: int) -> bool:
        """Check if placing a queen at (row, col) is safe.
        
        Args:
            board: Current board state
            row: Row to check
            col: Column to check
            
        Returns:
            True if placement is safe, False otherwise
        """
        # Check column
        if col in board:
            return False
            
        # Check diagonals
        for r, c in enumerate(board[:row]):
            if c != -1 and abs(row - r) == abs(col - c):
                return False
                
        return True
    
    def _format_solutions(self) -> List[List[str]]:
        """Format solutions for display.
        
        Returns:
            List of solutions where each solution is a list of strings
            representing the board rows (Q for queen, . for empty)
        """
        formatted = []
        for solution in self.solutions:
            board = []
            for row in solution:
                board_row = ['.'] * self.n
                board_row[row] = 'Q'
                board.append(''.join(board_row))
            formatted.append(board)
        return formatted
    
    def get_solution_count(self) -> int:
        """Return the number of solutions found."""
        return len(self.solutions)