import streamlit as st

# Título de la app
st.title("Conversor Universal")

# Selección de categoría
categorias = [
    "Temperatura", "Longitud", "Peso/Masa", "Volumen",
    "Tiempo", "Velocidad", "Área", "Energía", 
    "Presión", "Tamaño de Datos"
]
categoria_seleccionada = st.sidebar.selectbox("Selecciona una categoría", categorias)

# Convertir según la categoría seleccionada
if categoria_seleccionada == "Temperatura":
    conversiones_temperatura = ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_temperatura)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Celsius a Fahrenheit":
        resultado = convertir_temperatura(valor, "Celsius", "Fahrenheit")
        st.write(f"{valor} °C son {resultado:.2f} °F")

    elif conversion_seleccionada == "Fahrenheit a Celsius":
        resultado = convertir_temperatura(valor, "Fahrenheit", "Celsius")
        st.write(f"{valor} °F son {resultado:.2f} °C")

    elif conversion_seleccionada == "Celsius a Kelvin":
        resultado = convertir_temperatura(valor, "Celsius", "Kelvin")
        st.write(f"{valor} °C son {resultado:.2f} K")

    elif conversion_seleccionada == "Kelvin a Celsius":
        resultado = convertir_temperatura(valor, "Kelvin", "Celsius")
        st.write(f"{valor} K son {resultado:.2f} °C")

    pass

elif categoria_seleccionada == "Longitud":
    # Conversión de longitud
    conversiones_longitud = ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_longitud)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Pies a metros":
        resultado = convertir_longitud(valor, "pies", "metros")
        st.write(f"{valor} pies son {resultado:.4f} metros")

    elif conversion_seleccionada == "Metros a pies":
        resultado = convertir_longitud(valor, "metros", "pies")
        st.write(f"{valor} metros son {resultado:.4f} pies")

    elif conversion_seleccionada == "Pulgadas a centímetros":
        resultado = convertir_longitud(valor, "pulgadas", "metros") * 100
        st.write(f"{valor} pulgadas son {resultado:.4f} centímetros")

    elif conversion_seleccionada == "Centímetros a pulgadas":
        resultado = convertir_longitud(valor, "metros", "pulgadas") / 100
        st.write(f"{valor} centímetros son {resultado:.4f} pulgadas")

    pass

elif categoria_seleccionada == "Peso/Masa":
    # Conversión de peso/masa
    conversiones_peso = ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_peso)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Libras a kilogramos":
        resultado = convertir_peso(valor, "libras", "kilogramos")
        st.write(f"{valor} libras son {resultado:.4f} kilogramos")

    elif conversion_seleccionada == "Kilogramos a libras":
        resultado = convertir_peso(valor, "kilogramos", "libras")
        st.write(f"{valor} kilogramos son {resultado:.4f} libras")

    elif conversion_seleccionada == "Onzas a gramos":
        resultado = convertir_peso(valor, "onzas", "gramos")
        st.write(f"{valor} onzas son {resultado:.4f} gramos")

    elif conversion_seleccionada == "Gramos a onzas":
        resultado = convertir_peso(valor, "gramos", "onzas")
        st.write(f"{valor} gramos son {resultado:.4f} onzas")

    pass

elif categoria_seleccionada == "Volumen":
    # Conversión de volumen
    conversiones_volumen = ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_volumen)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Galones a litros":
        resultado = convertir_volumen(valor, "galones", "litros")
        st.write(f"{valor} galones son {resultado:.4f} litros")

    elif conversion_seleccionada == "Litros a galones":
        resultado = convertir_volumen(valor, "litros", "galones")
        st.write(f"{valor} litros son {resultado:.4f} galones")

    elif conversion_seleccionada == "Pulgadas cúbicas a centímetros cúbicos":
        resultado = convertir_volumen(valor, "pulgadas cúbicas", "metros cúbicos") * 1e6
        st.write(f"{valor} pulgadas cúbicas son {resultado:.4f} centímetros cúbicos")

    elif conversion_seleccionada == "Centímetros cúbicos a pulgadas cúbicas":
        resultado = convertir_volumen(valor, "metros cúbicos", "pulgadas cúbicas") * 1e-6
        st.write(f"{valor} centímetros cúbicos son {resultado:.4f} pulgadas cúbicas")

    pass

elif categoria_seleccionada == "Tiempo":
    # Conversión de tiempo
    conversiones_tiempo = ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_tiempo)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Horas a minutos":
        resultado = valor * 60
        st.write(f"{valor} horas son {resultado:.4f} minutos")

    elif conversion_seleccionada == "Minutos a segundos":
        resultado = valor * 60
        st.write(f"{valor} minutos son {resultado:.4f} segundos")

    elif conversion_seleccionada == "Días a horas":
        resultado = valor * 24
        st.write(f"{valor} días son {resultado:.4f} horas")

    elif conversion_seleccionada == "Semanas a días":
        resultado = valor * 7
        st.write(f"{valor} semanas son {resultado:.4f} días")

    pass

