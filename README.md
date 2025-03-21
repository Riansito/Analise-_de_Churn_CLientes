# Projeto de Previsão de Churn de Clientes Bancários

Este projeto tem como objetivo prever o **churn** (cancelamento) de clientes de um banco, utilizando técnicas de análise de dados e machine learning. Abaixo estão as informações sobre o projeto, incluindo a descrição das colunas do dataset, as etapas realizadas e os resultados obtidos.

---

## **Descrição das Colunas**

Aqui estão as colunas do dataset e seus significados:

| **Nome da Coluna**       | **Significado**                                                                 |
|--------------------------|--------------------------------------------------------------------------------|
| **RowNumber**            | Número da linha no dataset (não afeta o resultado).                            |
| **CustomerId**           | ID único do cliente (não afeta o resultado).                                   |
| **Surname**              | Sobrenome do cliente (não afeta o resultado).                                  |
| **CreditScore**          | Pontuação de crédito do cliente (quanto maior, menor a chance de churn).       |
| **Geography**            | Localização geográfica do cliente (pode afetar o churn).                       |
| **Gender**               | Gênero do cliente (pode ser relevante para análise de churn).                  |
| **Age**                  | Idade do cliente (clientes mais velhos tendem a cancelar menos).               |
| **Tenure**               | Tempo (em anos) que o cliente é cliente do banco (clientes mais antigos tendem a cancelar menos). |
| **Balance**              | Saldo da conta do cliente (clientes com saldo maior tendem a cancelar menos).  |
| **NumOfProducts**        | Número de produtos que o cliente contratou no banco.                           |
| **HasCrCard**            | Indica se o cliente possui cartão de crédito (1 = sim, 0 = não).               |
| **IsActiveMember**       | Indica se o cliente é um membro ativo (1 = sim, 0 = não).                      |
| **EstimatedSalary**      | Salário estimado do cliente (clientes com salários mais altos tendem a cancelar menos). |
| **Exited**               | Indica se o cliente deixou o banco (1 = sim, 0 = não).                         |
| **Complain**             | Indica se o cliente registrou uma reclamação (1 = sim, 0 = não).               |
| **Satisfaction Score**   | Pontuação de satisfação do cliente com a resolução de reclamações.             |
| **Card Type**            | Tipo de cartão que o cliente possui.                                           |
| **Points Earned**        | Pontos acumulados pelo cliente ao usar o cartão de crédito.                    |

---

## **Etapas do Projeto**

1. **Análise Exploratória de Dados (EDA):**
   - Verificação de valores faltantes e outliers.
   - Análise da distribuição das variáveis.
   - Identificação de correlações entre as variáveis e o churn.

2. **Pré-processamento dos Dados:**
   - Codificação de variáveis categóricas (ex.: Geography, Gender).
   - Normalização de variáveis numéricas (ex.: Age, Balance).
   - Divisão dos dados em conjuntos de treino e teste.

3. **Modelagem:**
   - Treinamento de modelos de machine learning, como **Random Forest**, **XGBoost** e **Regressão Logística**.
   - Ajuste de hiperparâmetros usando técnicas como **GridSearchCV**.

4. **Avaliação do Modelo:**
   - Uso de métricas como **AUC-ROC**, **Recall**, **Precisão** e **F1-Score**.
   - Análise da importância das variáveis para o modelo.

5. **Implementação de Ações:**
   - Identificação de clientes com alta probabilidade de churn.
   - Sugestão de estratégias de retenção baseadas nos insights obtidos.


## **Como Executar o Projeto**

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
