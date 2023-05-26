#Práctica3
#Aquiles vs tortuga evaluando segundo a segundo
v_tortuga= (input('Ingrese velocidad de la tortuga dada en metros por hora: ')) #1 hora son 3600 segundos

x_inicial_tortuga= ((input('Ingrese la distancia de ventaja de la tortuga con respecto a Aquiles en m: '))) 

while ( v_tortuga.isalpha() and x_inicial_tortuga.isalpha()):
    print('por favor verifique que los datos sean numéricos')
    v_tortuga= (input('Ingrese velocidad de la tortuga dada en metros por hora: '))
    x_inicial_tortuga= ((input('Ingrese la distancia de ventaja de la tortuga con respecto a Aquiles en m: ')))
else:
    v_tortuga=float(v_tortuga)
    x_inicial_tortuga=float(x_inicial_tortuga)
    v_tortuga= v_tortuga #se recibe el dato en metros por hora, se convierte a metros por segundo
    v_aquiles= 10*v_tortuga
    t=0 #segundos
    x_tortuga= x_inicial_tortuga + v_tortuga*t 
    x_aquiles= 0 + 10*v_tortuga*t
    while x_tortuga > x_aquiles:
       
        x_tortuga= x_inicial_tortuga + v_tortuga*t 
        x_aquiles= 0 + 10*v_tortuga*t
        t+=1/3600 #para recorrer segundo a segundo
    count=1    
    while not count==5:
        corte_tiempo= count/5*t
        gap= (-v_tortuga*corte_tiempo+v_aquiles*corte_tiempo)
        hours=int(corte_tiempo)
        minutes= (corte_tiempo-int(corte_tiempo))*60
        seconds= (minutes-int(minutes))*60
        print('Pasadas', hours,'h:',int(minutes),'min:',int(seconds),'s. La distancia entre aquiles y la tortuga es de',gap,'metros')
        count+=1
    horas= int(t)
    minutos= (t-horas)*60
    segundos= (minutos-int(minutos))*60
    print('Aquiles tardará',horas,'h:',int(minutos),'min:',int(segundos),'s en alcanzar a la tortuga')