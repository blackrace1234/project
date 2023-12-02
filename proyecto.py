import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import altair as alt

df = pd.read_excel(r'OPENDATA_DS_01_AFILIADOS.xlsx',header=0)
db=pd.read_csv(r'muestra2023.csv', encoding='latin1')
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
        options=["Inicio", "Muestra","Afiliados 2023","Afiliados 2022"],
        icons=["discord","bar-chart-fill","facebook","circle-half"],
        menu_icon="compass",
        styles={
            "container":{"padding":"5!important","background-color":'white'},
            "icon": {"color": "black", "font-size": "23px"}, 

            "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#ff6961"},
            "nav-link-selected": {"background-color": '#e57d56'},
        }

    )
if selected=="Inicio":
    st.title("Proximamente")


if selected=="Muestra":
    page="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://img.freepik.com/fotos-premium/fondo-abstracto-borrosa-fondo-sala-espacio-trabajo-moderno_834769-700.jpg");
    background-size:cover;
    background-repeat: no-repeat;
    background-position: center
    }
    </style>
    """
    st.sidebar.markdown(page, unsafe_allow_html=True)
    st.title('Muestra de afiliados')
    # Desapilar el DataFrame
    conteo_sexos = df.groupby(['REGION', 'SEXO']).size().reset_index(name='Cantidad')

    # Crear un gráfico de barras con Altair
    chart = alt.Chart(conteo_sexos).mark_bar().encode(
        x='Cantidad:Q',
        y='REGION:N',
        color='SEXO:N',
        tooltip=['REGION', 'SEXO', 'Cantidad']
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
    st.title('PASTEL')
    conteo_ambito = df['AMBITO_INEI'].value_counts()

    # Crear un gráfico de pastel
    plt.figure(figsize=(10,6))  # Ajustar el tamaño del gráfico
    conteo_ambito.plot.pie(autopct='%1.1f%%')

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)
    st.title('MAPA')
    # Crear una lista de las regiones únicas en el DataFrame
    regiones = df['REGION'].unique().tolist()

    # Crear un selectbox para seleccionar una región
    region_seleccionada = st.selectbox('Selecciona una región', regiones)

    # Filtrar el DataFrame para obtener solo los datos de la región seleccionada
    df_filtrado = df[df['REGION'] == region_seleccionada]

    # Crear un mapa con los datos de la región seleccionada
    st.map(df_filtrado)
    


if selected=="Afiliados 2022":
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
    st.title("Proximamente")



if selected=="Afiliados 2023":
    page="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://media.istockphoto.com/id/472336288/es/foto/desenfocada-fondo-de-la-zona-de-oficina-abierta.jpg?s=612x612&w=0&k=20&c=pjsuNe8K8-MvW9_N5yODQAiFwRZBpLu-PZv_9mBw9IE=");
    background-size:cover;
    background-repeat: no-repeat;
    background-position: center
    }
    </style>
    """
    st.sidebar.markdown(page, unsafe_allow_html=True)
    st.title('Muestra de afiliados 2023')
     # Normalizar los caracteres de la columna 'REGION'
    st.title('Recuento de Géneros por Región')
    # Normalizar los caracteres de la columna 'REGION'
    db['REGION'] = db['REGION'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

        # Calcular el recuento de género por región
    conteo_sexos = db.groupby(['REGION', 'SEXO']).size().reset_index(name='Cantidad')

        # Crear un gráfico de barras interactivo con Altair
    chart = alt.Chart(conteo_sexos).mark_bar().encode(
            x='Cantidad:Q',
            y='REGION:N',
            color='SEXO:N',
            tooltip=['REGION', 'SEXO', 'Cantidad']
        ).interactive()
        # Mostrar el gráfico de barras interactivo
    st.altair_chart(chart, use_container_width=True)


        # Crear un mapa con los datos de la región seleccionada
    st.title('Mapa de las regiones')  # Añadir título al mapa
        # Crear un select box para seleccionar una región
    region_seleccionada = st.selectbox('Selecciona una región', db['REGION'].unique())

        # Filtrar el DataFrame para obtener solo los datos de la región seleccionada
    df_filtrado = db[db['REGION'] == region_seleccionada]
    st.map(df_filtrado)
        # Mostrar la cantidad de personas afiliadas en la región seleccionada
    cantidad_afiliados = df_filtrado.shape[0]
    st.write(f'La cantidad de personas afiliadas en la región {region_seleccionada} es: {cantidad_afiliados}')


    st.title('PASTEL')
    conteo_ambito = db['AMBITO_INEI'].value_counts()

        
    plt.figure(figsize=(10,6))  
    conteo_ambito.plot.pie(autopct='%1.1f%%')

        
    st.pyplot(plt)
