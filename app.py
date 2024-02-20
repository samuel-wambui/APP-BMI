from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'PUSH', 'POST'])
def index():
    if request.method == 'POST':
        weight = int(request.form['weight'])

        
        height = float(request.form['height'])
        unit = request.form['unit']

        if unit.upper() == "K":
            converted_weight = weight / 0.45
            weight_unit = "Lbs"
        else:
            converted_weight = weight * 0.45
            weight_unit = "Kgs"

        bmi = weight / (height * height)

        if bmi < 18:
            bmi_category = "Underweight"
        elif bmi > 26:
            bmi_category = "Obese"
        else:
            bmi_category = "Healthy"

        return render_template('index.html', bmi=bmi, bmi_category=bmi_category, converted_weight=converted_weight, weight_unit=weight_unit)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
