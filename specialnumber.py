import random

# Generate an array of random integers, let's say of length 10

def find_super_special(nums):
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    left_majority = find_super_special(nums[:mid])
    right_majority = find_super_special(nums[mid:])

    if left_majority == right_majority:
        return left_majority

    left_count = nums.count(left_majority)
    right_count = nums.count(right_majority)

    if left_count > len(nums) // 2:
        return left_majority
    elif right_count > len(nums) // 2:
        return right_majority

    return None


while True:
    n = 20
    random_array = [random.randint(1, 100) for _ in range(n)]

    # Add n/2 + 1 random integers to the existing array
    additional_elements = [random.randint(1, 1) for _ in range(n+1)]
    random_array.extend(additional_elements)

    # Shuffle the array
    random.shuffle(random_array)
    if not find_super_special(random_array) == 1:
        break
    # if find_super_special(random_array)[1] >= n//2 :
    #    bre 
print(random_array)
# random_array = [1, 73, 1, 1, 1, 27, 11, 74, 34, 7, 41, 1, 1, 51, 1, 1, 1, 16, 1, 1, 44, 1, 1, 47, 47]
# print(find_super_special(random_array))
# 
# print((random_array[len(random_array)//2:]))
# print(random_array)
# print(find_super_special(random_array))
# print(random_array[len(random_array)//2:].count(1))
# print(random_array.count(1))
