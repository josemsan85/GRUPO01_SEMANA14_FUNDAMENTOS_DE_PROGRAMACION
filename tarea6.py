#producto con decuento, esotck, y nombre
nombre =""
precio = 0
stock  = 0  

descuento =0; 
def aplicarDescuento(precio, descuento):
    return (precio - descuento*precio/100)

def vender(nombre, stock, precio, disco):
    descuento = aplicarDescuento(precio, disco)
    if stock > 0 and isinstance(precio, (int, float) ) :
     print ("el producto " + nombre + " tiene stock de " + str(stock) + " y cuesta " + str(descuento) )
    else:
       print ("no hay stock")
vender("pollo", 20, 15 , 5)