# 🧠 CobraSmart — Predicción de pagos en clientes de banca

CobraSmart es una herramienta interactiva diseñada para ayudar a instituciones financieras a **predecir cuánto pagará un cliente en el próximo mes** con base en su historial de pagos, saldos, edad y segmento ABC.  

La aplicación permite comparar modelos de machine learning, simular pagos, y visualizar gráficamente resultados clave, todo desde una interfaz simple e intuitiva desarrollada con **Streamlit**.

---

## 🚀 ¿Cómo funciona?

CobraSmart sigue estos pasos:

1. **Segmentación de clientes** con base en el principio ABC (A = cartera más importante, C = clientes pequeños).
2. **Entrenamiento de modelos** para predecir el pago mensual:  
   - `Pago_M1` → pago esperado en el próximo mes.
3. **Comparación entre tres modelos predictivos:**
   - 🌲 Random Forest  
   - 🧠 Red Neuronal  
   - 📊 Modelo Bayesiano
4. **Visualización y simulación** para apoyar decisiones de cobranza y exploración de cartera.

---

## 🗂️ Estructura del repositorio
```
📁 CobraSmart/
├── .streamlit/
│ └── config.toml # Configuración del tema e ícono de la app
│
├── modelos/
│ ├── RF_PP_light.pkl # Modelo Random Forest para Préstamos Personales
│ ├── RF_TDC_D_light.pkl # Modelo RF para TDC Dept
│ └── RF_TDC_V_light.pkl # Modelo RF para TDC Visa
│
├── pages/
│ ├── compare.py # Página para comparar los 3 modelos y clientes
│ ├── predict.py # Página de simulación para predicciones
│ └── scope.py # Página que describe el enfoque del proyecto
│
├── PP_ABC.png # Imagen usada para visualización de segmentos
├── logo.PNG # Logo principal
├── logo_sidebar.png # Logo para la barra lateral
├── main.py # Página principal de bienvenida
├── requirements.txt # Librerías necesarias para correr la app
└── README.md # Este archivo
```

---

## 💻 Tecnologías empleadas

| Herramienta         | Uso principal                                      |
|---------------------|----------------------------------------------------|
| **Python**          | Lenguaje principal del backend                     |
| **Streamlit**       | Creación de la interfaz web interactiva            |
| **scikit-learn**    | Entrenamiento de modelos como Random Forest        |
| **Keras / TensorFlow** | Red neuronal para regresión                       |
| **R / Rstudio** | Modelos bayesianos   |
| **Pandas & NumPy**  | Manipulación de datos                              |

---

## 🧾 Licencia
Este proyecto está bajo la Licencia MIT — consulta el archivo LICENSE para más información.

---
## ✍️ Autoras/Autores
* Santiago Mora Cruz
* Gabriel Eduardo Meléndez Zavala
* Melanie Astrid Montaño Ramos
* Victoria González González
* María Fernanda Gamboa Martínez

> Estudiantes de Ingeniería en Ciencia de Datos y Matemáticas.
