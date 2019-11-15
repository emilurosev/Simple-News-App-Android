import flask, json
from flask import Flask

app = Flask(__name__, template_folder="", static_folder="", root_path="", static_url_path="")

# @app.route('/json')
# def getJSON():
#     try:
#         data = []
#         with open('json/vesti.json', 'r') as f:
#             data = json.load(f)
#             return(str(data))

#     except(Exception):
#         return "GRESKA"

@app.route('/json')
def getJSON():
    return flask.render_template("json/vesti.json")


@app.route('/json/<number>')
def getSingleJSON(number = None):
    try:
        data = []
        with open('json/vesti.json', 'r') as f:
            data = json.load(f)
            for i in data:
                if i['id'] == number:
                    return str(i)

    except(Exception):
        return "Greska"

@app.route('/jsonEng')
def getJSONeng():
    return flask.render_template("json/vesti-eng.json")


@app.route('/jsonEng/<number>')
def getSingleJSONeng(number = None):
    try:
        data = []
        with open('json/vesti-eng.json', 'r') as f:
            data = json.load(f)
            for i in data:
                if i['id'] == number:
                    return str(i)

    except(Exception):
        return "Greska"
    


app.run(host='0.0.0.0', port=5000, debug=True)