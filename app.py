
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Predicción de Abandono Estudiantil",
    page_icon="🎓",
    layout="wide"
)

@st.cache_resource
def cargar_modelo():
    modelo = joblib.load("models/modelo_random_forest.pkl")
    columnas = joblib.load("models/columnas_modelo.pkl")
    return modelo, columnas

@st.cache_data
def cargar_datos():
    return pd.read_csv("data/student_dropout_procesado.csv")

modelo, columnas_modelo = cargar_modelo()
df = cargar_datos()

def clasificar_riesgo(probabilidad):
    if probabilidad >= 0.70:
        return "Alto"
    elif probabilidad >= 0.40:
        return "Medio"
    else:
        return "Bajo"

def resumir_estudiante_para_llm(estudiante, probabilidad):
    datos = estudiante.iloc[0]
    riesgo = clasificar_riesgo(probabilidad)

    resumen = {
        "nivel_riesgo": riesgo,
        "probabilidad_abandono": round(probabilidad * 100, 2),
        "materias_aprobadas_1er_sem": datos.get("Curricular units 1st sem (approved)", "No disponible"),
        "nota_1er_sem": datos.get("Curricular units 1st sem (grade)", "No disponible"),
        "materias_aprobadas_2do_sem": datos.get("Curricular units 2nd sem (approved)", "No disponible"),
        "nota_2do_sem": datos.get("Curricular units 2nd sem (grade)", "No disponible"),
        "matricula_al_dia": datos.get("Tuition fees up to date", "No disponible"),
        "deudor": datos.get("Debtor", "No disponible"),
        "becario": datos.get("Scholarship holder", "No disponible"),
        "edad_ingreso": datos.get("Age at enrollment", "No disponible")
    }

    return resumen

def respuesta_llm_demo(resumen):
    riesgo = resumen["nivel_riesgo"]
    prob = resumen["probabilidad_abandono"]

    respuesta = f"""
**Nivel de riesgo:** {riesgo}

El modelo identifica una probabilidad estimada de abandono del **{prob}%**. 
Este resultado indica que el estudiante requiere seguimiento institucional, especialmente en factores académicos y de permanencia.

**Recomendaciones concretas:**
"""

    if resumen["materias_aprobadas_2do_sem"] != "No disponible" and resumen["materias_aprobadas_2do_sem"] < 3:
        respuesta += "\n- Asignar tutorías académicas para reforzar las asignaturas con bajo desempeño."

    if resumen["nota_2do_sem"] != "No disponible" and resumen["nota_2do_sem"] < 10:
        respuesta += "\n- Realizar seguimiento al rendimiento académico del segundo semestre."

    if resumen["matricula_al_dia"] == 0 or resumen["deudor"] == 1:
        respuesta += "\n- Remitir el caso a bienestar universitario o apoyo financiero."

    if resumen["edad_ingreso"] != "No disponible" and resumen["edad_ingreso"] > 25:
        respuesta += "\n- Ofrecer acompañamiento flexible considerando posibles responsabilidades laborales o familiares."

    respuesta += "\n- Programar una revisión periódica del caso para verificar si el riesgo disminuye."

    return respuesta

st.title("🎓 Sistema de Predicción de Abandono Estudiantil")

st.write(
    "Esta aplicación utiliza un modelo de Machine Learning para estimar el riesgo de abandono "
    "de un estudiante y generar una recomendación personalizada de intervención."
)

st.divider()

df_modelo = df.drop(columns=["Target", "Dropout_Binary"], errors="ignore")

st.sidebar.header("Selección de estudiante")

indice = st.sidebar.number_input(
    "Selecciona el índice del estudiante",
    min_value=0,
    max_value=len(df_modelo) - 1,
    value=0,
    step=1
)

estudiante = df_modelo.iloc[[indice]]

st.subheader("Datos del estudiante seleccionado")
st.dataframe(estudiante)

if st.button("Predecir riesgo de abandono"):
    prediccion = modelo.predict(estudiante)[0]
    probabilidad = modelo.predict_proba(estudiante)[0][1]
    riesgo = clasificar_riesgo(probabilidad)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Predicción", "Abandona" if prediccion == 1 else "No abandona")

    with col2:
        st.metric("Probabilidad de abandono", f"{probabilidad:.2%}")

    with col3:
        st.metric("Nivel de riesgo", riesgo)

    st.divider()

    st.subheader("Recomendación personalizada")

    resumen = resumir_estudiante_para_llm(estudiante, probabilidad)
    recomendacion = respuesta_llm_demo(resumen)

    st.markdown(recomendacion)

    st.info(
        "Nota: el modelo Random Forest realiza la predicción. "
        "El componente de recomendación transforma la predicción y las variables relevantes "
        "en una orientación comprensible para intervención académica."
    )
