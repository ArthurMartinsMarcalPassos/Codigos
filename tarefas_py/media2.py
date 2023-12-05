nota=input("digite sua nota:")
if nota.isnumeric():
 nota=int(nota)
 if nota>=0 and nota<=10:
  while True:
   print(f"sua nota e {nota}")
   break
 else:
  print("valor invalido")
else:
 print("nota invalida")


