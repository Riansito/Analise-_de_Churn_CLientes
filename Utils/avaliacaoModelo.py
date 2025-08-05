#Graficos
import matplotlib.pyplot as plt
import seaborn as sns

#Manipulação de tabelas
import pandas as pd

#Avaliação do modelo
from scipy.stats import uniform, randint
from sklearn.metrics import accuracy_score,recall_score, f1_score
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold, cross_val_score
from sklearn.metrics import roc_curve, auc, confusion_matrix


plt.style.use("Solarize_Light2")
class AvaliacaoModelo:
    def __init__(self):
        pass

    def avaliacaoHiperParametros(self, modelo, parametros, metrica, X_train, y_train):

        model = modelo(random_state=42)
        cv = StratifiedKFold(5, shuffle=True, random_state=42)

        randomSearch = RandomizedSearchCV(
            estimator=model,
            param_distributions=parametros,
            n_iter=50,  
            scoring=metrica,  
            cv=cv,  # Número de folds na validação cruzada
            verbose=1,  # Mostra logs durante o treinamento
            n_jobs=-1,  # Usa todos os cores disponíveis
            random_state=42
        )


        randomSearch.fit(X_train, y_train)
        resultados = pd.DataFrame(randomSearch.cv_results_)
        dfd = resultados.sort_values(by="mean_test_score", ascending=False)
        
        return randomSearch.best_estimator_, dfd
    
    def avaliacaoCruzada(self, modelo, X_train, y_train): 
        estimadorFinal = modelo

        cv = StratifiedKFold(5, shuffle=True, random_state=42)#Serve para separar os dados em k folds para a avaliação mas mantendo a proporção da Target
        
        scoresAccuracy = cross_val_score(estimadorFinal, X_train, y_train, cv=cv, scoring='accuracy')#Avalicação cruzada focada em acuracia
        scoresRecall = cross_val_score(estimadorFinal, X_train, y_train, cv=cv, scoring='recall')#Avalicação cruzada focada em recall

        # Resultados
        print(f"Acurácia em cada fold: Acuracia =  {scoresAccuracy}")
        print(f"Acurácia em cada fold: recall =  {scoresRecall}")
            
        print("Acurácia média:", scoresAccuracy.mean())
        print("Recall medio: ", scoresRecall.mean())


    def matrizConfusao(self, melhorModelo,X_test ,y_test):
        #Calcular a matriz de confusão
        y_pred = melhorModelo.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)

        # 8. Plotar a matriz de confusão
        plt.figure(figsize=(6, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                    xticklabels=['Classe 0', 'Classe 1'],
                    yticklabels=['Classe 0', 'Classe 1'])
        plt.xlabel('Predito')
        plt.ylabel('Verdadeiro')
        plt.title('Matriz de Confusão')
        plt.show()

    
    def curvaRoc(self, melhorModelo, X_test, y_test):
        #Prever probabilidades para a curva ROC
        y_pred_prob = melhorModelo.predict_proba(X_test)[:, 1]  # Probabilidades da classe positiva

        #Calcular a curva ROC
        fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
        roc_auc = auc(fpr, tpr)

        #Plotar a curva ROC
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='blue', lw=2, label=f'Curva ROC (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='gray', linestyle='--', lw=2)
        plt.xlabel('Taxa de Falsos Positivos (FPR)')
        plt.ylabel('Taxa de Verdadeiros Positivos (TPR)')
        plt.title('Curva ROC')
        plt.legend(loc='lower right')
        plt.show()
    
    def importanciaVariaveis(self, melhorModelo, X_train):
        # Criando o DataFrame com colunas e suas influências
        df_importancia = pd.DataFrame({
            "Coluna": X_train.columns,
            "Importancia": melhorModelo.feature_importances_
        }).sort_values(by="Importancia", ascending=False)

        # Normalizando para usar no gradiente de cores
        influencia_normalizada = df_importancia["Importancia"] / df_importancia["Importancia"].max()
        cores = plt.cm.Blues(influencia_normalizada)

        # Plotando o gráfico
        plt.figure(figsize=(12, 6))
        barras = plt.bar(df_importancia["Coluna"], df_importancia["Importancia"], color=cores)

        # Adicionar os valores no topo das barras 
        for barra, valor in zip(barras, df_importancia["Importancia"]):
            plt.text(barra.get_x() + barra.get_width()/2, barra.get_height(), f'{valor:.3f}', 
                    ha='center', va='bottom', fontsize=8)

        plt.xticks(rotation=90)
        plt.grid(axis='y', linestyle='--', alpha=0.4)
        plt.title("📊 Importância das Variáveis no Modelo")
        plt.xlabel("Variáveis")
        plt.ylabel("Importância")
        plt.tight_layout()
        plt.show()
