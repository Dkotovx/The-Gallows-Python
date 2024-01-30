gallows = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

max_wrong = len(gallows) - 1
word = "Питон" 
so_far = "_" * len(word)
wrong = 0
used = []

while wrong < max_wrong and so_far != word:
    print(gallows[wrong])
    print("\nВы использовли эти буквы:\n", used)
    print("\nВаше слово сейчас выглядит так:\n", so_far)

    letter = input("\n\nВведите свое предположение: ")

    while letter in used:
        print("Эй! Эта буква уже была использована", letter)
        letter = input("Введите свое предположение: ")

    used.append(letter)

    if letter in word:
        print("\nУра!", letter, "есть в слове!")
        new = ""
        for i in range(len(word)):
            if letter == word[i]:
                new += letter
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nИзвините, буквы \"" + letter + "\" нет в слове.")
        wrong += 1

if wrong == max_wrong:
    print(gallows[wrong])
    print("\nТебя повесили!")
else:
    print("\nВы угадали слово!")

print("\nЗагаданное слово было \"" + word + '\"')