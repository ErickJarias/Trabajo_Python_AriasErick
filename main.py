import json
import funciones.globales as fg
import compras as vc
import ventas as vv

def mainMenu(op):
    title= """
*******************************************
*************PANADERIA PANCAM**************
*******************************************
"""
fg.borrar_pantalla()
mainMenuOp= "1.compras \n2. ventas \n3. gestion de informes \n4. salir"
if(op !=4):
    print(title)
    print(mainMenuOp)
    try:
        opcion= int(input(':)'))
    except ValueError:
        print("error en la informacion ingresada")
        mainMenu(0)
    else: 
        match(opcion):
            case 1:
                vc.Compras(0)
            case 2:
                vv.Ventas(0)
            case 3:
