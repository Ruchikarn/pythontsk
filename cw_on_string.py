entered_string = input('Enter a paragraph\n')

lower_entered_string = entered_string.lower()

vowel_count = 0

for ch in lower_entered_string:
    # if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    if ch in 'aeiou':
        vowel_count += 1

print('Vowel count is', vowel_count)

print('length of string is', len(entered_string))
