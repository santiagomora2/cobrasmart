import streamlit as st

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
        st.page_link("pages/compare.py", label="Comparar Modelos", icon="⚖️")
        st.page_link("pages/predict.py", label="Predecir (simulador)", icon="📈")
    # ------- Termina sidebar --------

    st.markdown('# Enfoque del Proyecto')

    # Objetivos

    st.markdown('### 🎯 Objetivos')

    st.markdown("""
    El objetivo principal de **CobraSmart** es ayudar a las instituciones financieras a **anticipar el comportamiento de pago** de sus clientes.  


    Buscamos:
    - **Segmentar la cartera de clientes** por productos y grupos.
    - Construir modelos predictivos para **predecir cuánto pagará cada cliente** y comparar estos modelos.
    - Generar **estrategias de cobranza** basado en el segmento y predicción de cada cliente, para facilitar la recuperación de deuda de la institución.
    - Crear una **interfaz clara** que permita a cualquier analista explorar los resultados.  

    Para lograrlo, segmentamos a los clientes usando **segmentación ABC**, desarrollamos modelos de machine learning capaces de **predecir cuánto pagará un cliente en un mes dado**, con base en información histórica de pagos, saldos, edades y segmentos.
    """)

    # Teoría

    st.markdown('### 📚 Teoría')

    st.markdown('##### Segmentación')

    st.markdown(r"""
    El principio básico de la segmentación ABC es que el **80% de la deuda** de los clientes esta **representada por el 20% de los clientes**, a este segmento corresponde la letra 'A'
    , mientras que la letra 'B', representa aproximadamente del 10 al **15% de la deuda**, por lo tanto el resto corresponde a la letra 'C', en donde comúnmente se encuentran la 
    mayoría de los clientes. 
    """)

    st.markdown('##### Predicción')

    st.markdown("""
    Este proyecto se apoya en modelos de **regresión supervisada** que buscan predecir el **pago en un mes del cliente**:  
    > `Pago_M1 = ` pago del cliente en el mes actual.

    Los modelos utilizados son:
    - **Random Forest:** modelo de árboles de decisión que combina múltiples árboles para mejorar la precisión.""")

    with st.expander('Ventajas/desventajas'):
        st.markdown("""
        **Ventajas**
        - Modelo simple, no lineal y resistente a *overfitting*.               
        - Permite ver las *features* más importantes para predecir.
                    
        **Desventajas**
        - Limitado para relaciones muy complejas.
        - Puede quedar corto frente a arquitecturas más potentes como redes neuronales.
        """)

    st.markdown("""- **Red Neuronal:** una arquitectura básica capaz de aprender patrones complejos no lineales.""")
                
    with st.expander('Ventajas/desventajas'):
        st.markdown("""
        **Ventajas**
        - Detecta patrones complejos y relaciones no lineales entre las variables.
        - Se puede adaptar para tareas más avanzadas con arquitecturas más profundas o especializadas.
                    
        **Desventajas**
        - Modelo de caja negra, no tiene mucha interpretabilidad.
        - Requiere muchos recursos computacionales para correr.
        """)

    st.markdown("""- **Modelo Bayesiano:** clasificador probabilístico basado en la Teoría de Bayes.""")


    with st.expander('Ventajas/desventajas'):
        st.markdown("""
        **Ventajas**
        - Modelo probabilístico, proporciona intervalo de credibilidad.
        - Se pueden calcular *point estimates* con distribuciones de probabilidad.
        - Se puede incorporar conocimiento a priori.   
                                
        **Desventajas**
        - Requiere muchos recursos computacionales para correr.
        - Poco interpretable.
        """)

    # Resultados

    st.markdown('### 📊 Resultados')

    st.write("""
    Logramos **segmentar a los clientes** de una forma efectiva e informativa para una institución financiera, así como generar 
    **modelos predictivos** con métricas $R^2$ mayores a $0.80$ en todos los casos y con ventajas y desventajas para cada modelo. 
    Esto nos permitió ayudar a la institución a **desarrollar estrategias de cobranza efectivas** y a recuperar un mayor porcentaje de deuda.
    """)

    st.image('PP_ABC.png',width = 500 ,caption='Segmentación ABC para clientes que cuentan con prestamos personales')



if __name__ == '__main__':
    main()
