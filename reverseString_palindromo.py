# Escribe una función llamada reverseString. Esta función recibe como parámetro
# un string. La función se encarga de retornar el string recibido pero en orden
# de atrás hacia adelante.
# "Hola como estas" => "satse omoc aloH"

# def reverseString(str):
    # words = str.split()
    # bid_arr = []
    result = ""

    # for i in range(0, len(words)):
    #     bid_arr.append([s for s in words[i]])

    # for first_arr in range(len(bid_arr) - 1, -1, -1):
    #     for second_arr in range(len(bid_arr[first_arr]) -1, -1, -1):
    #         result += bid_arr[first_arr][second_arr]
    #     result += " "

def reverseString(str):
    for i in range(len(str) - 1, -1, -1):
        result += str[i]

    return result

print(reverseString('Hola como estas'))

# Escribe una función llamada palindromo. Esta función recibe como parámetro
# un string. La función se encarga de retornar True si el string es un palindromo
# False de lo contrario.
# Palíndromos: radar - oso - arañera - orejero - rayar - salas - seres - sometemos
# BONUS: "Anita lava la tina" - "No traces en ese carton" - "Son robos o sobornos"

# def palindromo(str):
    # original = ""
    # words = str.split()
    # bid_arr = []
    # result = ""

    # for i in range(0, len(words)):
    #     bid_arr.append([s for s in words[i]])
    #     original += words[i]
    
    # for first_arr in range(len(bid_arr) - 1, -1, -1):
    #     for second_arr in range(len(bid_arr[first_arr]) -1, -1, -1):
    #         result += bid_arr[first_arr][second_arr]

    # if result.strip().lower() == original.strip().lower():
    #     return True

    # return False


def palindromo(str):
    return reverseString(str).lower().replace(" ", "") == str.lower().replace(" ", "")


print(palindromo('Anita lava la tina'))