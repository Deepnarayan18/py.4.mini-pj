from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_table', methods=['POST'])
def generate_table():
    try:
        number = int(request.form['number'])
        range_limit = int(request.form['range_limit'])

        if number <= 0 or range_limit <= 0:
            raise ValueError("Please enter positive integers.")

        multiplication_table = [(number, i, number * i) for i in range(1, range_limit + 1)]
        return render_template('display.html', display=multiplication_table, number=number)
    except ValueError as ve:
        return render_template('index.html', error=str(ve))
    except Exception as e:
        return render_template('error.html', error=e)

if __name__ == '__main__':
    app.run(debug=True)
