import json
import os
import time
from datetime import datetime
from random import random
import requests

URL = "https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx"

def coletar_taxa():
    try:
        resposta = requests.get(URL, timeout=10)
        resposta.raise_for_status()
        conteudo = json.loads(resposta.text)
        taxa = float(conteudo["taxa"].replace(",", "."))
        return taxa + (random() - 0.5)
    except Exception as e:
        print("Erro ao coletar taxa:", e)
        return None

def main():
    arquivo = "taxa-cdi.csv"
    
    if not os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write("data,hora,taxa\n")
    
    for _ in range(10):
        agora = datetime.now()
        data = agora.strftime("%Y/%m/%d")
        hora = agora.strftime("%H:%M:%S")
        taxa = coletar_taxa()

        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(f"{data},{hora},{taxa}\n")
        
        time.sleep(2 + (random() - 0.5))
    
    print("Coleta finalizada. Arquivo 'taxa-cdi.csv' criado ou atualizado com sucesso.")

if __name__ == "__main__":
    main()