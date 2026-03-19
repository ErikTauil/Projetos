# ⚽ Análise Estatística de Times Brasileiros com Python

## 📊 Sobre o Projeto

Este projeto realiza a **coleta, tratamento e análise de estatísticas de times do futebol brasileiro** (Série A e Série B), utilizando dados da API do SofaScore.

A aplicação permite:

* 📥 Coletar dados automaticamente de temporadas (2025 e 2026)
* 🧹 Tratar e organizar os dados com Python
* 📊 Gerar tabelas comparativas entre dois times
* 📈 Criar gráficos interativos para análise visual

---

## 🎯 Objetivo

Transformar dados brutos de futebol em **informações estratégicas**, permitindo análises comparativas de desempenho entre times.

---

## ⚙️ Como o Projeto Funciona (Explicação Simples)

1. Você informa o nome de um ou dois times
2. O sistema busca os dados automaticamente
3. Organiza tudo em formato de tabela
4. Calcula métricas como média de desempenho
5. Permite visualizar os dados ou gerar gráficos

---

## 🧠 Fluxo Técnico do Projeto

### 🔹 1. Coleta de Dados (API)

O sistema acessa a API pública do SofaScore:

* Identifica o time e a série (A ou B)
* Consulta dados das temporadas:

  * 2025
  * 2026
* Retorna estatísticas como:

  * gols marcados
  * gols sofridos
  * chutes
  * assistências
  * entre outras

📌 *Obs: Não é scraping tradicional — é consumo direto de API (mais robusto e profissional)*

---

### 🔹 2. Tratamento de Dados (Pandas)

Os dados são transformados em DataFrame:

* Conversão de JSON → tabela
* Remoção de estruturas complexas (dict/list)
* Conversão de dados numéricos
* Criação de coluna de média (`Media`)
* Estrutura MultiIndex para comparação entre times

---

### 🔹 3. Análise Comparativa

O sistema:

* Alinha métricas entre dois times
* Garante consistência de dados
* Gera uma tabela comparativa estruturada

Exemplo:

| Métrica       | São Paulo | Palmeiras |
| ------------- | --------- | --------- |
| Gols Marcados | 43        | 66        |
| Assistências  | 33        | 44        |

---

### 🔹 4. Visualização de Dados (Plotly)

Geração de gráficos interativos:

* Comparação por métrica
* Visualização por ano (2025 vs 2026)
* Gráficos de barras dinâmicos

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Pandas** → manipulação de dados
* **Requests** → consumo de API
* **Plotly** → visualização interativa
* **Jupyter Notebook** → ambiente de análise

---

## 📦 Estrutura do Projeto

```
📁 projeto
 ┣ 📄 main.ipynb
 ┣ 📄 script.py
 ┣ 📄 README.md
 ┗ 📄 requirements.txt
```

---

## 🚀 Como Executar

### 1. Instalar dependências

```bash
pip install pandas requests plotly nbformat openpyxl
```

---

### 2. Executar no Jupyter

```python
df = gerar_estatisticas("sao paulo", "palmeiras")
df
```

---

### 3. Gerar gráfico

```python
gerar_grafico(df, "goalsScored")
```

---

## 📊 Exemplos de Métricas

* goalsScored
* goalsConceded
* assists
* shots
* ballRecovery
* freeKicks

---

## 💡 Diferenciais do Projeto

✅ Uso de API (não scraping frágil)
✅ Estrutura profissional de dados
✅ MultiIndex (padrão BI)
✅ Separação de camadas (coleta, processamento, visualização)
✅ Pronto para evolução em dashboard

---

## 📈 Possíveis Evoluções

* Dashboard interativo (Streamlit)
* Ranking automático de times
* Machine Learning para previsão de resultados
* Integração com Power BI

---

## 👨‍💻 Autor

**Erik Lopes Tauil**

---

## 📌 Conclusão

Este projeto demonstra como transformar dados esportivos em **insights analíticos reais**, aplicando conceitos de:

* Data Science
* Engenharia de Dados
* Business Intelligence

---

💬 *Ideal para portfólio de Data Analyst / Data Scientist*
