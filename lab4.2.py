consonants = "bcdfghjklmnpqrstvwxz"
vowels = "aeiouy"
t = "lorem ipsum dolor sit amet,   consectetur  adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
text = t.lower()
consonant_count = 0
vowel_count = 0
for char in text:
    if char in consonants:
        consonant_count += 1
    elif char in vowels:
        vowel_count += 1
    else:
        current_run = 0

print("Number of consonants:", consonant_count)
print("Number of vowels:", vowel_count)

if consonant_count > vowel_count:
    print("Consonants are more frequent.")
elif vowel_count > consonant_count:
    print("Vowels are more frequent.")