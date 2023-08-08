
def codificar(n):
    
        if not type(n) in (str, int, float):
           raise TypeError() 
        n=str(n)    
        global clave       
        
        clave= {'a':'%','b':'!','c':'♪','d':'-','e':'♂','f':'◙','g':'$','h':':','i':'#','j':'=','k':'◘','l':'`','m':'~','n':'^','ñ':'&','o':')','p':'(','q':'}','r':'[','s':'/','t':'?','u':'.','v':'"','w':'•','x':'♠','y':'@','z':'<','0':'♣','1':'♦','2':'2','3':'>','4':'☻','5':'_','6':'☺','7':"'", '8':'♫','9':'☼','A':'►','B':'◄','C':'↕','D':'‼','E':'¶','F':'§','G':'▬','H':'↨','I':'↑','J':'↓','K':'→','L':'←','M':'∟','N':'↔','Ñ':'▲','O':'▼','P':',','Q':'ª','R':'|','S':'⌂','T':'Ç','U':'ü','V':'é','W':'â','X':'ä','Y':'û','Z':'ƒ'}
                
        
        lista_auxiliar=[]
        for ij in n:
           lista_auxiliar.append(ij)
        n=lista_auxiliar 
        lista_cifrada=[]
        #la clave de codificacion debe ser un diccionario
        for j in lista_auxiliar:
            for jj in clave: #jj empieza en a
                if j == jj :
                    j= clave[jj]#valor de la posicion jj
            lista_cifrada.append(j)
        texto=""
        for i in lista_cifrada:
            a= str(i)
            texto+= a
        global n_cifrado
        n_cifrado=texto
        return (n_cifrado)




def decodificar(m):
    # necesito invertir la clave cambiando cada clave por su valor
    global clave_invertida
    clave_invertida= {value:key for key, value in clave.items()}  #recurso obtenido de investigacion en internet. value:key le indica al ciclo for como reorganizar los pares de key:value en el diccionario
    texto=""
    for llave in m:
        texto+= clave_invertida[llave]
        caracter = clave_invertida [llave]
    global n_descifrado
    n_descifrado=texto
    return (n_descifrado)


print(codificar(1.53))
print(decodificar(codificar(1.53)))