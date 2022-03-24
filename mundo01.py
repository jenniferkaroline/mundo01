

def desafio001():
  print('olá mundo!')

def desafio002():
  nome = input('escreva seu nome:')
  print('Seja bem vindo(a)', nome)

def desafio003():
  x1 = int(input("digite um número: "))
  x2 = int(input("digite outro número: "))
  s = x1 + x2
  print('a soma vale: ', s)

def desafio004():
  a = input("digite algo: ")
  print("o tipo primitivo desse valor é ", type(a))
  print("só tem espaços? ", a.isspace())
  print("é um número? ", a.isnumeric())
  print("é alfabético? ", a.isalpha())
  print("é alfanumérico? ", a.isalnum())
  print("está em maíusculas? ", a.isupper())
  print("está em minúsculas? ", a.islower())
  print("está capitalizada? ", a.istitle())

def desafio005():
  n1 = int(input("me dê um número: "))
  an1 = n1 - 1
  sn1 = n1 + 1
  print('analisando o valor {}, seu antecessor é {}, e seu sucessor é {}'.format(n1, an1, sn1))

def desafio006():
  n2 = int(input("me dê um número: "))
  dn2 = n2 * 2
  tn2 = n2 * 3
  rqn2 = n2 ** (1 / 2)
  print('analisando o valor {}, seu dobro é {}, seu triplo é {}, e sua raíz quadrada é {}'.format(n2, dn2, tn2, rqn2))

def desafio007():
  nota1 = float(input("digite sua primeira nota: "))
  nota2 = float(input("digite sua segunda nota: "))
  média = (nota1 + nota2) / 2
  print('a média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, média))

def desafio008():
  medida = float(input("me dê uma distância em metros: "))
  cm = medida * 100
  mm = medida * 1000
  print('a medida de {}m é igual a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

def desafio009():
  num = int(input("digite um número e veja sua tabuada: "))
  print('{} x {} = {}'.format(num, 1, num * 1))
  print('{} x {} = {}'.format(num, 2, num * 2))
  print('{} x {} = {}'.format(num, 3, num * 3))
  print('{} x {} = {}'.format(num, 4, num * 4))
  print('{} x {} = {}'.format(num, 5, num * 5))
  print('{} x {} = {}'.format(num, 6, num * 6))
  print('{} x {} = {}'.format(num, 7, num * 7))
  print('{} x {} = {}'.format(num, 8, num * 8))
  print('{} x {} = {}'.format(num, 9, num * 9))
  print('{} x {} = {}'.format(num, 10, num * 10))

def desafio010():
  real = float(input("quanto dinheiro você tem na carteira? R$"))
  dolar = real / 3.27
  print('com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

def desafio011():
  largura = float(input("largura da parede: "))
  altura = float(input("altura da parede: "))
  área = largura * altura
  print('sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, área))
  tinta = área / 2
  print("para pintar esta parede, você vai precisar de {} L de tinta ".format(tinta))

def desafio012():
  preço = float(input("qual é o preço do produto? R$"))
  novop = preço - (preço * 5 / 100)
  print("o produto que custa R${} está por R${} com o desonto de 5%".format(preço, novop))

def desafio013():
  salário = float(input("digite seu salário R$: "))
  reajuste = salário + (salário * 15 / 100)
  print('seu salário de R${:.2f} teve um aumento de 15% e passou a ser R${:.2f}'.format(salário, reajuste))

def desafio014():
  C = float(input("informe a temperatura em °C: "))
  F = ((9 * C ) / 5) + 32
  print('a temperatura de {}°C corresponde a {}°F'.format(C, F))

def desafio015():
  km = float(input("quantos km foram percorridos? "))
  aluguel = int(input("por quantos dias o carro foi alugado? "))
  custo = (60 * aluguel) + (0.15 * km)
  print('você vai pagar R${} por {}km rodados e {} dias alugado'.format(custo, km, aluguel))

def desafio016():
  nmr = float(input("digite um valor: "))
  print('o valor digitado foi {} e e sua porção inteira é {}'.format(nmr, int(nmr)))

def desafio017():
  import math
  co = float(input("comprimento do cateto oposto: "))
  ca = float(input("comprimento do cateto adjacente: "))
  hip = math.hypot(co, ca)
  print('a hipotenusa mede {:.2f}'.format(hip))

def desafio018():
  from math import radians, sin, cos, tan
  an = float(input("digite o ângulo que você deseja: "))
  seno = sin(radians(an))
  print('o ângulo de {} tem o seno de {:.2f}'.format(an, seno))
  cosseno = cos(radians(an))
  print('o ângulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
  tangente = tan(radians(an))
  print('o ângulo de {} tem a tangente de {:.2f}'.format(an, tangente))

def desafio019():
  import random
  a1 = input("primeiro aluno(a): ")
  a2 = input("segundo aluno(a): ")
  a3 = input("terceiro aluno(a): ")
  a4 = input("quarto aluno(a): ")
  lista1 = [a1, a2, a3, a4]
  sorteado = random.choice(lista1)
  print('o aluno(a) sorteado foi {}'.format(sorteado))

def desafio020():
  import random
  aluno1 = input("primeiro aluno(a): ")
  aluno2 = input("segundo aluno(a): ")
  aluno3 = input("terceiro aluno(a): ")
  aluno4 = input("quarto aluno(a): ")
  lista2 = [aluno1, aluno2, aluno3, aluno4]
  random.shuffle(lista2)
  print("a ordem será... ")
  print(lista2)

def desafio022():
  nome = str(input("digite seu nome completo: ")).strip()
  print("seu nome em maíusculas é {}".format(nome.upper()))
  print("seu nome em minúsculas é {}".format(nome.lower()))
  print("seu nome tem um total de {} letras".format(len(nome) - nome.count(' ')))
  print("seu primeiro nome tem um total de {} letras".format(nome.find(' ')))

def desafio023():
  numr = int(input("me dê um número: "))
  u = numr // 1 % 10
  d = numr // 10 % 10
  c = numr // 100 % 10
  m = numr // 1000 % 10
  print('a unidade é {}, a dezena é {}, a centena é {} e a unidade de milhar é {}'.format(u, d, c, m))

def desafio024():
  cid = str(input("em que cidade você mora? ")).strip()
  print(cid[:5].upper() == 'SANTO')

def desafio025():
  nm = str(input("digite seu nome completo: ")).strip()
  print("seu nome tem Silva? {}".format('silva' in nm.lower()))

def desafio026():
  frase = str(input("digite uma frase: ")).upper().strip()
  print("a letra A aparece {} vezes na frase.".format(frase.count('A')))
  print("a letra  aparece pela primeira vez na posição {}".format(frase.find('A') +1))
  print("a letra aparece pela última vez na posição {}".format(frase.rfind('A') +1))

def desafio027():
  nc = str(input("digite seu nome completo: ")).strip()
  print("muito prazer em te conhecer, {}".format(nc))
  ncf = nc.split()
  print("seu primeiro nome é {}".format(ncf[0]))
  print("seu último nome é {}".format(ncf[len(ncf) -1]))
  
  
  
  
  