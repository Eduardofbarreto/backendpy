from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form.get('task')
        
        if task_content:
            tasks.append(task_content)
            return redirect(url_for('index'))
        else:
            return render_template('index.html', tasks=tasks, error_message="A tarefa não pode ser vazia!")
    
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)