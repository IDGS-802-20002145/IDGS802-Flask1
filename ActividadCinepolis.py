from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/", methods=["GET"])
def menu():
    return render_template("formCinepolis.html")

@app.route('/desc', methods=["POST"])
def calcularDescuentos():
    boletas = int(request.form.get('txtCantidadBol'))
    tarCineco = request.form.get('rbtnTarjeta')
    nCompradores = int(request.form.get('txtCantidadC'))
    precio = 12
    total = precio * boletas
    cantMaxBol = nCompradores * 7
   
    alerta = ""
    
    t=""
    if cantMaxBol < boletas:
        alerta = "Lo maximo son 7 entradas P/P"
        t = ""
        
    else:
        if int(boletas) > 5:
            if tarCineco == "S":
                pDesc =  total - (total*0.15)
                t = pDesc - (pDesc*0.1)
            else:
                t = total - (total*0.15)
        elif int(boletas) == 3 or int(boletas) == 4 or int(boletas) == 5:
            if tarCineco == "S":
                    pDesc= total-(total*0.1)
                    t = pDesc -(pDesc*0.1)
            else:
                    t = total-(total*0.1)
        else:
            if tarCineco == "S":
                    t = total- (total*0.1)
                    print(total*0.1)
            else:
                    t= total     
    
   
     
    return render_template('formCinepolis.html',total=t, alert=alerta)



if __name__ == "__main__":
    app.run(debug=True, port=3000)




