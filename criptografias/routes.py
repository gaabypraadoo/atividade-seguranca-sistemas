from flask import render_template, request
from main import app
from utils.cifra_cesar import cifra_cesar, decifra_cesar
from utils.cifra_hill import cifra_hill, decifrar_hill, matriz_inversa_mod26


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

@app.route("/hill", methods=["GET", "POST"])
def hill():
    resultado = None

    if request.method == "POST":

        mensagem = request.form.get("mensagem")
        chave_input = request.form.get("chave")

        try:
            numeros = list(map(int, chave_input.split()))
            
            #verifica se chave tem 4 números
            if len(numeros) != 4:
                raise ValueError("A chave deve ter 4 números")
            
            matriz = [numeros[:2], numeros[2:]] #cria matriz 2x2

            #testa se a matriz tem inverso módulo 26
            try:
                _ = matriz_inversa_mod26(matriz)
            except ValueError:
                raise ValueError("A chave informada não é válida - não possui inverso modular.")
            
            criptografado = cifra_hill(mensagem, matriz)
            descriptografado = decifrar_hill(criptografado, matriz)

            resultado = {
                "mensagem_original": mensagem,
                "chave": matriz,
                "criptografado": criptografado,
                "descriptografado": descriptografado
            }
        except ValueError as e:
            resultado = {"erro": str(e)}

    return render_template("pagina_hill.html", resultado=resultado)