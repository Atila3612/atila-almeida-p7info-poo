x = int (input("Quantas frases você deseja escrever?"))
contador = 0
string = 0
while contador < x:
  condicion = 0
  frase = input("Escreva uma frase:").split()
  lista = []
  for i in frase:
      lista.append(str(len(i)))
      if len(i)>= string:
        string = len(i)
        mp = i
  saida = "-".join(lista)
  print("ENTRADA | SAÍDA")
  print(str(frase)+"|"+str(saida))
  contador += 1
  condicion = int(input("Digite 1 para continuar ou 0 para parar"))
  if condicion == 0:
      break
print("A maior palavra é: %s" %mp)