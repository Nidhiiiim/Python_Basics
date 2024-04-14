import io

# Problem Stated Clearly
# There is set of cards arranged in decreasing order upside down, Alice wants bob to pick a particular card with minimum attempts.

# Inputs
# Cards
# Target Card

# Name function with sensible name.
# Descriptive Variable Name

# Outputs
#  Position of Target

# Solution
# 1. We can consider deck of cards as list
# 2. Divide total number of cards to get midpoint
# 3. Check if value of mid >= or <= mid number
# 4. if >= mid then keep right and remove left part of list
# 5. If <= then keep left and remove right.
# 6. Repeat Step 2 - 5 again.

# Test Cases represented as dictionaries

Cards = []
Target_Number = 10
Output = 3

test = {
    # All function arguments
    'input': {
        'Cards': [14, 11, 10, 9, 8, 7, 6, 2, 0],
        'Target_Number': 10
    },
    'output': 2
}


# 1) Brute Force Solution
def locate_Card(Cards, Target_Number):
    position = 0
    while True:
        # Check if element is at this position
        if Cards[position] == Target_Number:
            return position
        position += 1

        if position == len(Cards):
            return -1


# List all possible test cases
# 1) The target is somewhere in middle of card
# 2) Target is first element
# 3) Target is last element
# 4) There is only one card
# 5) Target number is not in the card Alice is bluffing
# 6) List is empty
# 7) The number is more than once
tests = []

tests.append(test)
tests.append({
    # All function arguments
    'input': {
        'Cards': [14, 11, 10, 9, 8, 7, 6, 2, 0],
        'Target_Number': 10
    },
    'output': 2
})

tests.append({
    # All function arguments
    'input': {
        'Cards': [14, 11, 10, 9, 8, 7, 6, 2, 0],
        'Target_Number': 14
    },
    'output': 0
})

tests.append({
    # All function arguments
    'input': {
        'Cards': [14, 11, 10, 9, 8, 7, 6, 2, 0],
        'Target_Number': 0
    },
    'output': 8
})

tests.append({
    # All function arguments
    'input': {
        'Cards': [10],
        'Target_Number': 10
    },
    'output': 0
})

tests.append({
    # All function arguments
    'input': {
        'Cards': [14, 12, 11, 9, 8, 7, 6, 2, 0],
        'Target_Number': 10
    },
    'output': -1
})

tests.append({
    # All function arguments
    'input': {
        'Cards': [14, 11, 10, 9, 8, 7, 6, 2, 0],
        'Target_Number': 10
    },
    'output': 2
})

tests.append({
    # All function arguments
    'input': {
        'Cards': [],
        'Target_Number': 3
    },
    'output': -1
})

tests.append({
    # All function arguments
    'input': {
        'Cards': [14, 11, 10, 10, 8, 7, 6, 2, 0],
        'Target_Number': 10
    },
    'output': 2
})
print(tests)

result = locate_Card(test['input']['Cards'], test['input']['Target_Number'])
output = test['output']

# CONFIRMING THE ANSWER
print(result == output)


# Brute force method complexity O(n)
# We will perform Binary Search Method

def binary_card_locate(Cards, Target_Number):
    lo, hi = 0, len(Cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2  # Get Midpoint
        mid_num = Cards[mid]
        print("lo: ", lo, "hi: ", hi, "mid: ", mid)
        if mid_num == Target_Number:
            return mid
        elif mid_num < Target_Number:
            hi = mid - 1
        elif mid_num > Target_Number:
            lo = mid + 1
    return -1


binary_result = binary_card_locate(test['input']['Cards'], test['input']['Target_Number'])
binary_output = test['output']

# CONFIRMING THE ANSWER
print(binary_result == binary_output)
