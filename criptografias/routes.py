from flask import render_template, request
from main import app
from utils.cifra_cesar import cifra_cesar, decifra_cesar



@app.route("/cesar", methods=["GET", "POST"])
def cesar():
    resultado = None

    if request.method == "POST":
        mensagem = request.form.get("mensagem")
        chave = request.form.get("chave")

        try:
            deslocamento = int(chave)
            criptografado = cifra_cesar(mensagem, deslocamento)
            descriptografado = decifra_cesar(criptografado, deslocamento)

            resultado = {
                "mensagem_original": mensagem,
                "chave": deslocamento,
                "criptografado": criptografado,
                "descriptografado": descriptografado
            }
        except ValueError:
            resultado = {"erro": "A chave deve ser um número inteiro."}

    return render_template("pagina_cesar.html", resultado=resultado)

