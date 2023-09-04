def imc(weight, height):
    if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Os argumentos devem ser do tipo int ou float")
    return weight / (height * height)


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")


def show_imc():
    try:
        weight = get_float_input("Informe o peso em quilogramas: ")
        height = get_float_input("Informe a altura em metros: ")

        print(f"Calculando o IMC para peso {weight} kg e altura {height} m...")

        result = imc(weight, height)

        print(f"O resultado do IMC foi de {result}.")

        if result < 18.5:
            print("Situação: MAGREZA")
        elif result < 25:
            print("Situação: NORMAL")
        elif result < 30:
            print("Situação: SOBREPESO")
        elif result < 40:
            print("Situação: OBESIDADE")
        else:
            print("Situação: OBESIDADE GRAVE")
    except ValueError as err:
        print(err)


show_imc()
