import self as self

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Convert string to list
        # Iterate thru list elements linierly
        if not s:
            return 0

        longest_len = 0
        start = 0  # Initialized to 0, it marks the start index of the current substring being checked.
        seen = {}  # Initialized as an empty dictionary, it stores the last seen index of each character in the string.

        # loop iterates over the indices of the input string
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                start = seen[s[i]] + 1

            seen[s[i]] = i
            longest_len = max(longest_len, i - start + 1)

        return longest_len


tests = []
test = {
    'input': "abcabcbb",
    'output': 3
}

tests.append(test)
tests.append({
    'input': 'bbbbb',
    'output': 1
})

tests.append({
    'input': 'pwwkew',
    'output': 3
})

for test in tests:
    result = Solution.lengthOfLongestSubstring(self, test['input'])
    output = test['output']
    if result == output:
        print("PASS")
    else:
        print("FAILED")