from flask import Flask, render_template, request
from imc import calculate_imc, interpret_imc, get_imc_color
import locale

app = Flask(__name__)
app.static_folder = 'static'
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


@app.route('/', methods=['GET', 'POST'])
def calculate_and_interpret_imc():
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'].replace(',', '.'))
            height = float(request.form['height'].replace(',', '.'))

            formatted_weight = locale.format_string(
                "%.2f", weight, grouping=True)
            formatted_height = locale.format_string(
                "%.2f", height, grouping=True)

            result = calculate_imc(weight, height)
            result_formatted = "{:.2f}".format(result)
            situation = interpret_imc(result)
            imc_color = get_imc_color(result)

            return render_template('index.html', error_message=None, result=result_formatted, situation=situation, formatted_weight=formatted_weight, formatted_height=formatted_height, imc_color=imc_color)
        except ValueError:
            error_message = "Entrada inválida. Por favor, insira números válidos."
            return render_template('index.html', error_message=error_message)
    return render_template('index.html', error_message=None)


if __name__ == '__main__':
    app.run(debug=True)
