

letters_dict= {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j":10, 'k': 11, "l":12, "m": 13, "n": 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
n = input('do you wish to encrypt or decrypt(encrypt/decrypt): ')
if n == "encrypt":
    def alphabet_position (phrase) :
        list_01 = []
        for i in phrase:
            if i in letters_dict:
                num = str(letters_dict[i])
                list_01. append(num)
        numbers = " ".join(list_01)
        print (numbers)
    alphabet_position(input("please type the text you want to encrypt: "))

numbers_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26:'z'}
if n == "decrypt":
    def number_position (digits) :
        list_02 = []
        for i in digits.split():
            if int(i) in numbers_dict:
                let = numbers_dict[int(i)]
                list_02.append(let)
            letters = ''.join(list_02)
            print (letters)
    number_position(input("please type the numbers: "))