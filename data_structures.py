print("data structures exercise started")
def filter_and_sort_evens(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:

           even_numbers.append(number)

    return sorted(even_numbers)

numbers = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
print (filter_and_sort_evens(numbers))

def count_character_frequency(text):
    frequency = {}

    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    return frequency
text = "This my task for Baisic Data Structures & Algorithms"
print(count_character_frequency(text))