elif categoria_seleccionada == "Velocidad":
    # Conversión de velocidad
    conversiones_velocidad = ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_velocidad)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Millas por hora a kilómetros por hora":
        resultado = valor * 1.60934
        st.write(f"{valor} millas por hora son {resultado:.4f} kilómetros por hora")

    elif conversion_seleccionada == "Kilómetros por hora a metros por segundo":
        resultado = valor * 0.277778
        st.write(f"{valor} kilómetros por hora son {resultado:.4f} metros por segundo")

    elif conversion_seleccionada == "Nudos a millas por hora":
        resultado = valor * 1.15078
        st.write(f"{valor} nudos son {resultado:.4f} millas por hora")

    elif conversion_seleccionada == "Metros por segundo a pies por segundo":
        resultado = valor * 3.28084
        st.write(f"{valor} metros por segundo son {resultado:.4f} pies por segundo")

    pass

elif categoria_seleccionada == "Área":
    # Conversión de área
    conversiones_area = ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_area)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Metros cuadrados a pies cuadrados":
        resultado = valor * 10.7639
        st.write(f"{valor} metros cuadrados son {resultado:.4f} pies cuadrados")

    elif conversion_seleccionada == "Pies cuadrados a metros cuadrados":
        resultado = valor * 0.092903
        st.write(f"{valor} pies cuadrados son {resultado:.4f} metros cuadrados")

    elif conversion_seleccionada == "Kilómetros cuadrados a millas cuadradas":
        resultado = valor * 0.386102
        st.write(f"{valor} kilómetros cuadrados son {resultado:.4f} millas cuadradas")

    elif conversion_seleccionada == "Millas cuadradas a kilómetros cuadrados":
        resultado = valor * 2.58999
        st.write(f"{valor} millas cuadradas son {resultado:.4f} kilómetros cuadrados")

    pass

elif categoria_seleccionada == "Energía":
    conversiones_energia = ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_energia)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Julios a calorías":
        resultado = valor * 0.239006
        st.write(f"{valor} julios son {resultado:.4f} calorías")

    elif conversion_seleccionada == "Calorías a kilojulios":
        resultado = valor * 0.004184
        st.write(f"{valor} calorías son {resultado:.4f} kilojulios")

    elif conversion_seleccionada == "Kilovatios-hora a megajulios":
        resultado = valor * 3.6
        st.write(f"{valor} kilovatios-hora son {resultado:.4f} megajulios")

    elif conversion_seleccionada == "Megajulios a kilovatios-hora":
        resultado = valor * 0.277778
        st.write(f"{valor} megajulios son {resultado:.4f} kilovatios-hora")

    pass

elif categoria_seleccionada == "Presión":
    # Conversión de presión:
    conversiones_presion = ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_presion)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Pascales a atmósferas":
        resultado = valor * 9.86923e-6
        st.write(f"{valor} pascales son {resultado:.10f} atmósferas")

    elif conversion_seleccionada == "Atmósferas a pascales":
        resultado = valor * 101325
        st.write(f"{valor} atmósferas son {resultado:.4f} pascales")

    elif conversion_seleccionada == "Barras a libras por pulgada cuadrada":
        resultado = valor * 14.5038
        st.write(f"{valor} barras son {resultado:.4f} libras por pulgada cuadrada")

    elif conversion_seleccionada == "Libras por pulgada cuadrada a bares":
        resultado = valor * 0.0689476
        st.write(f"{valor} libras por pulgada cuadrada son {resultado:.4f} bares")

    pass

elif categoria_seleccionada == "Tamaño de Datos":
    # Conversión de tamaño de datos
    conversiones_datos = ["Megabytes a gigabytes", "Gigabytes a terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_datos)
    valor = st.number_input("Ingresa el valor", value=0.0)

    if conversion_seleccionada == "Megabytes a gigabytes":
        resultado = valor * 0.001
        st.write(f"{valor} megabytes son {resultado:.6f} gigabytes")

    elif conversion_seleccionada == "Gigabytes a terabytes":
        resultado = valor * 0.001
        st.write(f"{valor} gigabytes son {resultado:.6f} terabytes")

    elif conversion_seleccionada == "Kilobytes a megabytes":
        resultado = valor * 0.001
        st.write(f"{valor} kilobytes son {resultado:.6f} megabytes")

    elif conversion_seleccionada == "Terabytes a petabytes":
        resultado = valor * 0.001
        st.write(f"{valor} terabytes son {resultado:.6f} petabytes")

    pass
