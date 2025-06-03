from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [] # Sua lista de tarefas em memória

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form.get('task')
        
        if task_content:
            tasks.append(task_content)
            # AQUI ESTÁ A MUDANÇA: Agora renderizamos 'realizado.html'
            # e passamos a 'task_content' para que ele possa ser exibido na página de sucesso.
            return render_template('realizado.html', task=task_content)
        else:
            # Se a tarefa estiver vazia, ainda mostramos o erro na página principal
            return render_template('index.html', tasks=tasks, error_message="A tarefa não pode ser vazia!")
            
    # Se a requisição for GET, apenas renderiza a página principal com as tarefas
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)