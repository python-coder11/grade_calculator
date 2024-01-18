from flask import Flask, render_template, request
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testhi77'

def get_test_grades():
    tests = []
    num_of_tests = int(request.form.get("num_of_tests"))

    for i in range(num_of_tests):
        test_grade_input = request.form.get(f"test_{i + 1}")

        # Check if the input contains a slash and handle accordingly
        if '/' in test_grade_input:
            numerator, denominator = map(int, test_grade_input.split('/'))
            test_grade = numerator / denominator
        else:
            test_grade = float(test_grade_input) / 100

        tests.append(test_grade)

    return tests

def calculate_grades():
    tests = get_test_grades()
    formative_grade = float(request.form.get("formative_grade")) / 100
    grade_test_input = request.form.get("grade_test")

    # Check if the input contains a slash and handle accordingly
    if '/' in grade_test_input:
        numerator, denominator = map(int, grade_test_input.split('/'))
        grade_test = numerator / denominator
    else:
        grade_test = float(grade_test_input) / 100

    if not tests:
        all_test_grades = grade_test
    else:
        all_test_grades = tests + [grade_test]

    final_grade = 0.9 * ((sum(all_test_grades)) / (len(all_test_grades))) + 0.1 * formative_grade

    return final_grade

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_of_tests = int(request.form.get("num_of_tests"))
        answer = calculate_grades()
        return render_template('index.html', answer=f"Your grade would be {answer * 100}%", form=request.form, num_of_tests=num_of_tests)
    return render_template('index.html', answer=None, form={}, num_of_tests=0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6667, debug=False)
