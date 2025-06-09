import streamlit as st
import pandas as pd
import joblib

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
        st.page_link("pages/compare.py", label="Comparar Modelos", icon="⚖️")

    # ------- Termina sidebar --------


    # Título principal
    st.title("Predicción de Pago para Clientes de Tarjetas de Crédito")

    # Descripción breve del simulador
    with st.expander("🧾 Descripción breve del simulador", expanded=True):
        st.write("""
        Esta aplicación te permite predecir el pago de un cliente simulado en distintos productos financieros 
        como préstamos personales o tarjetas de crédito. Ingresa los valores de comportamiento y demográficos del cliente, 
        selecciona el segmento correspondiente y obtén una predicción utilizando modelos de aprendizaje automático entrenados previamente.
        """)

    # Selección de producto
    producto = st.selectbox("Selecciona el producto:", 
                            ["Prestamo Personal", "TDC Departamental", "TDC Visa"])

    # Variables light
    light_variables = ['Saldo_Mes_M1', 'Saldo_Mes_M2', 'dias_deudados_m1', 'dias_deudados_m2', 
                    'Pago_M2' ,'Variable_Objetivo_m2', 'L2_Saldo_Mes', 'Edad']

    # Segmentos codificados
    segmento_col_b = 'Segmento_ABC_B'
    segmento_col_c = 'Segmento_ABC_C'

    # Configuración de sliders
    variable_config = {
        'Saldo_Mes_M1': {'min': 0, 'max': 100000, 'default': 2000, 'desc': 'Saldo del mes de la predicción'},
        'Saldo_Mes_M2': {'min': 0, 'max': 100000, 'default': 5000, 'desc': 'Saldo del mes anterior a la predicción'},
        'dias_deudados_m1': {'min': -90, 'max': 0, 'default': -7, 'desc': 'Días que el cliente ha estado en el mes de predicción'},
        'dias_deudados_m2': {'min': -90, 'max': 0, 'default': -4, 'desc': 'Días que el cliente ha estado en el mes anterior a la predicción'},
        'Pago_M2': {'min': 0, 'max': 60000, 'default': 5000, 'desc': 'Pago realizado el mes anterior a la predicción '},
        'Variable_Objetivo_m2': {'min': 0, 'max': 1, 'default': 0, 'desc': 'Si el cliente pagó más que el mínimo en el mes anterior a la predicción'},
        'L2_Saldo_Mes': {'min': 0, 'max': 250000, 'default': 8000, 'desc': 'Cuantificación del saldo del cliente'},
        'Edad': {'min': 18, 'max': 100, 'default': 48, 'desc': 'Edad del cliente'}
    }

    # Cachear modelos
    @st.cache_resource
    def load_models():
        modelos = {
            "Prestamo Personal": joblib.load("modelos/RF_PP_light.pkl"),
            "TDC Departamental": joblib.load("modelos/RF_TDC_D_light.pkl"),
            "TDC Visa": joblib.load("modelos/RF_TDC_V_light.pkl")
        }
        return modelos

    modelos = load_models()

    # Sliders en columnas
    col1, col2 = st.columns(2)
    input_data = {}

    with col1:
        for var in light_variables[:len(light_variables)//2]:
            config = variable_config[var]
            input_data[var] = st.slider(var, config['min'], config['max'], config['default'])
            st.caption(config['desc'])

    with col2:
        for var in light_variables[len(light_variables)//2:]:
            config = variable_config[var]
            input_data[var] = st.slider(var, config['min'], config['max'], config['default'])
            st.caption(config['desc'])

    # Segmento
    segmento = st.selectbox("Selecciona el segmento:", ["A", "B", "C"])
    input_data[segmento_col_b] = 1 if segmento == "B" else 0
    input_data[segmento_col_c] = 1 if segmento == "C" else 0

    # Mostrar datos ingresados
    df_input = pd.DataFrame([input_data])
    st.subheader("Valores seleccionados:")
    st.write(df_input)

    # Predicción
    if st.button("Predecir"):
        try:
            model = modelos[producto]
            prediction = model.predict(df_input)
            st.markdown(f"""
            <div style='
                background-color: #e8f0fe;
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.1);
            '>
                <h1 style='color: #1a73e8; font-size: 3rem;'>💰 ${prediction[0]:,.2f}</h1>
                <p style='font-size: 1.2rem;'>Este es el monto estimado que pagará el cliente</p>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error al predecir: {e}")

    # Explicación técnica al final
    with st.expander("🛠️ ¿Cómo funciona?", expanded=False):
        st.write("""
        El sistema utiliza modelos de *Random Forest* previamente entrenados para cada tipo de producto financiero. 
        Los modelos toman como entrada variables relacionadas al comportamiento financiero reciente del cliente (saldos, pagos, días en mora), 
        así como características demográficas (edad, segmento).

        La predicción resultante indica la cantidad que el cliente probablemente pagará en el siguiente período, 
        lo cual es útil para decisiones de crédito y riesgo.
        """)



if __name__ == '__main__':
    main()