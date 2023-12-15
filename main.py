from flask import Flask, render_template, request
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testhi77'

def get_test_grades():
    tests = []
    num_of_tests = int(request.form.get("num_of_tests"))

    for i in range(num_of_tests):
        test_grade = float(request.form.get(f"test_{i + 1}")) / 100
        tests.append(test_grade)

    return tests

def calculate_grades():
    tests = get_test_grades()
    formative_grade = float(request.form.get("formative_grade")) / 100
    grade_test = float(request.form.get("grade_test")) / 100

    all_test_grades = tests + [grade_test]

    final_grade = 0.9 * ((sum(all_test_grades)) / (len(all_test_grades))) + 0.1 * formative_grade

    return final_grade

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        answer = calculate_grades()
        return render_template('index.html', answer=f"Your grade would be {answer * 100}%", form=request.form)
    return render_template('index.html', answer=None, form={})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6667, debug=True)
