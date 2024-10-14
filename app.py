from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate BMI
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Route to display the form and handle the result
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get user inputs from the form
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            
            if weight <= 0 or height <= 0:
                return render_template('index.html', error="Please enter positive numbers for weight and height.")
            
            # Calculate BMI
            bmi = calculate_bmi(weight, height)
            # Classify BMI
            category = classify_bmi(bmi)
            
            return render_template('index.html', bmi=bmi, category=category)
        except ValueError:
            return render_template('index.html', error="Invalid input. Please enter numeric values for weight and height.")
    
    return render_template('index.html')

# Run the application on port 5001
if __name__ == '__main__':
    app.run(port=5001)
