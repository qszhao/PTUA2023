# Exercise 2 - Count the number of 'a's in "banana"
print("The number of 'a's in \"banana\" is " + str("banana".count("a")))

# Exercise 3 - Write a one-line version of is_palindrome
def is_palindrome(word):
    return word == word[::-1]

print("\"banana\" is a palindrome? " + str(is_palindrome("banana")))
print("\"kayak\" is a palindrome? " + str(is_palindrome("kayak")))

# Incorrect. This will only check whether the first letter is lower case
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# Incorrect. This will always return True.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# Incorrect. This will return whether only the final letter is lower case.
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# Correct. This will check every letter and return if any of them are lower case.
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# Incorrect. This will only return True if ALL of the letters are lowercase.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# Exercise 5: Caesar cypher

def rotate_word(word, n):
    rotated_word = ""

    for ch in word:
        rotated_ch = ""
        offset = 'a' if ch.islower() else 'A'
        rotated_ch = chr((ord(ch) - ord(offset) + n) % 26 + ord(offset))
        rotated_word += rotated_ch

    return rotated_word

print("Rotate 'HelloWorld' by -19: " + rotate_word("HelloWorld", -19))


