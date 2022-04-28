import markdown

f = open('2. La Agonía del Régimen de la Restauración.md',"r")
list = []
for line in f:
    list.append(line)

list_with_wrongs=[]

for i in range(len(list)):
    if list[i].startswith("##"):
        cont = i+1
        cont2 = 0
        try:
            ## Cuenta las lines que hay desde i (i tiene que tener ## al principio) hasta la siguiente linea que tenga ## en el principio
            while(list[cont].startswith("##")!=True):
                ## cont2 = numero de lineas que hay hasta la siguiente con ##
                cont2 += 1
                cont += 1
        ## En caso de que no haya ninguna linea más con ##
        except:
            print("Se acabo el texto")
        ## Le pongo el Heading
        print(cont)
        list_with_wrongs.append(list[i])
        for x in range(cont2):
            ## Si hay una sola línea, que tenga algo mal poner el apartado entero
            if list[i+x+1].find('mark') != -1:
                for z in range(cont2):
                    list_with_wrongs.append(list[i+z+1])
                break

full_text= ""
for i in list_with_wrongs:
    full_text = full_text + i

htmlf = markdown.markdown(full_text)
htmlfinal = open("Pa repasar.html","w")
htmlfinal.write(htmlf)
