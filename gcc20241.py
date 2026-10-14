# Input list
input_list = [1, 2, 2, 3, 5, 4, 6, 7, 9, 8, 10, 15, 11, 11, 12]

# initialize the two things we're finding
position = 1
max_difference = 0

# go through every item in input_list.
# normally I'd use enumerate, but we need
# to compare two items at a time, go going
#through it by index is the best thing to do here.
for index in range(len(input_list)):

    # ignore the first item.
    if index == 0:
        continue

    # find the terrain difference, record it if it's a maximum.
    terrain_difference = input_list[index] - input_list[index - 1]
    if terrain_difference > max_difference:
        max_difference = terrain_difference
        position = index

# print our solution
print(max_difference, position)
