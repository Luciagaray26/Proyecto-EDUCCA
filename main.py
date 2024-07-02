import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### CONFIGURACIÓN DE PÁGINA

st.set_page_config(
    page_title="Análisis del Programa Educca",
    page_icon=":deciduous_tree:",
    # layout="wide"
)

### leer db
df = pd.read_csv("data.csv", sep=';', encoding='latin1')

### Leer imagenes
image0 = 'img/educca.png'
image1 = 'img/nombre-educca.jpeg'
image2 = 'img/educca-1.jpeg'
image3 = 'img/educca-2.jpeg'

### Cargar estilos
with open("css/styles.css") as file:
    st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

### END CONFIGURACIÓN DE PÁGINA

st.image(image1, caption='', use_column_width=True)

st.title("ANÁLISIS DEL PROGRAMA")

st.markdown("""<div class="justified">El Programa Municipal de Educación, Cultura y Ciudadanía Ambiental (EDUCCA), respaldado por la Política Nacional de Educación Ambiental y el Plan Nacional de Educación Ambiental, busca mejorar el conocimiento, el ejercicio de derechos y deberes, y promover cambios de comportamiento y buenas prácticas ambientales. Esto por medio de una acción coordinada, multisectorial y descentralizada, involucrando especialmente a las 196 municipalidades provinciales y las 1675 municipalidades distritales.<div>""", unsafe_allow_html=True)
st.write("\n")
st.image(image2, caption='', use_column_width=True)

st.markdown("""<div class="justified">El programa tiene como objetivo fomentar un cambio cultural en la población y en las instituciones, brindando una mejor educación ambiental a las instituciones, el sector privado, la sociedad civil y la población en general. Se presta especial atención a niñas, niños, adolescentes y jóvenes por peso demográfico y capacidad crítica, de innovación y aprendizaje, con el fin de mejorar la calidad de vida y lograr sociedades sostenibles.<div>""", unsafe_allow_html=True)
st.write("\n")

st.image(image3, caption='', use_column_width=True)

st.header('Base de Datos:')
st.write(df)

### PRIMER GRÁFICO

p1 = df[df['ANIO_INICIO_PME'] != 'NC']['ANIO_INICIO_PME'].value_counts().sort_index()

fig, ax = plt.subplots()
colors = plt.cm.Set2(range(len(p1)))

p1.plot(kind='bar', ax=ax, color=colors)

for i, v in enumerate(p1):
    ax.text(i, v + 1, str(v), ha='center', va='bottom', fontsize=8, color='black')

ax.set_xlabel('Año de Inicio')
ax.set_ylabel('Cantidad de Proyectos')
ax.set_title('Cantidad de Proyectos por Año de Inicio')

st.header('Cantidad de Proyectos por Año de Inicio')

col1, col2 = st.columns([1, 2])

with col1:
    st.write('Tabla:')
    st.dataframe(p1)

with col2:
    st.write("Gráfico:")
    st.pyplot(fig)

st.markdown("""<div class="justified">En el año 2023 el programa EDUCCA pudo instruirse en el mayor número de instituciones educativas que fue 384.<div>""", unsafe_allow_html=True)
st.write("\n")

### Líneas

p0 = p1.cumsum()

# Crear el gráfico de líneas acumulado con Matplotlib
fig, ax = plt.subplots()
ax.plot(p0.index, p0.values, marker='o', linestyle='-', color='g', label='Proyectos Acumulados')
ax.set_title('Cantidad Acumulada de Proyectos por Año de Inicio')
ax.set_xlabel('Año de Inicio')
ax.set_ylabel('Cantidad Acumulada de Proyectos')
ax.grid(True)
ax.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


st.markdown("""<div class="justified">Se puede apreciar en el gráfico que la mayor pendiente se encuentra del año 2022 a 2023 y la menor pendiente del año 2023 a 2024, esto último se puede deber a que aún no concluye el presente año 2024.<div>""", unsafe_allow_html=True)
st.write("\n")

### SEGUNDO GRÁFICO

state = st.selectbox('Seleccione el Departamento:', df['DEPARTAMENTO'].unique())
departamento = df[df['DEPARTAMENTO'] == state]

p2 = departamento[departamento['ANIO_INICIO_PME'] != 'NC']['ANIO_INICIO_PME'].value_counts().sort_index()

fig, ax = plt.subplots()
colors = plt.cm.Set2(range(len(p2)))

p2.plot(kind='bar', ax=ax, color=colors)

for i, v in enumerate(p2):
    ax.text(i, v, str(v), ha='center', va='bottom', fontsize=8, color='black')

ax.set_xlabel('Año de Inicio')
ax.set_ylabel('Cantidad de Proyectos')
ax.set_title(f'Cantidad de Proyectos por Año de Inicio en el departamento {state.title()}.')


st.header('Cantidad de Proyectos por Año de Inicio y Departamento')

col1, col2 = st.columns([1, 2])

with col1:
    st.write('Tabla:')
    st.dataframe(p2)

with col2:
    st.write("Gráfico:")
    st.pyplot(fig)

# Hallar mayor cantidad
mayor = p2.max()
anho = p2[p2 == mayor].keys()[0]

st.markdown(f"""<div class="justified">Se puede apreciar en el gráfico que la mayor cantidad de nuevas instituciones en las que se instruyó el programa EDUCCA en el departamento de {state} fue en el año {anho} con la cantidad de {mayor}.<div>""", unsafe_allow_html=True)
st.write("\n")
