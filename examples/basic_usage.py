from n_queens.backtracking import NQueensSolver
from n_queens.visualization import print_ascii_board, visualize_with_pygame
import time

def main():
    n = 8  # Change this to try different board sizes
    
    print(f"Solving {n}-Queens problem...")
    start_time = time.time()
    
    solver = NQueensSolver(n)
    solutions = solver.solve()
    
    end_time = time.time()
    print(f"Found {solver.get_solution_count()} solutions in {end_time - start_time:.4f} seconds")
    
    if solutions:
        print("\nFirst solution:")
        print_ascii_board(solutions[0])
        
        # Uncomment to visualize with Pygame
        # visualize_with_pygame(solutions[0])
    
if __name__ == "__main__":
    main()