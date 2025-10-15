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

def inverso_modular(numero_inverso_modular, valor_limite_alfabeto):
    for x in range(1, valor_limite_alfabeto):
        if (numero_inverso_modular * x) % valor_limite_alfabeto == 1:
            return x
    raise ValueError("Não existe inverso modular")
    
def matriz_inversa_mod26(matriz):
    a, b = matriz[0]
    c, d = matriz[1]

    determinante_matriz = (a * d - b * c) % 26
    inverso_modular_determinante = inverso_modular(determinante_matriz, 26)
    
    matriz_adjunta = [
        [d, -b],
        [-c, a]
    ]

    #aplica o inverso do determinante e módulo 26
    inversa = []
    for linha in matriz_adjunta:
        nova_linha = [(inverso_modular_determinante * x) % 26 for x in linha]
        inversa.append(nova_linha)

    return inversa

def decifrar_hill(texto_cifrado, chave):
    texto_cifrado = texto_cifrado.replace(" ", "").upper()
    matriz_inversa = matriz_inversa_mod26(chave)

    texto_decifrado = ""

    for i in range(0, len(texto_cifrado), 2):
        bloco = texto_cifrado[i:i+2]
        vetor = [converter_letra_para_numero(bloco[0]), converter_letra_para_numero(bloco[1])]
        resultado = multiplicar_matriz_vetor(matriz_inversa, vetor)
        texto_decifrado += converter_numero_para_letra(resultado[0]) + converter_numero_para_letra(resultado[1])

    return texto_decifrado

#exemplo de uso:
chave = [[3, 3],
         [2, 5]] #matriz-chave 2x2 válida
texto = "Tarefa"

cifrado = cifra_hill(texto, chave)
print("Texto cifrado:", cifrado)

decifrado = decifrar_hill(cifrado, chave)
print("Texto decifrado", decifrado)