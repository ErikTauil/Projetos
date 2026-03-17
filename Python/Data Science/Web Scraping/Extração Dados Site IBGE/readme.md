# 🚀 Scraping de Indicadores do IBGE com Python

Projeto simples e prático para coletar, tratar e visualizar indicadores oficiais dos estados brasileiros utilizando Python.

---

## 📊 Visão geral

Este projeto automatiza a coleta de dados diretamente do site do IBGE, transformando informações públicas em uma estrutura organizada e pronta para análise.

👉 Ideal para quem quer trabalhar com dados reais de forma prática.

---

## 🔎 O que o projeto faz

* Acessa dados oficiais de qualquer estado do Brasil
* Extrai indicadores diretamente da página do IBGE
* Realiza tratamento dos dados (limpeza e ajustes de texto)
* Organiza tudo em uma tabela utilizando **pandas**

---

## 💡 Exemplo prático

No exemplo demonstrado:

* São extraídos dados de **SP (São Paulo)** e **MG (Minas Gerais)**
* Mas o código funciona para **qualquer estado brasileiro**, bastando alterar a sigla

```python
estado = scraping_uf('sp')
```

---

## 🧠 Como funciona

O projeto segue um fluxo simples:

1. Faz uma requisição HTTP para a página do estado no IBGE
2. Utiliza BeautifulSoup para interpretar o HTML
3. Extrai os indicadores disponíveis
4. Realiza tratamento dos dados (remoção de trechos desnecessários)
5. Converte tudo em um DataFrame com pandas

---

## ⚙️ Tecnologias utilizadas

* Python
* requests
* BeautifulSoup
* pandas

---

## 📈 Visualização dos dados

Após o processamento, os dados são organizados em um DataFrame:

```python
df = pd.DataFrame(estado.values(), index=estado.keys())
```

👉 Isso permite:

* Visualização estruturada
* Análises rápidas
* Integração com gráficos e dashboards

---

## 🧹 Tratamento dos dados

O projeto inclui uma etapa de limpeza para melhorar a qualidade das informações:

* Remoção de observações e caracteres extras
* Padronização dos valores extraídos

---

## 🚀 Como usar

### 1. Instale as dependências

```bash
pip install requests beautifulsoup4 pandas
```

---

### 2. Execute o script

```python
estado = scraping_uf('mg')
```

---

### 3. Visualize os dados

```python
print(df)
```

---

## ⚠️ Observações

* O projeto depende da estrutura do site do IBGE
* Mudanças no site podem impactar o funcionamento
* Os dados são públicos e extraídos diretamente da fonte oficial

---

## 💡 Possíveis melhorias

* Exportação para CSV/Excel
* Criação de gráficos automáticos
* Coleta de múltiplos estados em lote
* Integração com APIs ou dashboards

---

## 👨‍💻 Aplicações

Este tipo de projeto pode ser usado em:

* Análise de dados
* Automação de relatórios
* Estudos acadêmicos
* Projetos de Data Science

---

## 📌 Objetivo

Demonstrar, de forma prática, como coletar, tratar e visualizar dados reais utilizando Python.

---
