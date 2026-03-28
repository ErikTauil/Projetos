# Importa a biblioteca Streamlit (usada para criar a interface web do app)
import streamlit as st

# Importa o NumPy (usado para trabalhar com números e arrays - base da IA)
import numpy as np

# Importa o Pandas (usado para criar tabelas organizadas)
import pandas as pd

# Importa o modelo de rede neural MLP do sklearn (o "cérebro" da IA)
from sklearn.neural_network import MLPClassifier


# -------------------------------
# 1. TREINAMENTO DA IA
# -------------------------------

# Cacheia o modelo para não treinar toda vez que o usuário interagir (melhora performance)
@st.cache_resource
def inicializar_ia():

    # Aqui criamos os dados de treino (o que a IA vai "estudar")
    # Cada linha representa uma situação do dia:
    # [Sol, Trânsito, Dinheiro, Amigos]
    X_treino = np.array([
        [1,0,1,1],  # Tem sol, sem trânsito, tem dinheiro, amigos vão
        [0,1,0,0],  # Não tem sol, tem trânsito, sem dinheiro, sem amigos
        [1,1,0,0],  # Tem sol, tem trânsito, sem dinheiro, sem amigos
        [0,0,1,1],  # Sem sol, sem trânsito, tem dinheiro, amigos vão
        [1,0,0,1],  # Tem sol, sem trânsito, sem dinheiro, amigos vão
        [0,1,1,0],  # Sem sol, com trânsito, tem dinheiro, sem amigos
        [1,1,1,1],  # Tudo positivo (mas pode ter decisão negativa)
        [0,1,1,1],  # Sem sol, com trânsito, mas com dinheiro e amigos
        [1,0,1,0],  # Sol e dinheiro, mas sem amigos
        [0,0,0,1],  # Só amigos vão
        [1,0,1,1],  # Repetição para reforçar padrão
        [0,1,0,1],  # Trânsito e amigos
        [1,1,1,0],  # Tudo menos amigos
        [0,1,1,1],  # Reforço de cenário negativo
        [0,1,0,1]   # Repetição
    ])

    # Aqui estão as respostas esperadas para cada cenário
    # 1 = Vai pra praia
    # 0 = Não vai
    y_treino = np.array([
        1,0,0,
        1,0,0,
        0,0,1,
        0,1,0,
        0,0,0
    ])

    # Cria o modelo de rede neural (IA)
    # hidden_layer_sizes=(8,) significa 8 "neurônios" internos
    # max_iter=3000 define quantas vezes a IA vai tentar aprender
    modelo = MLPClassifier(hidden_layer_sizes=(8,), max_iter=3000, random_state=42)

    # Aqui acontece o aprendizado (treinamento)
    # A IA aprende padrões com base nos dados acima
    modelo.fit(X_treino, y_treino)

    # Retorna o modelo já treinado
    return modelo


# Executa a função e guarda o modelo treinado
modelo = inicializar_ia()


# -------------------------------
# 2. INTERFACE DO APP
# -------------------------------

# Define título da aba do navegador e layout da página
st.set_page_config(page_title="Simulador IA", layout="centered")

# Título principal exibido na tela
st.title("🏖️ Simulador de Decisão Ir a Praia com IA - (By Erik Tauil)")

# Cria um formulário (grupo de inputs)
with st.form("form"):

    # Subtítulo da seção
    st.subheader("📊 Condições do Dia")

    # Perguntas para o usuário (radio = botão de seleção)
    f1 = st.radio("☀️ Está sol?", ("Não", "Sim"), horizontal=True)
    f2 = st.radio("🚗 Tem trânsito?", ("Não", "Sim"), horizontal=True)
    f3 = st.radio("💰 Tem dinheiro?", ("Não", "Sim"), horizontal=True)
    f4 = st.radio("👥 Amigos vão?", ("Não", "Sim"), horizontal=True)

    # Botão que envia o formulário
    btn = st.form_submit_button("🤖 Consultar IA")


# -------------------------------
# 3. PREVISÃO DA IA
# -------------------------------

# Só executa se o botão foi clicado
if btn:

    # Converte respostas "Sim/Não" para números (1 ou 0)
    dados = np.array([[
        1 if f1 == "Sim" else 0,
        1 if f2 == "Sim" else 0,
        1 if f3 == "Sim" else 0,
        1 if f4 == "Sim" else 0
    ]])

    # A IA faz a previsão (vai ou não vai)
    resultado = modelo.predict(dados)

    # A IA calcula a probabilidade de cada resultado
    prob = modelo.predict_proba(dados)

    # Linha divisória visual
    st.divider()

    # Se a IA decidiu ir
    if resultado[0] == 1:
        st.success("### ✅ PARTIU PRAIA!")

        # Barra de progresso mostrando confiança
        st.progress(float(prob[0][1]))

        # Mostra porcentagem de confiança
        st.info(f"Confiança: {prob[0][1]*100:.1f}%")

    else:
        st.error("### 🏠 MELHOR FICAR EM CASA")

        st.progress(float(prob[0][0]))
        st.info(f"Confiança: {prob[0][0]*100:.1f}%")


    # -------------------------------
    # 4. TABELA EXPLICATIVA
    # -------------------------------

    # Subtítulo
    st.subheader("📊 Como a IA tomou a decisão")

    # Lista de fatores analisados
    fatores = ["Sol", "Trânsito", "Dinheiro", "Amigos"]

    # Respostas do usuário
    valores = [f1, f2, f3, f4]

    # Peso de cada fator (explicação didática)
    pesos = [
        "Médio",
        "Alto (negativo)",
        "Alto (positivo)",
        "Muito Alto"
    ]

    # Lista que vai guardar o impacto (positivo ou negativo)
    impacto = []

    # Loop para analisar cada fator
    for i, v in enumerate(valores):

        # Trânsito é negativo quando está "Sim"
        if fatores[i] == "Trânsito":
            impacto.append("Negativo" if v == "Sim" else "Positivo")

        # Outros fatores são positivos quando "Sim"
        else:
            impacto.append("Positivo" if v == "Sim" else "Negativo")

    # Cria tabela com Pandas
    df = pd.DataFrame({
        "Fator": fatores,
        "Sua Resposta": valores,
        "Peso na Decisão": pesos,
        "Impacto": impacto
    })

    # Exibe tabela na tela
    st.dataframe(df, use_container_width=True)


    # -------------------------------
    # 5. INSIGHT AUTOMÁTICO
    # -------------------------------

    # Subtítulo
    st.subheader("🧠 Insight da IA")

    # Interpreta o nível de confiança da IA
    if prob[0][1] > 0.7:
        st.write("A decisão foi fortemente influenciada por fatores positivos como dinheiro e companhia.")

    elif prob[0][1] > 0.5:
        st.write("A decisão está equilibrada, mas fatores positivos ainda prevalecem.")

    else:
        st.write("Fatores negativos como trânsito ou falta de condições impactaram a decisão.")


# -------------------------------
# 6. BOTÃO DE RESET
# -------------------------------

# Botão para reiniciar o app
if st.button("🔄 Reiniciar"):

    # Recarrega a aplicação do zero
    st.rerun()