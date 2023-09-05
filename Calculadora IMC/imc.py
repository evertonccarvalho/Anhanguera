def calculate_imc(weight, height):
    if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Os argumentos devem ser do tipo int ou float")
    return weight / (height * height)


def interpret_imc(imc_value):

    if imc_value < 18.5:
        return "Magreza"
    elif imc_value < 25:
        return "Normal"
    elif imc_value < 30:
        return "Sobrepeso"
    elif imc_value < 40:
        return "Obesidade"
    else:
        return "Obesidade Grave"

# Função para determinar a cor com base no valor do IMC


def get_imc_color(imc_value):
    if imc_value < 18.5:
        return "red"
    elif imc_value < 25:
        return "green"
    elif imc_value < 30:
        return "orange"
    elif imc_value < 40:
        return "purple"
    else:
        return "black"


if __name__ == "__main__":
    try:
        weight = float(input("Informe o peso em quilogramas: "))
        height = float(input("Informe a altura em metros: "))

        print(f"Calculando o IMC para peso {weight} kg e altura {height} m...")

        result = calculate_imc(weight, height)

        print(f"O resultado do IMC foi de {result}.")

        situation = interpret_imc(result)

        print(f"Situação: {situation}")
    except ValueError as err:
        print(err)
