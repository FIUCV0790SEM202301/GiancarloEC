def auxiliarTuplist (intervalo):
   
    if not type(intervalo) in (tuple, list):
        raise TypeError()
    elif len(intervalo)!= 2:
        raise ValueError()
    elif intervalo[0]>= intervalo[1]:
        raise ValueError()    
   
    elif type(intervalo)== tuple:
        return(True)
    elif type(intervalo)== list:
        return(False)



def valInt(n, intervalo=None):
    

    if type(n)!=int:
        if intervalo!= None:
            auxiliarTuplist(intervalo)

        return False
    elif auxiliarTuplist(intervalo)==True: #Es una tuple
        if not n in range(intervalo[0]+1, intervalo [1]): #
            return False
        return True 
    elif auxiliarTuplist(intervalo)== False: #Es una lista
        if not n in range(intervalo[0], intervalo [1] +1): # evalua presencia de n dentro del intervalo desde primer hasta [ultimo]
           return False
        return True
    return True
    
def valFloat(n, intervalo=None):
    

    if type(n)!=float and type(n)!= int:
        if intervalo!= None:
            auxiliarTuplist(intervalo)

        return False
    elif auxiliarTuplist(intervalo)==True: #Es una tuple
        if intervalo[0]>= n or intervalo[1]<=n:
            return False
        return True 
    elif auxiliarTuplist(intervalo)== False: #Es una lista
        if intervalo[0]> n or intervalo[1]<n:
            return False
        return True 
    return True


def valComplex(n, intervalo=None):
    if type(n)!=complex:
        if intervalo!= None:
            auxiliarTuplist(intervalo)

        return False
    elif auxiliarTuplist(intervalo)==True: #Es una tuple
        n = (n.real**2+n.imag**2)**(0.5)
        if intervalo[0]>= n or intervalo[1]<=n:
            return False
        return True 
    elif auxiliarTuplist(intervalo)== False: #Es una lista
        n = (n.real**2+n.imag**2)**(0.5)
        if intervalo[0]> n or intervalo[1]<n:
            return False
        return True 
    return True


def valList(lista, list_int= None , value_len=None):
    if type(lista)!= list:
        return (False)
    if not type(list_int) in (list, int) and list_int!= None:
        raise TypeError()
    if (list_int== None and value_len != None) or (list_int!= None and value_len == None):
        raise TypeError ('no se admiten dos argumentos. Debe ser uno solo o tres en simultaneo')

    if value_len != 'value' and value_len!= 'len' and value_len!= None:
        raise ValueError()
    if type(list_int)== list and value_len== 'len':
        raise TypeError()
    if type (list_int)== int and value_len== 'value':
        raise TypeError()
    
    
    if type(list_int)== int and value_len == 'len':
        if len(lista)== list_int:
            return (True)
        return False
    if type(list_int)== list and value_len == 'value':
        list_int.sort()
        lista.sort()
        if list_int == lista:
            return True
        return False
        
        
    return True




    
    
