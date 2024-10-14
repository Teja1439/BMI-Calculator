
# BMI Calculator using Flask

This project is a simple BMI (Body Mass Index) Calculator web application built using Python's Flask framework. Users can input their weight and height to calculate their BMI and view their BMI classification (Underweight, Normal weight, Overweight, or Obesity).

## Features

- Input weight (in kilograms) and height (in meters).
- Calculate BMI based on the provided inputs.
- Display the BMI value along with its classification.
- Handles invalid inputs and displays user-friendly error messages.

## Technologies Used

- **Flask**: Backend web framework for Python.
- **HTML/CSS**: For rendering web pages.
- **Python**: Core programming language for backend logic.

## Prerequisites

- Python 3.x
- Flask library (install using `pip install Flask`)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/bmi-calculator-flask.git
   cd bmi-calculator-flask
   ```

2. Install Flask if not already installed:

   ```bash
   pip install Flask
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5001/` to use the BMI calculator.

## Example

- **Input**:  
  - Weight: 70 kg  
  - Height: 1.75 m

- **Output**:  
  - Your BMI is: 22.86  
  - Category: Normal weight
