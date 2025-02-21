from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to calculate the number of panels that fit in the area without rotation
def number_of_panels(L, W, a, b):
    """Calcula el número de paneles que caben en un área de dimensiones L x W con paneles de dimensiones a x b"""
    return (L // a) * (W // b)

# Function to calculate the maximum number of panels with or without rotation
def max_panels(L, W, a, b):
    """Calcula el número máximo de paneles que caben en un techo de dimensiones L x W,
    considerando la posibilidad de rotar los paneles y aprovechando el espacio sobrante."""

    # Opción 1: Sin rotación (colocar paneles con dimensiones a x b)
    op1 = number_of_panels(L, W, a, b)

    # Restos de espacio después de colocar paneles
    rest_L = L % a
    rest_W = W % b

    # Opción 1: Intentar colocar más paneles en los restos de espacio
    op1_rest = max(number_of_panels(L, rest_W, b, a), number_of_panels(rest_L, W, b, a))

    # Opción 2: Con rotación (colocar paneles con dimensiones b x a)
    op2 = number_of_panels(L, W, b, a)

    # Restos de espacio después de colocar paneles rotados
    rest_L = L % b
    rest_W = W % a

    # Opción 2: Intentar colocar más paneles en los restos de espacio
    op2_rest = max(number_of_panels(L, rest_W, a, b), number_of_panels(rest_L, W, a, b))

    # Retornar el máximo entre las opciones, considerando los restos
    return max(op1 + op1_rest, op2 + op2_rest)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    # Obtener los valores de los inputs
    try:
        largo_techo = float(request.form.get('input1'))
        ancho_techo = float(request.form.get('input2'))
        largo_panel = float(request.form.get('input3'))
        ancho_panel = float(request.form.get('input4'))
    except ValueError:
        return jsonify({'respuesta': 'Por favor ingrese valores válidos para todos los campos.'})

    # Calcular el número máximo de paneles que caben en el techo
    resultado = max_panels(largo_techo, ancho_techo, largo_panel, ancho_panel)

    # Devolver la respuesta en formato JSON
    return jsonify({'respuesta': f"Número máximo de paneles solares que caben: {resultado}"})


if __name__ == '__main__':
    app.run(debug=True)
