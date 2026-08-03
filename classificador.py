import sqlite3
import re

# classificador.py


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

    else:
        pacote["tipo_envio"] = "acervo"

    return pacote



def eh_grupo_traducao(pacote):
    """
    Verifica se deve ir para o grupo de tradução.
    """

    return pacote.get("tipo_envio") == "traducao"
