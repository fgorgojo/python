from flask import Flask, request
from umbrella import makeUmbrellaDecision

app = Flask(__name__)

@app.route('/')
def home():
    city = request.args.get('city')
    if city is None:
        city = 'new york'
    country = request.args.get('country')
    if country is None:
        country = 'us'
    if makeUmbrellaDecision(city,country):
        return f'Saca el paraguas en {city} de {country}'
    else:
        return f' NO Saques el paraguas en {city} de {country}'

if __name__ == "__main__":
    app.run()