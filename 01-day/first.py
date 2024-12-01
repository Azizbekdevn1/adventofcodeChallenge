with open('input', 'r') as file:
    lines = file.readlines()  # Har bir qatorni o'qiydi

list1 = []
list2 = []

for line in lines:
    values = line.strip().split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))


def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total_distance = 0
    for num in left_list:
        total_distance += num*right_list.count(num)

    return total_distance
print(calculate_total_distance(list2, list1))
