def deslocar_caractere(caractere, deslocamento):
    """
    desloca uma letra ASCII (A-Z, a-z) mantendo maiusculas e minusculas.
    Se o caractere não for letra ASCII, retorna caractere sem alterar.
    """
    
    #verifica se o caractere esta entre 'A' e 'Z' no código ASCII(maiúsculas)
    if 'A' <= caractere <= 'Z':
        #calcula a posição da letra no alfabeto(de 0 a 25)
        base = ord('A') # a função ord() converte um caractere em seu código numérico ASCII
        #adiciona o deslocamento desejado e garante que o resultado fique entre 0 e 25 (se passar do Z volta para o A)
        return chr((ord(caractere) - base + deslocamento) % 26 + base)# a função chr converte o número em letra de volta
    
    #verifica se o caractere esta entre 'a' e 'z' no código ASCII(minúsculas)
    if 'a' <= caractere <= 'z':
        base = ord('a')
        return chr((ord(caractere) - base + deslocamento) % 26 + base)
    
    #se não for letra ASCII
    return caractere

def cifra_cesar(texto, deslocamento):
    """
    Aplica a cifra de César ao texto com o deslocamento dado.
    deslocamento pode ser positivo (cifrar) ou negativo (decifrar).
    """
    if not isinstance(texto, str):
        raise TypeError("digite apenas letras.")
    
    #padronizar o deslocamento para 0 à 25 para evitar valores grandes
    valor_a_deslocar = deslocamento % 26
    resultado_caracteres = []
    for caractere in texto:
        resultado_caracteres.append(deslocar_caractere(caractere, valor_a_deslocar))
    return ''.join(resultado_caracteres) #junta todos os elementos da lista em uma única string

def decifra_cesar(texto_cifrado, deslocamento):
    """decifra aplicando o deslocamento negativo"""
    return cifra_cesar(texto_cifrado, -deslocamento)

texto_cifrado = cifra_cesar("tarefa", 4)
print(texto_cifrado)
print(decifra_cesar(texto_cifrado, 4))
