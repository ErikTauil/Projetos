# Treinando o modelo de classificação

# 1 - treinar um modelo com base nos dados para tentar prever o diagnóstico de doença cardíaca

# 2 - Utilizar esse modelo para criar um formulário 
# onde você pode preencher campos e o modelo vai dizer para você, conforme as variáveis, 
# se determinado paciente tem ou não uma doença cardíaca.


from ucimlrepo import fetch_ucirepo

heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
dados["doenca"] = (heart_disease.data.targets > 0) * 1

# X são todas as colunas dos dados, exceto a coluna doenca
X = dados.drop(columns='doenca')
# Y é a coluna doenca
y = dados['doenca']

# print(X.head())

# Treinando o modelo - Separando dados de treino e de teste:
# Separando Variáveis que dizem sobre os Pacientes, se teve diagnótico Positivo ou Não

from sklearn.model_selection import train_test_split
# Treino para Treinar o Modelo, Teste para saber o quão bom foi o resultado do Modelo
# test_size - Teste de 20% dos dados
# stratify - seleciona os pacientes COM e SEM diagnóstico de doença, proporcionalmente no treino e no teste. Importante
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=432, stratify=y)

# O modelo utilizado foi o xgboost, onde criamos um classificador de 0 ou 1
import xgboost as xgb
modelo = xgb.XGBClassifier(objective='binary:logistic')
modelo.fit(X_train, y_train)
preds = modelo.predict(X_test)

from sklearn.metrics import accuracy_score
# Calculando a Acuracia modelo acertou:
acuracia = accuracy_score(y_test, preds)
print(f'A acurácia do modelo é {acuracia:.2%}')
# Conclusão: A acurácia do modelo é 80.33%
# É um bom resultado.


# Salvando o modelo
import joblib
joblib.dump(modelo, 'modelo_xgboost.pkl')

medianas = X.median()
joblib.dump(medianas, 'medianas.pkl')