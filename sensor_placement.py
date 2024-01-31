import random
import matplotlib.pyplot as plt
def check_coverage(M, L):
    M.sort()  # Sort the list for easier checking
    last_covered = 0  # Initialize the last covered point on the segment

    for m in M:
        # Check if the Schill-o-meter at position m fills in the gap
        if m - 7 > last_covered:
            return False
        last_covered = m + 7  # Update the last covered point

    # Check if the entire segment is covered
    return last_covered >= L
def is_valid_input(N, L):
    # Condition 1: |N| * 14 < L
    if len(N) * 14 <  (L-7):
        return False
    
    # Sort N for easier checking
    N.sort()
    
    # Condition 2: n_0 <= 7
    if N[0] > 7:
        return False
    
    # Condition 2 continued: For all n_i in N, n_i - n_{i-1} <= 14
    for i in range(1, len(N)):
        if N[i] - N[i-1] > 14:
            return False
    
    if N[i] < L-7:
        return False
    return True

def find_target_or_smaller(N, l, r, target):
    closest = -1  
    
    while l <= r:
        mid = (l + r) // 2
        if N[mid] == target:
            return mid
        elif N[mid] < target:
            closest = mid  
            l = mid + 1
        else:
            r = mid - 1
    return closest

# Randomly generate L (length of the line segment)
length  = 200
min_num = 25

# 14 * n + 7 >= length -7 / 14 
L = random.randint(length-0, length)
n = random.randint(min_num, min_num)


# Generate N (set of n possible locations)
N = random.sample(range(0, L+1), n)
N.sort()


while not (is_valid_input(N,L)):         

    L = random.randint(length-0, length)
    n = random.randint(min_num, min_num)
    
    N = random.sample(range(0, L+1), n)
    N.sort()


M= []
Right_edge = 0
potential = 0
i = 0 
import numpy as np
N.extend(np.arange(0,200,14))
N.sort()
# N = list(np.arange(0,190,14))
# N.append(182)
N.sort()

while Right_edge < L:
    boundary = Right_edge + 7
    last_added = potential
    while  potential < len(N) and N[potential] <= boundary:
        potential+=1
    if potential-1 == last_added:
        break
    M.append(N[potential-1])
    Right_edge = M[-1] + 7
    i+=1

print(N)
print(len(M))

plt.plot([0, L], [0, 0], label='Line Segment [0, L]', linewidth=4)
plt.scatter(N, [0]*len(N), color='red', zorder=5, label='Possible Locations')

# Plotting the Schill-o-meter locations from M and their intervals
for m ,i in enumerate(M):
    plt.scatter(i, 0.5, color='green', zorder=6)
    plt.plot([i - 7, i + 7], [0.5, 0.5], color='purple', linewidth=2)  # Interval 7 units to the left and right

for m ,i in enumerate(M):
    plt.scatter(i, m+1, color='green', zorder=6)
    plt.plot([i - 7, i + 7], [m+1, m+1], color='purple', linewidth=2)  # Interval 7 units to the left and right
print(M)


if check_coverage(M, L):
    print(f"The segment [0, {L}] is fully covered.")
else:
    print(f"The segment [0, {L}] is not fully covered.")

plt.legend(['Line Segment [0, L]', 'Schill-o-meter Coverage', 'Possible Locations', 'Schill-o-meter Locations'])
plt.show()
