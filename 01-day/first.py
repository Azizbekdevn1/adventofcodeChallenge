
with open('input', 'r') as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    values = line.strip().split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))


# Second stars problem
def calculate_similarity(left_list, right_list):
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_list.count(num)
    return similarity_score


def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    # Calculate total distance
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
    return total_distance

print(calculate_total_distance(list2, list1))
# 2031679
print(calculate_similarity(list1, list2))
# 19678534
