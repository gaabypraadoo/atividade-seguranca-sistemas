from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == 'POST':
        try:
            mensagem = int(request.form['mensagem'])
            bits_mensagem = mensagem.bit_length()
            chave = random.randint(0, (2 ** bits_mensagem) - 1)
            criptografado = mensagem ^ chave
            descriptografado = criptografado ^ chave

            resultado = {
                'mensagem_decimal': mensagem,
                'mensagem_bin': bin(mensagem)[2:],
                'chave_decimal': chave,
                'chave_bin': bin(chave)[2:],
                'criptografado_decimal': criptografado,
                'criptografado_bin': bin(criptografado)[2:],
                'descriptografado_decimal': descriptografado,
                'descriptografado_bin': bin(descriptografado)[2:]
            }

        except ValueError:
            resultado = {'erro': 'Entrada inválida. Digite um número decimal válido.'}

    return render_template('pagina.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
