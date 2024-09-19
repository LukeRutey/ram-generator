from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def generate_random_number():
    number = random.randint(1, 100)
    return f'The random number is: {number}'

if __name__ == '__main__':
    app.run()
