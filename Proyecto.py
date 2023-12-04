import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import altair as alt

df = pd.read_excel(r'C:\Users\camil\Desktop\Base_de_datos\OPENDATA_DS_01_AFILIADOS.xlsx',header=0)
db=pd.read_csv(r'C:\Users\camil\Desktop\Base_de_datos\muestra2023.csv', encoding='latin1')
df1 = pd.read_csv(r'C:\Users\camil\Desktop\Base_de_datos\muestra2022.csv', encoding='latin1')
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
        options=["Inicio", "Muestra","Afiliados 2022", "Afiliados 2023"],
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
    st.title('RECUENTO DE GÉNERO POR REGIONES')
    
    conteo_sexos = df.groupby(['REGION', 'SEXO']).size().reset_index(name='Cantidad')
    chart = alt.Chart(conteo_sexos).mark_bar().encode(
        x='Cantidad:Q',
        y='REGION:N',
        color='SEXO:N',
        tooltip=['REGION', 'SEXO', 'Cantidad']
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
    st.title('MAPA DE AFILIADOS POR REGIONES')

    regiones = df['REGION'].unique().tolist()
    region_seleccionada = st.selectbox('Selecciona una región', regiones)
    df_filtrado = df[df['REGION'] == region_seleccionada]

    st.map(df_filtrado)
    cantidad_afiliados = df_filtrado.shape[0]
    st.write(f'La cantidad de personas afiliadas en la región {region_seleccionada} es: {cantidad_afiliados}')
    st.title('GRAFICO PORCENTUAL')
    conteo_ambito = df['AMBITO_INEI'].value_counts()


    plt.figure(figsize=(10,6))  
    conteo_ambito.plot.pie(autopct='%1.1f%%')
    st.pyplot(plt)



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
    
    st.title('Muestra de afiliados 2022')
    st.title('RECUENTO DE GÉNERO POR REGIONES')

    df1['REGION'] = df1['REGION'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')


    conteo_sexos = df1.groupby(['REGION', 'SEXO']).size().reset_index(name='Cantidad')

    chart = alt.Chart(conteo_sexos).mark_bar().encode(
            x='Cantidad:Q',
            y='REGION:N',
            color='SEXO:N',
            tooltip=['REGION', 'SEXO', 'Cantidad']
        ).interactive()

    st.altair_chart(chart, use_container_width=True)



    st.title('CANTIDAD TOTAL POR REGIÓN')  

    region_seleccionada = st.selectbox('Selecciona una región', df1['REGION'].unique())


    df_filtrado = df1[df1['REGION'] == region_seleccionada]

    cantidad_afiliados = df_filtrado.shape[0]
    st.write(f'La cantidad de personas afiliadas en la región {region_seleccionada} es: {cantidad_afiliados}')


    st.title('GRAFICO PORCENTUAL')
    conteo_ambito = df1['AMBITO_INEI'].value_counts()

        
    plt.figure(figsize=(10,6))  
    conteo_ambito.plot.pie(autopct='%1.1f%%')

        
    st.pyplot(plt)



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

    st.title('RECUENTO DE GÉNERO POR REGIONES')
    db['REGION'] = db['REGION'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')


    conteo_sexos = db.groupby(['REGION', 'SEXO']).size().reset_index(name='Cantidad')

    chart = alt.Chart(conteo_sexos).mark_bar().encode(
            x='Cantidad:Q',
            y='REGION:N',
            color='SEXO:N',
            tooltip=['REGION', 'SEXO', 'Cantidad']
        ).interactive()

    st.altair_chart(chart, use_container_width=True)

    st.title('MAPA DE AFILIADOS POR REGIÓN') 
    region_seleccionada = st.selectbox('Selecciona una región', db['REGION'].unique())

    df_filtrado = db[db['REGION'] == region_seleccionada]
    st.map(df_filtrado)
    cantidad_afiliados = df_filtrado.shape[0]
    st.write(f'La cantidad de personas afiliadas en la región {region_seleccionada} es: {cantidad_afiliados}')


    st.title('GRAFICO PORCENTUAL')
    conteo_ambito = db['AMBITO_INEI'].value_counts()

        
    plt.figure(figsize=(10,6))  
    conteo_ambito.plot.pie(autopct='%1.1f%%')

        
    st.pyplot(plt)