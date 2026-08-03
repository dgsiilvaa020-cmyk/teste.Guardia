import sqlite3
import re

def definir_destino(pacote):
    """
    Decide para onde o pedido será enviado.
    """

    if pacote.get("tipo_envio") == "traducao":
        return "traducao"

    return "acervo"


def marcar_como_traducao(pacote):
    """
    Marca o pacote como sendo do grupo de tradução.
    """

    pacote["tipo_envio"] = "traducao"

    return pacote


def eh_traducao(pacote):
    """
    Verifica se o pacote é de tradução.
    """

    return pacote.get("tipo_envio") == "traducao"
