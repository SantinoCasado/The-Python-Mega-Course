"""
Te objetive is to creat a sumUp file that uses all the things previously learned.
"""

def sentence_maker (phrase):
    interrogatives = ("how", "what", "why", "where", "when", "who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return f"{capitalized}?"
    else:
        return f"{capitalized}."

list_of_phrases = []
flag = True

while flag:
    user_input = input("Enter a phrase: ")

    while not user_input.replace(" ", "").isalpha():
        print("Please enter a valid phrase (only letters and spaces).")
        user_input = input("Enter a phrase: ")
    
    list_of_phrases.append(sentence_maker(user_input))

    respond = input("Do you want to continue? (yes/no): ").strip().lower()
    while respond != 'yes' and respond != 'no':
        print("Please answer with 'yes' or 'no'.")
        respond = input("Do you want to continue? (yes/no): ").strip().lower()
    if respond == 'no':
        flag = False

print(" | ".join(list_of_phrases))