try:
    from secret.hash import hash
except ImportError:
    from public.hash import hash
from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return hash('my passworld','spiderLambo')

if __name__ == '__main__':
    app.run(debug=True)