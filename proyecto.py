import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from streamlit_option_menu import option_menu

df = pd.read_excel(r'OPENDATA_DS_01_AFILIADOS.xlsx',header=0)
page_img="""
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://img.freepik.com/fotos-premium/interior-borroso-hospital-o-clinica-personas_1484-2139.jpg?size=626&ext=jpg");
background-size:cover;
background-repeat: no-repeat;
background-position: center
}
[data-testid="stHeader"]{
background-color:rgba(0,0,0,0);}

[data-testid="stSidebarContent"]{
background-image: url("https://hispaniaceramica.com/wp-content/uploads/2021/09/Pastel-Gris-es-2Wcx6KZ4GU8A4Wrc.jpg");
background-size:cover;
}
.sidebar-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        color:red;
    }
    .sidebar-content img {
        max-width: 300px;
        margin-top: -100px; 
    }

</style>
"""
url_l="https://ciencias.cayetano.edu.pe/wp-content/uploads/sites/28/2023/05/ciencias-e-ingenieria-oficial.png"
st.sidebar.markdown(page_img, unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-content'><img src='%s'></div>" % url_l, unsafe_allow_html=True)
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
with st.sidebar:
    selected=option_menu(
        menu_title="Selecionar",
        options=["Inicio","Grafico Mapa","Pastel"],
        icons=["bar-chart-fill","map","circle-half"],
        menu_icon="compass",
        styles={
            "container":{"padding":"5!important","background-color":'white'},
            "icon": {"color": "black", "font-size": "23px"},

            "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#ff6961"},
            "nav-link-selected": {"background-color": '#e57d56'},
        }

    )
if selected=="Inicio":
    plt.style.use('ggplot')

    st.title('Recuento de Géneros por Región')

    # Desapilar el DataFrame
    conteo_sexos = df.groupby(['REGION', 'SEXO']).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(9, 14))

    # Crear un gráfico de barras con colores específicos y agregar una leyenda
    conteo_sexos.plot(kind='barh', color={'FEMENINO': 'blue', 'MASCULINO': 'red'}, ax=ax)

    plt.title('')
    plt.ylabel('Región')
    plt.xlabel('Cantidad')

    # Agregar una leyenda
    plt.legend(['Femenino', 'Masculino'])

    st.pyplot(fig)

if selected=="Grafico Mapa":
    pages="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://img.freepik.com/foto-gratis/borrosa-resumen-antecedentes-vista-interior-mirando-fuera-vacio-vestibulo-oficina-puertas-entrada-pared-cortina-vidrio-marco_1339-6363.jpg?size=626&ext=jpg&ga=GA1.1.365413683.1700965736&semt=ais");
    background-size:cover;
    background-repeat: no-repeat;
    background-position: center
    }
    </style>
    """
    st.sidebar.markdown(pages, unsafe_allow_html=True)

    st.title('MAPA')
    # Crear una lista de las regiones únicas en el DataFrame
    regiones = df['REGION'].unique().tolist()

    # Crear un selectbox para seleccionar una región
    region_seleccionada = st.selectbox('Selecciona una región', regiones)

    # Filtrar el DataFrame para obtener solo los datos de la región seleccionada
    df_filtrado = df[df['REGION'] == region_seleccionada]

    # Crear un mapa con los datos de la región seleccionada
    st.map(df_filtrado)

if selected=="Pastel":
    page="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://img.freepik.com/foto-gratis/blur-hospital_1203-7957.jpg?size=626&ext=jpg&ga=GA1.1.365413683.1700965736&semt=ais");
    background-size:cover;
    background-repeat: no-repeat;
    background-position: center
    }
    </style>
    """


    st.sidebar.markdown(page, unsafe_allow_html=True)
    st.title('PASTEL')
    conteo_ambito = df['AMBITO_INEI'].value_counts()

    # Crear un gráfico de pastel
    plt.figure(figsize=(10,6))  # Ajustar el tamaño del gráfico
    conteo_ambito.plot.pie(autopct='%1.1f%%')

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)