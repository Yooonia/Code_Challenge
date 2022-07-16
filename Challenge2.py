# Challenge 2:
# Write a solution to find the character that has the highest number of occurrences within a certain string, ignoring
# case. If there is more than one character with equal highest occurrences, return the character that appeared first
# within the string.
# For example:
#  Input: "Character"
#  Output: c

def count_char(given_string):
    given_string = given_string.lower()
    res = max(given_string, key=given_string.count)
    return res


if __name__ == '__main__':
    input_str = input('Please enter a string: ')
    max_char = count_char(input_str)
    print(max_char)


