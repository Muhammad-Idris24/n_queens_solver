import random
import numpy as np
from typing import List, Tuple
from tqdm import tqdm  # pip install tqdm

class GeneticNQueensSolver:
    """Solve N-Queens using a genetic algorithm."""
    
    def __init__(self, n: int, population_size: int = 100):
        """Initialize the genetic solver.
        
        Args:
            n: Board size
            population_size: Number of individuals in population
        """
        self.n = n
        self.population_size = population_size
        
    def solve(self, max_generations: int = 1000) -> List[int]:
        """Run the genetic algorithm to find a solution.
        
        Args:
            max_generations: Maximum generations to run
            
        Returns:
            Solution as a list of column indices (one per row)
        """
        population = self._initialize_population()
        
        for generation in tqdm(range(max_generations)):
            # Evaluate fitness
            fitness = [self._fitness(ind) for ind in population]
            
            # Check for solution
            max_fit = max(fitness)
            if max_fit == self.n * (self.n - 1) // 2:
                idx = fitness.index(max_fit)
                return population[idx]
                
            # Selection
            parents = self._select_parents(population, fitness)
            
            # Crossover
            offspring = []
            for i in range(0, len(parents), 2):
                if i + 1 < len(parents):
                    child1, child2 = self._crossover(parents[i], parents[i+1])
                    offspring.extend([child1, child2])
            
            # Mutation
            population = [self._mutate(ind) for ind in offspring]
            
        return None  # No solution found
    
    def _initialize_population(self) -> List[List[int]]:
        """Create initial population."""
        return [
            random.sample(range(self.n), self.n)
            for _ in range(self.population_size)
        ]
    
    def _fitness(self, individual: List[int]) -> int:
        """Calculate fitness (higher is better)."""
        clashes = 0
        for i in range(len(individual)):
            for j in range(i + 1, len(individual)):
                if abs(i - j) == abs(individual[i] - individual[j]):
                    clashes += 1
        return (self.n * (self.n - 1) // 2) - clashes
    
    def _select_parents(self, population: List[List[int]], 
                       fitness: List[int]) -> List[List[int]]:
        """Select parents using tournament selection."""
        parents = []
        for _ in range(len(population)):
            # Tournament size of 3
            candidates = random.sample(list(zip(population, fitness)), 3)
            winner = max(candidates, key=lambda x: x[1])[0]
            parents.append(winner)
        return parents
    
    def _crossover(self, parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        """Ordered crossover for permutations."""
        size = len(parent1)
        a, b = random.sample(range(size), 2)
        start, end = min(a, b), max(a, b)
        
        def _create_child(p1, p2):
            child = [-1] * size
            child[start:end] = p1[start:end]
            
            remaining = [item for item in p2 if item not in child]
            ptr = 0
            for i in range(size):
                if child[i] == -1:
                    child[i] = remaining[ptr]
                    ptr += 1
            return child
            
        return _create_child(parent1, parent2), _create_child(parent2, parent1)
    
    def _mutate(self, individual: List[int]) -> List[int]:
        """Swap mutation."""
        if random.random() < 0.1:  # 10% mutation rate
            a, b = random.sample(range(len(individual)), 2)
            individual[a], individual[b] = individual[b], individual[a]
        return individual