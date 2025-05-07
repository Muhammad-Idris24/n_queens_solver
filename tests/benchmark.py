from n_queens.backtracking import NQueensSolver
import time

def benchmark():
    print("N\tSolutions\tTime (s)")
    print("-" * 30)
    
    for n in range(1, 13):  # Beyond 12 becomes very slow with backtracking
        start_time = time.time()
        solver = NQueensSolver(n)
        solutions = solver.solve()
        elapsed = time.time() - start_time
        
        print(f"{n}\t{solver.get_solution_count():<9}\t{elapsed:.4f}")

if __name__ == "__main__":
    benchmark()