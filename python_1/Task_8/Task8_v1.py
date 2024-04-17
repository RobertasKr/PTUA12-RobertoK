"""
Yra duotas listas, jame yra žodžiai. Parašyti algortimą, kuris atrinktų patį ilgiausią besikartojančių žodžių fragmenta. Pvz, jei listas:

[‚namas‘, ‚namelis‘, ‚nameliukas‘] -> „nam“

[morkytė, molas, morka] - > mo

[namas, balkonas, mama] - > „“ tuscias stringas.
"""

list_words = ["namas", "namelis", "nameliukas"]
duplicates = ""
check_letters = ""
print(list_words)
for word in list_words:
    # print(word)
    for letter in word:
        # print(letter)
        check_letters += letter
        if word.startswith(check_letters):
            print(duplicates, "-------")
            duplicates += letter
print(duplicates, " DUPLIKATAI ")
