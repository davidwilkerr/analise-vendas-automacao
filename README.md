# 📊 Automação de Análise de Vendas e Envio de Relatórios

Uma solução em Python desenvolvida para automatizar a consolidação de relatórios de faturamento regional a partir de planilhas Excel e realizar a distribuição automatizada de e-mails corporativos.

---

## 📌 Visão Geral

Este projeto lê múltiplos arquivos `.xlsx` armazenados no diretório `dados/` (cada um representando as vendas de uma unidade/cidade), calcula o faturamento total acumulado, gera um ranking ordenado e formatado em moeda nacional (R$) e envia o relatório consolidado via e-mail utilizando SMTP seguro.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem base para scripting e automação.
- **Pandas**: Leitura, manipulação, agregação e ordenação de conjuntos de dados.
- **Openpyxl**: Engine de integração e leitura de arquivos Excel (`.xlsx`).
- **Yagmail**: Cliente SMTP simplificado para envio seguro de e-mails.
- **Python-dotenv**: Gerenciamento e isolamento de variáveis de ambiente e credenciais sensíveis.

---

## 📂 Estrutura do Repositório

```text
analise-vendas-automacao/
│
├── dados/                       # Planilhas de dados de vendas regionais
│   ├── Loja BH.xlsx
│   ├── Loja DF.xlsx
│   ├── Loja Manaus.xlsx
│   ├── Loja Rio.xlsx
│   ├── Loja Salvador.xlsx
│   └── Loja SP.xlsx
│
├── .gitignore                   # Regras de exclusão do Git (oculta senhas e arquivos temporários)
├── main.py                      # Script principal de processamento e automação
├── README.md                    # Documentação do projeto
└── requirements.txt             # Dependências do projeto

```

---

## ⚙️ Pré-requisitos e Instalação

1. **Clone o repositório:**
```bash
git clone [https://github.com/SEU-USUARIO/analise-vendas-automacao.git](https://github.com/SEU-USUARIO/analise-vendas-automacao.git)
cd analise-vendas-automacao

```


2. **Instale as dependências:**
```bash
pip install -r requirements.txt

```


3. **Configure as credenciais (Variáveis de Ambiente):**
Crie um arquivo chamado `.env` na raiz do projeto (este arquivo é ignorado pelo Git por motivos de segurança) e adicione suas credenciais:
```env
EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=sua_senha_de_aplicativo

```


> 💡 *Nota:* Para contas Gmail, utilize uma **Senha de Aplicativo** gerada nas configurações de segurança da sua conta Google.



---

## 🚀 Como Executar

Após configurar o arquivo `.env` e garantir que as planilhas estão dispostas no diretório `dados/`, execute o script principal:

```bash
python main.py

```

O script irá:

1. Processar todas as planilhas na pasta `dados/`.
2. Exibir o ranking de vendas no terminal.
3. Disparar o e-mail contendo o relatório formatado.

---

## 👨‍💻 Autor

Desenvolvido por **David Souza**

Estudante de Análise e Desenvolvimento de Sistemas | Entusiasta de Automação e Análise de Dados

```

```