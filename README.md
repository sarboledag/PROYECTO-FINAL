# Sistema de Predicción de Abandono Estudiantil con Machine Learning

## Descripción del proyecto

Este proyecto desarrolla un sistema de Inteligencia Artificial para predecir el riesgo de abandono estudiantil a partir de variables académicas, económicas y personales.

El modelo principal utilizado es un Random Forest, el cual estima la probabilidad de abandono de cada estudiante. Además, el sistema incluye un componente de recomendación personalizada que transforma la predicción del modelo en orientaciones accionables para intervención temprana.

## Dataset

Se utiliza el dataset **Predict Students' Dropout and Academic Success**, disponible en UCI Machine Learning Repository.

El dataset contiene información de estudiantes de educación superior y permite analizar tres estados académicos: graduado, matriculado y abandono. Para este proyecto, la variable objetivo se transformó en una clasificación binaria:

- 0: No abandona
- 1: Abandona

## Modelos evaluados

Se evaluaron tres modelos:

1. Baseline basado en clase mayoritaria.
2. Regresión Logística.
3. Random Forest.

## Resultados principales

| Modelo | Accuracy | Precision | Recall | F1 | AUC-ROC |
|---|---:|---:|---:|---:|---:|
| Baseline | 0.6791 | 0.0000 | 0.0000 | 0.0000 | 0.5000 |
| Regresión Logística | 0.8858 | 0.8894 | 0.7359 | 0.8054 | 0.9266 |
| Random Forest | 0.8847 | 0.8823 | 0.7394 | 0.8046 | 0.9316 |

El modelo Random Forest fue seleccionado como modelo principal debido a su buen desempeño general, especialmente en AUC-ROC y recall.

## Estructura del proyecto

```text
proyecto-final-ia/
├── app.py
├── README.md
├── requirements.txt
├── data/
│   └── student_dropout_procesado.csv
├── models/
│   ├── modelo_random_forest.pkl
│   └── columnas_modelo.pkl
└── notebooks/
    └── Proyecto_Final_IA_Abandono_Estudiantil.ipynb
