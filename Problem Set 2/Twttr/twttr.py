vowel = ['a', 'e', 'i', 'o', 'u']
text = input()
text = text.lower()
for i in text:
    if i in vowel:
        text = text.replace(i, "")
print(text)