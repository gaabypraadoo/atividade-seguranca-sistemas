from flask import Flask, render_template, request

app = Flask(__name__)

def vigenere_encrypt(mensagem, chave):
    mensagem = mensagem.upper().replace(" ", "")
    chave = chave.upper().replace(" ", "")
    resultado = ""
    chave_repetida = (chave * (len(mensagem) // len(chave) + 1))[:len(mensagem)]

    for m, c in zip(mensagem, chave_repetida):
        if m.isalpha():
            valor = (ord(m) + ord(c) - 2 * ord('A')) % 26
            resultado += chr(valor + ord('A'))
        else:
            resultado += m
    return resultado


def vigenere_decrypt(mensagem, chave):
    mensagem = mensagem.upper().replace(" ", "")
    chave = chave.upper().replace(" ", "")
    resultado = ""
    chave_repetida = (chave * (len(mensagem) // len(chave) + 1))[:len(mensagem)]

    for m, c in zip(mensagem, chave_repetida):
        if m.isalpha():
            valor = (ord(m) - ord(c) + 26) % 26
            resultado += chr(valor + ord('A'))
        else:
            resultado += m
    return resultado


@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == 'POST':
        mensagem = request.form['mensagem']
        chave = request.form['chave']

        if len(mensagem.split()) < 4:
            resultado = {'erro': 'A mensagem deve ter no mínimo quatro palavras.'}
        elif not chave:
            resultado = {'erro': 'A chave não pode estar vazia.'}
        else:
            criptografado = vigenere_encrypt(mensagem, chave)
            descriptografado = vigenere_decrypt(criptografado, chave)

            resultado = {
                'mensagem_original': mensagem,
                'chave': chave,
                'criptografado': criptografado,
                'descriptografado': descriptografado
            }

    return render_template('web.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)