# 📘 Guía de Usuario — Sistema de Predicción de Abandono Estudiantil

**Proyecto Final · Inteligencia Artificial · EAFIT 2026-1**  
Santiago Arboleda · Juan Esteban Villada · Cristian Cabezas  
Repositorio: https://github.com/sarboledag/PROYECTO-FINAL

---

## ¿Qué hace este sistema?

Este sistema predice el riesgo de abandono estudiantil a partir de variables académicas, económicas y personales. Dado un estudiante, el sistema:

1. Estima la **probabilidad de que abandone** sus estudios
2. Clasifica el riesgo en **Alto, Medio o Bajo**
3. Genera una **recomendación personalizada** de intervención para orientadores académicos

---

## Requisitos

- Python 3.8 o superior
- Las librerías listadas en `requirements.txt`

---

## Instalación

**1. Clonar el repositorio:**
```bash
git clone https://github.com/sarboledag/PROYECTO-FINAL.git
cd PROYECTO-FINAL
```

**2. Instalar dependencias:**
```bash
pip install -r requirements.txt
```

---

## Cómo ejecutar la aplicación

Desde la raíz del proyecto ejecuta:

```bash
streamlit run app.py
```

Se abrirá automáticamente en el navegador en `http://localhost:8501`.

---

## Cómo usar la aplicación paso a paso

### Paso 1 — Abrir la aplicación
Al ejecutar el comando verás la pantalla principal con el título **"Sistema de Predicción de Abandono Estudiantil"**.

### Paso 2 — Seleccionar un estudiante
En el panel izquierdo (sidebar) encontrarás:

> **Selecciona el índice del estudiante**

Ingresa un número entre `0` y `4423`. Cada número representa un estudiante diferente del dataset.

### Paso 3 — Ver los datos del estudiante
Aparecerá una tabla con todas las variables del estudiante: notas, materias aprobadas, edad de ingreso, estado financiero, entre otras.

### Paso 4 — Predecir el riesgo
Haz clic en el botón:

> **Predecir riesgo de abandono**

El sistema mostrará tres métricas:

| Métrica | Descripción |
|---|---|
| **Predicción** | "Abandona" o "No abandona" |
| **Probabilidad de abandono** | Porcentaje estimado de riesgo |
| **Nivel de riesgo** | Alto (≥70%), Medio (≥40%), Bajo (<40%) |

### Paso 5 — Leer la recomendación
Debajo aparecerá una recomendación personalizada. Ejemplo:

```
Nivel de riesgo: Alto
Probabilidad de abandono: 87.0%

Recomendaciones:
- Asignar tutorías académicas de refuerzo
- Remitir a bienestar universitario o apoyo financiero
- Programar revisión periódica del caso
```

---

## Cómo ejecutar el notebook

```bash
jupyter notebook notebooks/Proyecto_Final_IA_Abandono_Estudiantil.ipynb
```

El notebook está organizado en estos bloques:

| Bloque | Contenido |
|---|---|
| Bloque 1 | Carga del dataset desde UCI |
| Bloque 2 | Análisis exploratorio (EDA) |
| Bloque 3 | Preprocesamiento y división de datos |
| Bloque 4 | Entrenamiento de modelos |
| Bloque 5 | Visualización de resultados |
| Bloque 6 | Sistema de recomendación |
| Bloque 7 | Guardado de modelos |

---

## Estructura del proyecto

```
PROYECTO-FINAL/
├── app.py
├── README.md
├── requirements.txt
├── data/
│   └── student_dropout_procesado.csv
├── models/
│   ├── modelo_random_forest.pkl
│   └── columnas_modelo.pkl
├── notebooks/
│   └── Proyecto_Final_IA_Abandono_Estudiantil.ipynb
├── docs/
│   ├── informe_final.tex
│   ├── informe_final.pdf
│   └── guia_usuario.md
└── video/
    └── video_demo.webm
```

---

## Niveles de riesgo

| Nivel | Probabilidad | Acción sugerida |
|---|---|---|
| 🔴 **Alto** | ≥ 70% | Intervención inmediata: tutorías, apoyo financiero, seguimiento semanal |
| 🟡 **Medio** | 40% – 69% | Seguimiento mensual, orientación académica |
| 🟢 **Bajo** | < 40% | Monitoreo rutinario |

---

## Preguntas frecuentes

**¿De dónde vienen los datos?**  
Del dataset *Predict Students' Dropout and Academic Success* del UCI Machine Learning Repository. Contiene información de 4,424 estudiantes de universidades portuguesas.

**¿El modelo predice en tiempo real?**  
Sí. El modelo Random Forest ya está entrenado y guardado en `models/`. La app lo carga al iniciar y hace predicciones instantáneas.

**¿Qué tan preciso es el modelo?**  
AUC-ROC = 0.932 y F1 = 0.805 en el conjunto de prueba, superando ampliamente al baseline (AUC = 0.500).

---

*Universidad EAFIT · Inteligencia Artificial · 2026-1*
