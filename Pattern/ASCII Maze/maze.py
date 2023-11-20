import numpy as np
import random
import svgwrite

def generate_maze(x, y):
    maze = np.ones((y, x), dtype=int)
    
    def create_maze(cx, cy):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            
            if 0 <= nx < x and 0 <= ny < y and maze[ny, nx] == 1:
                maze[cy + dy, cx + dx] = maze[ny, nx] = 0
                create_maze(nx, ny)
    
    create_maze(random.randint(0, x // 2) * 2, random.randint(0, y // 2) * 2)
    return maze

def generate_svg(maze, filename='maze.svg'):
    height, width = maze.shape
    
    cell_size = 10  # Adjust the size of each cell
    
    dwg = svgwrite.Drawing(filename, profile='full')
    dwg.add(dwg.rect((0, 0), (width * cell_size, height * cell_size), fill='white'))
    
    for y in range(height):
        for x in range(width):
            if maze[y, x] == 1:
                dwg.add(dwg.rect((x * cell_size, y * cell_size), (cell_size, cell_size), fill='black'))
    
    dwg.save()

# Example usage:
maze = generate_maze(11, 11)
generate_svg(maze)
print(maze)