import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Variables relevantes
variables = ['Saldo_Mes_M1', 'dias_deudados_m1', 'Pago_M2', 'Variable_Objetivo_m2', 
             'L2_Saldo_Mes', 'Edad']

# Datos de ejemplo (debes reemplazar estos con tus datos reales)
clientes_data = {
    "Prestamo Personal": pd.DataFrame([
        {'Cliente': 'No Pagó', 'Saldo_Mes_M1': 8.68, 'dias_deudados_m1': -150, 'Pago_M2': 0,
         'Variable_Objetivo_m2': 0, 'L2_Saldo_Mes': 18315.08, 'Edad': 39, 'Segmento_ABC_B': 0, 'Segmento_ABC_C': 0,
         'Pago Real': 0},
        {'Cliente': 'Pagó menos del mínimo', 'Saldo_Mes_M1': 5547.5, 'dias_deudados_m1': 3, 'Pago_M2': 1913,
         'Variable_Objetivo_m2': 1, 'L2_Saldo_Mes': 23088.90, 'Edad': 36, 'Segmento_ABC_B': 0, 'Segmento_ABC_C': 0,
         'Pago Real': 1913},
        {'Cliente': 'Pagó mínimo o más', 'Saldo_Mes_M1': 4444.48, 'dias_deudados_m1': 4, 'Pago_M2': 1766,
         'Variable_Objetivo_m2': 1, 'L2_Saldo_Mes': 20779.07, 'Edad': 55, 'Segmento_ABC_B': 0, 'Segmento_ABC_C': 0,
         'Pago Real': 1766},
    ]),

    "TDC Departamental": pd.DataFrame([
        {'Cliente': 'No Pagó', 'Saldo_Mes_M1': 8562.92, 'dias_deudados_m1': -72, 'Pago_M2': 0,
         'Variable_Objetivo_m2': 0, 'L2_Saldo_Mes': 18053.07, 'Edad': 49, 'Segmento_ABC_B': 0, 'Segmento_ABC_C': 0,
         'Pago Real': 0},
        {'Cliente': 'Pagó menos del mínimo', 'Saldo_Mes_M1': 12163.54, 'dias_deudados_m1': 13, 'Pago_M2': 0,
         'Variable_Objetivo_m2': 0, 'L2_Saldo_Mes': 26855.49, 'Edad': 23, 'Segmento_ABC_B': 0, 'Segmento_ABC_C': 0,
         'Pago Real': 1000},
        {'Cliente': 'Pagó mínimo o más', 'Saldo_Mes_M1': 8913, 'dias_deudados_m1': 25, 'Pago_M2': 2000,
         'Variable_Objetivo_m2': 0, 'L2_Saldo_Mes': 26835.60, 'Edad': 37, 'Segmento_ABC_B': 0, 'Segmento_ABC_C': 0,
         'Pago Real': 2000},
    ]),
    
    "TDC Visa": pd.DataFrame([
        {'Cliente': 'No Pagó', 'Saldo_Mes_M1': 52290.60, 'dias_deudados_m1': -91, 'Pago_M2': 0,
         'Variable_Objetivo_m2': 0, 'L2_Saldo_Mes': 111700.33, 'Edad': 67, 'Segmento_ABC_B': 0, 'Segmento_ABC_C': 0,
         'Pago Real': 0},
        {'Cliente': 'Pagó menos del mínimo', 'Saldo_Mes_M1': 20074.84, 'dias_deudados_m1': 0, 'Pago_M2': 6693,
         'Variable_Objetivo_m2': 1, 'L2_Saldo_Mes': 89329.21, 'Edad': 34, 'Segmento_ABC_B': 0, 'Segmento_ABC_C': 0,
         'Pago Real': 6693},
        {'Cliente': 'Pagó mínimo o más', 'Saldo_Mes_M1': 34356.4, 'dias_deudados_m1': 24, 'Pago_M2': 4000,
         'Variable_Objetivo_m2': 1, 'L2_Saldo_Mes': 92743.40, 'Edad': 53, 'Segmento_ABC_B': 0, 'Segmento_ABC_C': 0,
         'Pago Real': 4000},
    ])           # Llena con datos similares
}

