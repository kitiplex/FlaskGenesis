from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    password_length = int(request.form.get('length'))
    complexity = request.form.get('complexity')
    
    if complexity == 'low':
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level"

    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

if __name__ == '__main__':
    app.run()
