import pygame
import sys
from typing import List

def print_ascii_board(solution: List[str]) -> None:
    """Print a solution to the console in ASCII format.
    
    Args:
        solution: List of strings representing the board
    """
    border = '+' + ('-' * (len(solution[0]) * 2 - 1)) + '+'
    print(border)
    for row in solution:
        print('|' + ' '.join(row) + '|')
    print(border)
    print()

def visualize_with_pygame(solution: List[str], delay: int = 1000) -> None:
    """Visualize a solution using Pygame.
    
    Args:
        solution: List of strings representing the board
        delay: Time (ms) to display each frame
    """
    n = len(solution)
    cell_size = 60
    width, height = n * cell_size, n * cell_size
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(f"{n}-Queens Solution")
    
    colors = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'queen': (220, 20, 60)  # Crimson red
    }
    
    # Draw the board
    screen.fill(colors['white'])
    for row in range(n):
        for col in range(n):
            color = colors['white'] if (row + col) % 2 == 0 else colors['black']
            pygame.draw.rect(
                screen, color,
                (col * cell_size, row * cell_size, cell_size, cell_size)
            )
            
            if solution[row][col] == 'Q':
                center = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
                radius = cell_size // 3
                pygame.draw.circle(screen, colors['queen'], center, radius)
    
    pygame.display.flip()
    
    # Keep the window open until closed by user
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.delay(delay)
        running = False
    
    pygame.quit()