import yagmail
import pandas as pd
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env local
load_dotenv()

listaCidades = ["BH", "DF", "Manaus", "Rio", "Salvador", "SP"]

faturamentos = {}
for cidade in listaCidades:
    vendas_df = pd.read_excel(f"dados/Loja {cidade}.xlsx")
    faturamento_cidade = sum(vendas_df["Vendas"])
    faturamentos[cidade] = faturamento_cidade    

print(faturamentos)

# Criar o ranking
# Transformar o dicionário em uma tabela e ordenar a tabela
# Pandas ->
    # colunas = columns
    # linhas = index
ranking_df = pd.DataFrame.from_dict(faturamentos, orient="index", columns=["Vendas"])
# Ordenando em ordem crescente
ranking_df = ranking_df.sort_values(by="Vendas", ascending=False)
ranking_df = ranking_df.map("R${:,.2f}".format)
print(ranking_df)

mensagem = f"""
Prezados,
Segue em anexo o ranking de venda das Lojas:
Ranking:

{ranking_df.to_string().replace(" ", "-")}

Qualquer dúvida, estou a disposição,
Att., David Souza
"""

# Como enviar por email
# 4 grandes formas
    # Yagmail - a mais direta e simples
    # Smtplib - não é tão direto, mas é bem personalizado
    # Pyautogui - automação por RPA -> so usa em automações que já são RPA
    # Outlook - usa quando a empresa usa outlook


# Busca as credenciais com segurança das variáveis de ambiente
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

if EMAIL_USER and EMAIL_PASS:
    usuario = yagmail.SMTP(EMAIL_USER, EMAIL_PASS)
    usuario.send(
        to="davidwilker.ti+teste@gmail.com",
        subject="Ranking de vendas das Lojas",
        contents=mensagem,
    )
    print("E-mail enviado com sucesso!")
else:
    print(
        "Erro: Verifique se EMAIL_USER e EMAIL_PASS estão definidos no arquivo .env"
    )