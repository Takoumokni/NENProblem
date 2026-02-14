def solve_nen_grid(grid):
    if not grid or not grid[0]:
        return False
    
    rows = len(grid)
    cols = len(grid[0])

    dp = [[False for _ in range(cols)] for _ in range(rows)]
    
    # La cellule de départ est toujours atteinte
    dp[0][0] = True
    
    for r in range(rows):
        for c in range(cols):
            # Si on n'est pas au départ et qu'on peut atteindre cette cellule
            if r == 0 and c == 0:
                continue
                
            can_reach = False
            
            # Tentative de venir du haut
            if r > 0 and dp[r-1][c]:
                if grid[r][c] > grid[r-1][c]:
                    can_reach = True
            
            # Tentative de venir de la gauche
            if c > 0 and dp[r][c-1]:
                if grid[r][c] > grid[r][c-1]:
                    can_reach = True
            
            dp[r][c] = can_reach

    return dp[rows-1][cols-1]

# --- TEST DU SYSTÈME ---
grid_valide = [
    [1,  5,  2],
    [3,  10, 15],
    [4,  8,  20]
]
grid_invalide = [
    [10, 5, 2],
    [8,  4, 1],
    [7,  3, 0]
]

print(f"Chemin valide existe : {solve_nen_grid(grid_valide)}")   
print(f"Chemin invalide existe : {solve_nen_grid(grid_invalide)}") 