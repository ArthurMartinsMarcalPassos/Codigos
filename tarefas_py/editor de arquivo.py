arq = open('./36.txt',"w")
print(arq)
lista = "1,2,3,4,5,6,7,8,9"
arq.write(lista)
arq.close()

with open('./36.txt',"r") as arq:
 for x in arq:
  print(x)

with open('./36.txt',"r") as arq:
 conteudo = arq.read()
 print(conteudo)

with open('./36.txt',"r") as arq:
 cont= arq.readline()
 print(cont)
 cont= arq.readline()
 print(cont)

with open('./36.txt',"r") as arq:
  print(arq.readlines())

with open('./36.txt',"r") as arq: 
 arq.seek(0)
 print(arq.readlines())