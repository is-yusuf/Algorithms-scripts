def compute_opt(G):
    n = len(G) - 1  # Assuming G is a square matrix and index starts from 1
    OPT = [[0] * (n+1) for _ in range(n+1)]

    # Initial setup based on given pseudo-code
    OPT[1][1] = G[1][1]
    for i in range(2, n + 1):
        OPT[i][1] = OPT[i-1][1] + G[i][1]
        OPT[1][i] = OPT[1][i-1] + G[1][i]

    # Main dynamic programming loop
    for row in range(2, n + 1):
        for column in range(2, n + 1):
            left = OPT[row][column-1]
            top = OPT[row-1][column]
            topleft = OPT[row-1][column-1]
            OPT[row][column] = min(top, left, topleft) + G[row][column]

    return OPT

def trace_back(OPT):
    n = len(OPT) - 1  # Assuming OPT is a square matrix and index starts from 1
    PATH = []
    r, c = n, n

    # Traceback loop
    while r != 1 or c != 1:
        PATH.insert(0, (r, c))
        left = OPT[r][c-1] if c > 1 else float('inf')
        top = OPT[r-1][c] if r > 1 else float('inf')
        topleft = OPT[r-1][c-1] if r > 1 and c > 1 else float('inf')

        if left <= top and left <= topleft:
            c -= 1
        elif top < left and top <= topleft:
            r -= 1
        else:
            r -= 1
            c -= 1

    PATH.insert(0, (1, 1))  # Prepending the start position
    return PATH

G = [
    [0, 0, 0, 0, 0, 0],  # Adding a row of zeros for padding to match 1-based indexing
    [0, 5, 3, 2, 5, 4],  # Grid row 1
    [0, 1, 2, 5, 4, 3],  # Grid row 2
    [0, 7, 2, 5, 6, 4],  # Grid row 3
    [0, 6, 1, 1, 6, 3],  # Grid row 4
    [0, 5, 2, 7, 2, 3]   # Grid row 5
]

OPT = compute_opt(G)
for row in OPT:
    print("".join(str(row)))
print("")
PATH = trace_back(OPT)
print(PATH)