# Predicciones precomputadas
predicciones_modelos = {
    "Prestamo Personal": {
        "No Pagó": {'Random Forest': 0, 'Red Neuronal': 0, 'Bayesiano': "(-679.4, 1421.2)"},
        "Pagó menos del mínimo": {'Random Forest': 1865.9381, 'Red Neuronal': 0, 'Bayesiano': "(-777.5, 1361.5)"},
        "Pagó mínimo o más": {'Random Forest': 1578.56, 'Red Neuronal': 1, 'Bayesiano': "(-764.7, 1343.3)"},
    },
    "TDC Departamental": {
        "No Pagó": {'Random Forest': 0, 'Red Neuronal': 0, 'Bayesiano': "(-652.4, 1461.9)"},
        "Pagó menos del mínimo": {'Random Forest': 1558.3595, 'Red Neuronal': 0, 'Bayesiano': "(-749.4, 1388.4)"},
        "Pagó mínimo o más": {'Random Forest': 1947.2876, 'Red Neuronal': 1, 'Bayesiano': "(-724.4, 1380.5)"},
    },
    "TDC Visa": {
        "No Pagó": {'Random Forest': 0, 'Red Neuronal': 0, 'Bayesiano': "(-833.2, 1106.8)"},
        "Pagó menos del mínimo": {'Random Forest': 6097.7121, 'Red Neuronal': 0, 'Bayesiano': "(-757.9, 1131.9)"},
        "Pagó mínimo o más": {'Random Forest': 3865.0161, 'Red Neuronal': 1, 'Bayesiano': "(-627.21, 1293.7)"},
    }
}


def main():

    # Esconder menú de streamlit
    st.set_page_config(page_title="CobraSmart", page_icon='logo.png')
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # ------- Empieza sidebar --------

    with st.sidebar:
        st.image('logo_sidebar.png')
        st.page_link("main.py", label="Regresar a Inicio", icon="🏠")
        st.page_link("pages/scope.py", label="Enfoque del proyecto", icon="🎯")
        st.page_link("pages/predict.py", label="Predecir (simulador)", icon="📈")
    # ------- Termina sidebar --------

    # 1. Selección de producto
    producto_seleccionado = st.selectbox("Selecciona el producto a comparar:", list(clientes_data.keys()))
    df = clientes_data[producto_seleccionado]

    # 2. Comparación gráfica
    st.subheader("Comparación visual de clientes")
    var_seleccionada = st.selectbox("Selecciona la variable para comparar:", variables)

    # Transformar para que se adapte a st.bar_chart
    single_sol = df[['Cliente', var_seleccionada]].rename(columns={var_seleccionada: 'Valor'})

    # Gráfica con streamlit
    st.bar_chart(single_sol, x='Cliente', y='Valor', horizontal = True,color='#000000')

    # 3. Tabla con predicciones
    st.subheader("Predicciones de modelos y pago real")
    tabla_resultados = df[['Cliente', 'Pago Real']].copy()

    # Agregar predicciones
    for modelo in ['Random Forest', 'Red Neuronal', 'Bayesiano']:
        tabla_resultados[modelo] = tabla_resultados['Cliente'].apply(
            lambda c: predicciones_modelos[producto_seleccionado][c][modelo]
        )

    st.dataframe(tabla_resultados.set_index("Cliente"))

    # 4. Explicación opcional
    with st.expander("ℹ️ ¿Qué estás viendo?"):
        st.markdown("""
        - **Clientes** con comportamientos distintos: uno que no paga, otro que paga poco y otro que cumple.
        - Se comparan con **variables clave** de comportamiento financiero.
        - Las predicciones provienen de tres modelos ya entrenados: Random Forest, Red Neuronal y un modelo Bayesiano.
        - El modelo Bayesiano predice un intervalo de credibilidad dentro del cual se encuentra el pago del cliente.
        - También se muestra el **pago real** para validar el desempeño del modelo.
        """)

if __name__ == '__main__':
    main()