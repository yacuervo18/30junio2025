import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns


st.set_page_config(layout='centered', page_title='Talento Teche', page_icon=':smile:')

#TITULO DE LA PAGINA

t1,t2 =st.columns([0.3,0.7])
t1.image('Goku.png', width = 420)
t2.title('Tablero')
t2.markdown('*tel:* 123 | email: yedison.cuervo@streamlit.com',)

#SECCIONES
steps = st.tabs(['Pestaña', 'Pestaña 2', 'Pestaña $\sqrt{9}$'])
with steps[0]:
    camp_df=pd.read_csv('Campanhas.csv', encoding='latin-1', sep=';')
    camp=st.selectbox('Escoge un ID de campaña', camp_df['ID_Campana'], help='Muestra todas las campañas disponible ')

    met_df= pd.read_csv('Metricas.csv', encoding='latin-1', sep=';')
    st.dataframe(met_df)

    m1, m2, m3 = st.columns([1,1,1,])

    id1=met_df[(met_df['ID_Campana']== camp)]
    id2=met_df[met_df['ID_Campana']== camp]

    m1.write("Metricas filtradas")
    m1.metric(label='Metrica 1', value=sum(id1['Conversiones']),
              delta=str(sum(id1['Rebotes']))+'Numero de Rebotes', 
              delta_color='inverse')
    
    m2.metric(label= 'Metrica 2', value= np.mean(id1['Clics']),
              delta=str(np.mean(id1['Impresiones']))+'Número de rebotes', 
              delta_color='inverse')


    #Explorar nuevas graficas

    #Como publicamos nuestro streamlit
    
