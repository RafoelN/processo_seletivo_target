string = "Fui viajar"

string_resultante = ''

#Código para iterar a stringa de forma inversa o range recebe os seguintes parametros Start, Stop, Step
for i in range(len(string) - 1, -1, -1):
    string_resultante += string[i]

print(string_resultante)