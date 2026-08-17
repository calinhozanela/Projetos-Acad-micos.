numero = int(input("Digite o numero para ver a tabuada: "))

if numero < 1 or numero > 10:
    print("Numero fora do intervalo, digite um número de 1 a 10")
else:
    for i in range(1, 11):
      resultado = numero * i
      print(f"{numero} x {i} = {resultado}")
      
