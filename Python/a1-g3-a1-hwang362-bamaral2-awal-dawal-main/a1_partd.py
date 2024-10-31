#    Main Author(s): Bruno Amaral
#    Main Reviewer(s): Bruno Amaral

from a1_partc import Queue

def get_overflow_list(grid):
	rows = len(grid)
	cols = len(grid[0])
	overflow_list = []

	for r in range(rows):
		for c in range(cols):
			if (r == 0 or r == rows - 1) and (c == 0 or c == cols - 1):
				neighbours = 2
			elif r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
				neighbours = 3
			else:
				neighbours = 4

			if abs(grid[r][c]) >= neighbours: # abs is used to get the absolute value of the cell
				overflow_list.append((r, c))
	return overflow_list if overflow_list else None

def overflow(grid, a_queue):
	def is_overflowing(grid):
		overflow_list = get_overflow_list(grid)
		if not overflow_list:
			return False
		signs = set()
		for row in grid:
			for cell in row:
				if cell != 0:
					signs.add(cell > 0)
		return len(signs) > 1
    
	def create_new_grid(grid, overflow_list):
		rows = len(grid)
		cols = len(grid[0])
		new_grid = [row[:] for row in grid]

		for r, c in overflow_list:
			sign = 1 if grid[r][c] > 0 else -1
			new_grid[r][c] = 0  # Overflowing cell becomes empty
			if r > 0:
				new_grid[r-1][c] += sign
				new_grid[r-1][c] = sign * abs(new_grid[r-1][c])  # Ensure neighbor takes on the same sign
			if r < rows - 1:
				new_grid[r+1][c] += sign
				new_grid[r+1][c] = sign * abs(new_grid[r+1][c])  # Ensure neighbor takes on the same sign
			if c > 0:
				new_grid[r][c-1] += sign
				new_grid[r][c-1] = sign * abs(new_grid[r][c-1])  # Ensure neighbor takes on the same sign
			if c < cols - 1:
				new_grid[r][c+1] += sign
				new_grid[r][c+1] = sign * abs(new_grid[r][c+1])  # Ensure neighbor takes on the same sign
		return new_grid

	if not is_overflowing(grid):
		return 0
	
	overflow_list = get_overflow_list(grid)
	new_grid = create_new_grid(grid, overflow_list)
	a_queue.enqueue(new_grid)
	return 1 + overflow(new_grid, a_queue)