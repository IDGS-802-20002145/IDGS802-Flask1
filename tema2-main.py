from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo ------ Nuevo ---------"

@app.route("/hola")
def hola():
    return "Hola en la nueva ruta"

if __name__ =="__main__":
    app.run(debug=True,port=3000)