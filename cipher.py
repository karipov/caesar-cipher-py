# CONSTANTS
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# INPUT VALUES
user_sentence = input("Please enter your sentence: ")
while True:
    try:
        user_key = int(input("Please enter a key (0-26): "))
        break
    except ValueError:
        print("Please input a number!")

# FUNCTION
def encryptor(sentence, key):
    list_sentence = list(sentence)
    generated_sentence = [] # so we can later append the letters
    for character in list_sentence:
        if character.isupper() == True: # different for capitals
            position = capital_alphabet.index(character)
            new_position = (position + key) % 26
            generated_sentence.append(capital_alphabet[new_position]) # adds the letters one by one
        elif character.islower() == True:
            position = alphabet.index(character)
            new_position = (position + key) % 26
            generated_sentence.append(alphabet[new_position])
        else: # if the value is a number, just append the number
            generated_sentence.append(character)

    return ''.join(generated_sentence)


new_sentence = encryptor(user_sentence, user_key)

print("Your encrypted sentence:", new_sentence)
