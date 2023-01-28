from flask import Flask
from flask import request


app=Flask(__name__)


@app.route("/operBas",methods=["GET","POST"])
def operacion():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        if request.form.get('button') == 'sum':
            return "<h2> La suma es: {} </h2>".format(str(int(num1)+int(num2)))
        elif request.form.get('button') == 'res':
            return "<h2> La resta es: {} </h2>".format(str(int(num1)-int(num2)))
        elif request.form.get('button') == 'mult':
            return "<h2> La multiplicacion es: {} </h2>".format(str(int(num1)*int(num2)))
        elif request.form.get('button') == 'div':
            return "<h2> La division es: {} </h2>".format(str(int(num1)/int(num2)))
    else:
        return'''
        <form action = "/operBas" method="POST">
        <label><b>Ingrese los números para su operación</b></label><br></br>
        <label>N1: </label>
        <input type="text" name="num1"/><br><br>
        <label>N2: </label>
        <input type="text" name="num2"/><br><br>
        <label><b>Eligue la operacion </b></label><br><br>
        <label>Suma </label>
        <input type="radio" name="button" value="sum"><br><br>
        <label>Resta </label>
        <input type="radio" name="button" value="res"><br><br>
        <label>Multiplicacion </label>
        <input type="radio" name="button" value="mult"><br><br>
        <label>Division </label>
        <input type="radio" name="button" value="div"><br><br>        
        <button type="submit" name="Calcular">Calcular</button>
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True,port=3000)