##Caracol Express”
list_rut=["21673677-1"]
list_nom=["FELIPE"]
list_precio=[2000]
lsit_peso=[17]
list_ciudad=["PARIS"]
list_SOP=["SOBRE"]

def ingreso_SOP():
    while True:
        try:
            print("TIPO DE PAQUETE\n----------------\n1- SOBRE\n2- PAQUETE")
            resp=int(input("-"))
            if resp==1:
                sobre="SOBRE"
                list_SOP.append(sobre)
                print("Se ingreso su respuesta correctamente\n")
                break
            elif resp==2:
                paquete="PAQUETE"
                list_SOP.append(paquete)
                print("se ingreso su respuesta correctamente\n")
                break
            else:
                print("ESTA OPCION NO ES VALIDA\n")
        except:
            print("ocurrio una exepcion")

def ingreso_rut():
    while True:
        try:
            rut_u=input("ingrse su rut(con el -) : ")
            cont_R=len(rut_u)
            if cont_R==10:
                result=rut_u.count("-",-2,-1)
                if result==1:
                    rut=rut_u.upper()
                    list_rut.append(rut)
                    print("se ingreso el rut correctamente\n")
                    break
                else:
                    print("\nerror de ingreso de rut(el - deberia estar antepenultimo)\n")
            else:
                print(f"\n error de ingreso de rut,solo tiene {cont_R} digitos.\n (verifique si estan todos los digitos,deberian ser 10)\n")
        except:
            print("ocurrio una exepcion")

def ingreso_nom(): 
    while True:
        try:
            nom_u=input("ingrse su nombre : ")
            cont_n=len(nom_u)
            if cont_n>2 and cont_n<=30:
                nom=nom_u.upper()
                list_nom.append(nom)
                print("se ingreso el nombre correctamente\n")
                break
            else:
                print(f"\n error de ingreso de nombre, tiene q tener mas de 2 y menos de 30 caracteres.\n")
        except:
            print("ocurrio una exepcion")

def ingreso_precio():
    while True:
        try:
            precio_u=int(input("ingrese el precio: "))
            if precio_u>=2000:
                list_precio.append(precio_u)
                print("se ingreso el precio correctamente\n")
                break
            else:
                print("\nEL PRECIO DEBE SER MAYOR O IGUAL A 2000\n")

        except:
            print("ocurrio una exepcion")

def ingreso_peso():
    while True:
        try:
            peso_u=float(input("Ingrese el peso: "))
            if peso_u>=0.1:
                lsit_peso.append(peso_u)
                print("se ingreso un peso correctamente\n")
                break
            else:
                print("el peso debe ser mayor a 0.1\n")
        except:
            print("ocurrio una exepcion\n")

def ingreso_ciudad():
     while True:
        try:
            ciudad_u=input("Ingrese la ciudad: ")
            con_n=len(ciudad_u)
            if con_n>2 :
                nomc=ciudad_u.upper()
                print(f"{nomc}")
                list_ciudad.append(nomc)
                print("se ingreso la ciudad correctamente\n")
                break
            else:
                print(f"\n error al ingreso de la ciudad, tiene q tener mas de 2 caracteres.\n")
        except:
            print("ocurrio una exepcion")


menu=("""
---------MENU--------
1-GRABAR
2-BUSCAR
3-Listar encomiendas
0-salir
---------------------
""")

while True:
    print(menu)
    try:
        opc=int(input("Igrese una opcion- "))
        if opc==1:
            ingreso_SOP()
          
            ingreso_rut()
           
            ingreso_nom()
            
            ingreso_precio()
            
            ingreso_peso()
            
            ingreso_ciudad()
           
        
        if opc==3:
            print("\nLISTADO DE ENCOMIENDAS")
            print("N° |TIPO DE PAQUETE|    RUT    | PRECIO |  PESO  |   CIUDAD   | NOMBRE DESTINATARIO")
            print("----------------------------------------------------------------------------------")
            for i in range(len(list_rut)):
                print(f"{i:3d}|{list_SOP[i]:15s}|{list_rut[i]:11s}|{list_precio[i]:8d}|{lsit_peso[i]:5f}KG|{list_ciudad[i]:12s}|{list_nom[i]:31s}")
    
        if opc==2:
            print("buscar")
        if opc==0:
            break
    except:
        print("ocurrio una exepcion")
   

fin=input("A salido del menu principal -")

