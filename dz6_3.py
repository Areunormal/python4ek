key = bytes(str(input("Введите ключ для xor-шифрования:")), encoding = "utf-8")
text = open("xortext.txt")
text1 = bytes(text.readline(), encoding ="utf-8")
encrypted_text=""
for i in range(len(text1)):
    simvol = text1[i]
    kluch = key[i%len(key)]
    encrypted_text+=chr(simvol^kluch)
print("Ваш зашифрованый текст-", encrypted_text)
text1 = bytes(encrypted_text, encoding ="utf-8")
decrypted_text=""
for i in range(len(text1)):
    simvol = text1[i]
    kluch = key[i%len(key)]
    decrypted_text+=chr(simvol^kluch)
print("Ваш расшифрованный текст-",decrypted_text)

