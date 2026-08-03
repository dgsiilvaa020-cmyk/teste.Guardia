import sqlite3
import re

# classificador.py

def mensagem_final_envio(pacote, link):

    if pacote.get("tipo_envio") == "traducao":

        return (
            "✨ Feitiço postado no grupo de tradução!\n\n"
            "🕯️Seu E-book está aqui:\n"
            f"{link}"
        )

    return (
        "✨ Feitiço concluído com sucesso!\n\n"
        "🕯️Seu E-book está aqui:\n"
        f"{link}"
    )

def classificar_envio(tipo_envio):

    if tipo_envio == "traducao":
        return {
            "grupo": "traducao",
            "mensagem": (
                "✨ Feitiço postado no grupo de tradução!\n\n"
                "🕯️Seu E-book está aqui:"
            )
        }

    return {
        "grupo": "acervo",
        "mensagem": None
    }

def definir_destino(pacote):
    """
    Decide o grupo de destino.
    """

    if pacote.get("traducao") == "🤖 Tradução Mecânica":
        return "traducao"

    return "acervo"



def marcar_tipo_traducao(pacote):
    """
    Salva a escolha da tradução.
    """

    if pacote.get("traducao") == "🤖 Tradução Mecânica":
        pacote["tipo_envio"] = "traducao"

    elif pacote.get("traducao") == "📚 Tradução Oficial":
        pacote["tipo_envio"] = "acervo"

    else:
        pacote["tipo_envio"] = "acervo"

    return pacote


def eh_grupo_traducao(pacote):
    """
    Verifica se deve ir para o grupo de tradução.
    """

    return pacote.get("tipo_envio") == "traducao"
