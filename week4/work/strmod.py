# Part 1: strmod
#
# Complete the function `strmod` (string modify) which takes three parameters:

# - `mod` - modification to make:
#     - '+' - combines the two strings via concatenation
#     - '-' - removes any occurrences of `str2` from `str1`
#     - '@' - combines the two strings, and then sorts their letters alphabetically
# - `str1` - first string parameter
# - `str2` - second string parameter

# Examples:
# >>> from strmod import strmod
# >>> strmod("+", "abc", "def")     # concatenation
# "abcdef"
# >>> strmod("-", "banana", "na")   # remove/replace all "na"
# "ba"
# >>> strmod("-", "banana", "x")    # nothing to remove
# "banana"
# >>> strmod("@", "cat", "dog")     # combined then sorted
# "acdgot"

# ```
# Do this part **without helper functions**; use `lambda` instead.

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a.replace(b, ""),
    "@": lambda a, b: "".join(sorted(a + b))
}
def strmod(op, str1, str2):
    return OPERATIONS[op](str1, str2)
    
