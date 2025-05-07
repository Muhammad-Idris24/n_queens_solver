from n_queens.backtracking import NQueensSolver
from n_queens.genetic import GeneticNQueensSolver
import time
from typing import List

def compare(n_values: List[int], num_trials: int = 5):
    print("Algorithm\tN\tTime (s)\tSuccess")
    print("-" * 50)
    
    for n in n_values:
        # Backtracking
        start = time.time()
        solver = NQueensSolver(n)
        solutions = solver.solve()
        bt_time = time.time() - start
        print(f"Backtracking\t{n}\t{bt_time:.4f}\t{len(solutions) > 0}")
        
        # Genetic
        for trial in range(num_trials):
            start = time.time()
            solver = GeneticNQueensSolver(n, population_size=100)
            solution = solver.solve(max_generations=1000)
            ga_time = time.time() - start
            success = solution is not None
            print(f"Genetic\t{n}\t{ga_time:.4f}\t{success}")

if __name__ == "__main__":
    compare([4, 8, 10, 12])