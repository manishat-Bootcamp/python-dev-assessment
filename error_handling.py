def calculate_average(data):
    if len(data) == 0:
        return "Cannot calculate average of an empty list"

    return sum(data) / len(data)

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")