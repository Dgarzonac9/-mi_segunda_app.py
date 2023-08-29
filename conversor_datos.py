import streamlit as st

def convertir_temperatura(valor, escala_origen, escala_destino):
    if escala_origen == "Celsius":
        if escala_destino == "Fahrenheit":
            resultado = (valor * 9/5) + 32
            return resultado
        elif escala_destino == "Kelvin":
            resultado = valor + 273.15
            return resultado
    
    elif escala_origen == "Fahrenheit":
        if escala_destino == "Celsius":
            resultado = (valor - 32) * 5/9
            return resultado
        elif escala_destino == "Kelvin":
            resultado = (valor + 459.67) * 5/9
            return resultado

    elif escala_origen == "Kelvin":
        if escala_destino == "Celsius":
            resultado = valor - 273.15
            return resultado
        elif escala_destino == "Fahrenheit":
            resultado = (valor * 9/5) - 459.67
            return resultado

    pass

def convertir_longitud(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Pies" and unidad_destino == "Metros":
        resultado = valor * 0.3048
        return resultado
    elif unidad_origen == "Metros" and unidad_destino == "Pies":
        resultado = valor / 0.3048
        return resultado
    elif unidad_origen == "Pulgadas" and unidad_destino == "Centímetros":
        resultado = valor * 2.54
        return resultado
    elif unidad_origen == "Centímetros" and unidad_destino == "Pulgadas":
        resultado = valor / 2.54
        return resultado


def convertir_peso(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Libras" and unidad_destino == "Kilogramos":
        resultado = valor * 0.453592
        return resultado
    elif unidad_origen == "Kilogramos" and unidad_destino == "Libras":
        resultado = valor / 0.453592
        return resultado
    elif unidad_origen == "Onzas" and unidad_destino == "Gramos":
        resultado = valor * 28.3495
        return resultado
    elif unidad_origen == "Gramos" and unidad_destino == "Onzas":
        resultado = valor / 28.3495
        return resultado


def convertir_volumen(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Galones" and unidad_destino == "Litros":
        resultado = valor * 3.78541
        return resultado
    elif unidad_origen == "Litros" and unidad_destino == "Galones":
        resultado = valor / 3.78541
        return resultado
    elif unidad_origen == "Pulgadas cúbicas" and unidad_destino == "Centímetros cúbicos":
        resultado = valor * 16.3871
        return resultado
    elif unidad_origen == "Centímetros cúbicos" and unidad_destino == "Pulgadas cúbicas":
        resultado = valor / 16.3871
        return resultado


def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Horas" and unidad_destino == "Minutos":
        resultado = valor * 60
        return resultado
    elif unidad_origen == "Minutos" and unidad_destino == "Segundos":
        resultado = valor * 60
        return resultado
    elif unidad_origen == "Días" and unidad_destino == "Horas":
        resultado = valor * 24
        return resultado
    elif unidad_origen == "Semanas" and unidad_destino == "Días":
        resultado = valor * 7
        return resultado


def convertir_velocidad(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Millas por hora" and unidad_destino == "Kilómetros por hora":
        resultado = valor * 1.60934
        return resultado
    elif unidad_origen == "Kilómetros por hora" and unidad_destino == "Metros por segundo":
        resultado = valor * 0.277778
        return resultado
    elif unidad_origen == "Nudos" and unidad_destino == "Millas por hora":
        resultado = valor * 1.15078
        return resultado
    elif unidad_origen == "Metros por segundo" and unidad_destino == "Pies por segundo":
        resultado = valor * 3.28084
        return resultado


def convertir_area(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Metros cuadrados" and unidad_destino == "Pies cuadrados":
        resultado = valor * 10.7639
        return resultado
    elif unidad_origen == "Pies cuadrados" and unidad_destino == "Metros cuadrados":
        resultado = valor * 0.092903
        return resultado
    elif unidad_origen == "Kilómetros cuadrados" and unidad_destino == "Millas cuadradas":
        resultado = valor * 0.386102
        return resultado
    elif unidad_origen == "Millas cuadradas" and unidad_destino == "Kilómetros cuadrados":
        resultado = valor * 2.58999
        return resultado


def convertir_energia(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Julios" and unidad_destino == "Calorías":
        resultado = valor * 0.239006
        return resultado
    elif unidad_origen == "Calorías" and unidad_destino == "Kilojulios":
        resultado = valor * 0.004184
        return resultado
    elif unidad_origen == "Kilovatios-hora" and unidad_destino == "Megajulios":
        resultado = valor * 3.6
        return resultado
    elif unidad_origen == "Megajulios" and unidad_destino == "Kilovatios-hora":
        resultado = valor * 0.277778
        return resultado


def convertir_presion(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Pascales" and unidad_destino == "Atmósferas":
        resultado = valor * 9.86923e-6
        return resultado
    elif unidad_origen == "Atmósferas" and unidad_destino == "Pascales":
        resultado = valor * 101325
        return resultado
    elif unidad_origen == "Barras" and unidad_destino == "Libras por pulgada cuadrada":
        resultado = valor * 14.5038
        return resultado
    elif unidad_origen == "Libras por pulgada cuadrada" and unidad_destino == "Bares":
        resultado = valor * 0.0689476
        return resultado


def convertir_tamano_datos(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Megabytes" and unidad_destino == "Gigabytes":
        resultado = valor * 0.001
        return resultado
    elif unidad_origen == "Gigabytes" and unidad_destino == "Terabytes":
        resultado = valor * 0.001
        return resultado
    elif unidad_origen == "Kilobytes" and unidad_destino == "Megabytes":
        resultado = valor * 0.001
        return resultado
    elif unidad_origen == "Terabytes" and unidad_destino == "Petabytes":
        resultado = valor * 0.001
        return resultado

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

    escala_origen, escala_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_temperatura(valor, escala_origen, escala_destino)
    st.write(f"{valor} {escala_origen} son {resultado:.2f} {escala_destino}")

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
    conversiones_longitud = ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_longitud)
    valor = st.number_input("Ingresa el valor", value=0.0)

    unidad_origen, unidad_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
    st.write(f"{valor} {unidad_origen} son {resultado:.4f} {unidad_destino}")

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
    conversiones_peso = ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_peso)
    valor = st.number_input("Ingresa el valor", value=0.0)

    unidad_origen, unidad_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_peso(valor, unidad_origen, unidad_destino)
    st.write(f"{valor} {unidad_origen} son {resultado:.4f} {unidad_destino}")


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
    conversiones_volumen = ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_volumen)
    valor = st.number_input("Ingresa el valor", value=0.0)

    unidad_origen, unidad_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_volumen(valor, unidad_origen, unidad_destino)
    st.write(f"{valor} {unidad_origen} son {resultado:.4f} {unidad_destino}")


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
    conversiones_tiempo = ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_tiempo)
    valor = st.number_input("Ingresa el valor", value=0.0)

    unidad_origen, unidad_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_tiempo(valor, unidad_origen, unidad_destino)
    st.write(f"{valor} {unidad_origen} son {resultado:.4f} {unidad_destino}")


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
    conversiones_velocidad = ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_velocidad)
    valor = st.number_input("Ingresa el valor", value=0.0)

    unidad_origen, unidad_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_velocidad(valor, unidad_origen, unidad_destino)
    st.write(f"{valor} {unidad_origen} son {resultado:.4f} {unidad_destino}")


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

elif categoria_seleccionada == "Velocidad":
    conversiones_velocidad = ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_velocidad)
    valor = st.number_input("Ingresa el valor", value=0.0)

    unidad_origen, unidad_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_velocidad(valor, unidad_origen, unidad_destino)
    st.write(f"{valor} {unidad_origen} son {resultado:.4f} {unidad_destino}")


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

    unidad_origen, unidad_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_energia(valor, unidad_origen, unidad_destino)
    st.write(f"{valor} {unidad_origen} son {resultado:.4f} {unidad_destino}")


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
    conversiones_presion = ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_presion)
    valor = st.number_input("Ingresa el valor", value=0.0)

    unidad_origen, unidad_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_presion(valor, unidad_origen, unidad_destino)
    st.write(f"{valor} {unidad_origen} son {resultado:.4f} {unidad_destino}")


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
    conversiones_tamano_datos = ["Megabytes a gigabytes", "Gigabytes a terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"]
    conversion_seleccionada = st.sidebar.selectbox("Tipo de conversión", conversiones_tamano_datos)
    valor = st.number_input("Ingresa el valor", value=0.0)

    unidad_origen, unidad_destino = conversion_seleccionada.split(" a ")
    resultado = convertir_tamano_datos(valor, unidad_origen, unidad_destino)
    st.write(f"{valor} {unidad_origen} son {resultado:.6f} {unidad_destino}")


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
