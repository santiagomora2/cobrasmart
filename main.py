import streamlit as st
import streamlit.components.v1 as components

# página principal
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

    # Custom HTML with inline styling
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <style>
            /* Full-screen animated background */
            body {
                background-image: url('https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnAzYXdseGJncDgxdXF3eDhha2U1dHF3dDZqdDBsdGo1OWVwanF5MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JtBZm3Getg3dqxK0zP/giphy.gif');
                background-size: cover;
                background-attachment: fixed;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
            }

            /* Container for the title and divider */
            .container {
                position: relative;
                text-align: center;
                color: white;
                max-width: 1000px;
                width: 100%;
            }

            /* Horizontal divider line */
            .line {
                border-top: 2px solid white;
                width: 80%; /* Adjust width as needed */
                margin: 20px auto; /* Adds spacing above and below */
            }

            /* Big title text on top */
            .big-title {
                font-size: 50px;
                font-weight: bold;
                margin-bottom: 20px; /* Adds spacing below the title */
            }

            /* Small title text below */
            .small-title {
                font-size: 20px;
                margin-top: 20px; /* Adds spacing above the subtitle */
            }

        </style>
    </head>
    <body>
        <div class="container">
            <div class="big-title">CobraSmart</div>
            <div class="line"></div>
            <div class="small-title">Segmentación de clientes de productos financieros.</div>
        </div>
    </body>
    </html>

        """

    # Display the custom HTML in Streamlit
    components.html(html_code, height=350)

    cols = st.columns(3)
    with cols[0]:
        st.page_link("pages/scope.py", label="Enfoque del proyecto", icon="🎯")
    with cols[2]:
        st.page_link("pages/compare.py", label="Comparar Modelos", icon="⚖️")
        st.page_link("pages/predict.py", label="Predecir (simulador)", icon="📈")


if __name__ == '__main__':
    main()
