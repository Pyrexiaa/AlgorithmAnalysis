letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == '':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
    return plaintext

ciphertext = "Ymfy ujwxts nx htrnsl ktw rj! Nk dtz knsi ymnx styj, qttp fwtzsi rd uwtujwyd. Mnsy: N anxnyji ymj fwjf bnym rd ywtqqjd kwtr ymj lfwijs xmji."
key = 5
decrypted_message = decrypt(ciphertext, key)
print(decrypted_message)
