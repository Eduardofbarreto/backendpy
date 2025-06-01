from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)

# Configurações do banco de dados PostgreSQL
DB_HOST = 'edu_barreto' # Substitua pelo IP/hostname do seu servidor PostgreSQL se for diferente
DB_NAME = 'postgres'
DB_USER = 'postgres'    # Geralmente é 'postgres' ou o usuário que você criou
DB_PASS = 'root'        # A senha que você mencionou

# Conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST,
                            database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salvar_nome', methods=['POST'])
def salvar_nome():
    if request.method == 'POST':
        nome = request.form['nome']
        
        if not nome:
            return "O nome não pode ser vazio!", 400 # Bad Request

        conn = None # Inicializa conn como None
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO pessoas (nome) VALUES (%s)", (nome,))
            conn.commit()
            cur.close()
            return redirect(url_for('sucesso')) # Redireciona para uma página de sucesso
        except psycopg2.Error as e:
            # Em um ambiente de produção, logar o erro e mostrar uma mensagem genérica.
            # Para depuração, podemos imprimir o erro.
            print(f"Erro ao conectar ou inserir no banco de dados: {e}")
            return "Erro ao salvar o nome no banco de dados. Por favor, tente novamente.", 500
        finally:
            if conn:
                conn.close()

@app.route('/sucesso')
def sucesso():
    return "Nome salvo com sucesso no banco de dados!"

if __name__ == '__main__':
    # Para rodar em ambiente de desenvolvimento
    # No ambiente de produção, use um servidor como Gunicorn ou Nginx/Apache + Gunicorn
    app.run(debug=True, host='0.0.0.0') # '0.0.0.0' para que seja acessível externamente na rede local