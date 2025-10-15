def converter_letra_para_numero(letra):
    return ord(letra.upper()) - ord('A')

def converter_numero_para_letra(numero):
    return chr((numero % 26) + ord('A'))

def multiplicar_matriz_vetor(matriz, vetor):
    resultado = []
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(vetor)):
            soma += matriz[i][j] * vetor[j]
        resultado.append(soma % 26)
    return resultado

#função principal: cifra de Hill (2x2)
def cifra_hill(texto, chave):
    #remove espaços e deixa em maiúscula
    texto = texto.replace(" ", "").upper()

    #se número de letras for ímpar, adiciona 'X' no final
    if len(texto) % 2 != 0:
        texto += 'X'

    texto_cifrado = ""

    #processa de 2 em 2 letras
    for i in range(0, len(texto), 2):
        bloco = texto[i:i+2]
        vetor = [converter_letra_para_numero(bloco[0]), converter_letra_para_numero(bloco[1])]
        resultado = multiplicar_matriz_vetor(chave, vetor)
        texto_cifrado += converter_numero_para_letra(resultado[0]) + converter_numero_para_letra(resultado[1])

    return texto_cifrado

#exemplo de uso:
chave = [[3, 3],
         [2, 5]] #matriz-chave 2x2 válida
texto = "Tarefa"

cifrado = cifra_hill(texto, chave)
print("Texto cifrado:", cifrado)