cont1=int(0)
cont2=int(0)
cont3=int(0)
cont4=int(0)
cont5=int(0)
a=print ("El mayor de 5 numeros ingresados")
for a in range (0,5):
 n=int(input("Escriba los numeros:"))
 if a==0:
  cont1 += n
 if a==1:
  cont2 += n
 if a==2:
  cont3 += n
 if a==3:
  cont4 += n
 if a==4:
  cont5 += n
if cont1>cont2 and cont1>cont3 and cont1>cont4 and cont1>cont5:
 print ("El numero mayor es:", cont1)
if cont2>cont1 and cont2>cont3 and cont2>cont4 and cont2>cont5:
 print ("El numero mayor es:", cont2)
if cont3>cont2 and cont3>cont1 and cont3>cont4 and cont3>cont5:
 print ("El numero mayor es:", cont3)
if cont4>cont2 and cont4>cont3 and cont4>cont1 and cont4>cont5:
 print ("El numero mayor es:", cont4)
if cont5>cont2 and cont5>cont3 and cont5>cont4 and cont5>cont1:
 print ("El numero mayor es:", cont5)
