from math import inf
import sys

def get_opt(cost, k):
    n = len(cost)
    # k+1 length so that we have k = 0 case
    OPT = [[inf] * (n) for _ in range(k + 1)]
    # fill out the n = 1 case
    for i in range(k + 1):
        OPT[i][0] = cost[0]
        OPT[i][1] = cost[1] if i != 0 else cost[1] + cost[0]
    
    # fill out the k = 0 case
    for i in range (2,n):
        OPT[0][i] = OPT[0][i-1] + cost[i]  

    # fill out the remaining of OPT
    for r in range(1, k + 1):
        for c in range(2, n):
            OPT[r][c] = min(OPT[r - 1][c - 2], OPT[r][c - 1]) + cost[c]
    return OPT

def get_path (OPT):
    path = []
    r = len(OPT)-1
    c = len(OPT[0])-1

    # is it more optimal to end at the last attraction of the one before it
    if OPT[r][c] <= OPT[r-1][c-1]:
        path.append(c)
    else:
        path.append(c-1)
        c = c-1
    
    # retrieve the path from end to start
    while r > 0 and c > 1:
        if OPT[r-1][c-2] <= OPT[r][c-1]:
            path.append(c-2)
            r = r-1
            c = c-2
        else:
            path.append(c-1)
            c = c-1
    return path[::-1]

def read_file_and_parse_data(filename):
    stops = []
    costs = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                stops.append(parts[0])
                costs.append(int(parts[1]))
    return stops, costs

def calculate_optimal_path(stops, costs, k):
    # Get the optimal stops we make
    path = get_path(get_opt(costs, k))
    solution_string = ""
    solution_length = sum(costs)
    # We found the stops with minimum cost, so we invert it to get the skips we need to take

    for i in range(len(stops)):
        if i not in path:
            solution_string += stops[i] + " "
            # subtract the skips from the total cost to get optimal cost
            solution_length -= costs[i]
    return solution_string.strip(), solution_length

def main():
    if len(sys.argv) != 3:
        print("Usage: opt_path.py <filename> <k>")
        sys.exit(1)

    filename = sys.argv[1]
    k = int(sys.argv[2])

    stops, costs = read_file_and_parse_data(filename)
    solution_string, solution_length = calculate_optimal_path(stops, costs, k)

    print(solution_string)
    print(solution_length)

if __name__ == "__main__":
    main()

