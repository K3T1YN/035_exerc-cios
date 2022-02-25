
def desafio001():
  print("Olá, mundo!")

def desafio002():
  nome = input("Digite seu nome:")
  print("Seja bem vinda, {}!".format(nome))

def desafio003():
  n1 = int(input("Digite um número:"))
  n2 = int(input("Digite outro número:"))
  soma = n1 + n2
  print("A soma entre {} e {} é igual a {}!".format(n1, n2, soma))

def desafio004():
  a = input("Digite algo:")
  print("O tipo primitivo desse valor é", type(a))

def desafio005():
  n = int(input("Digite um número:"))
  antecessor = n - 1
  sucessor = n + 1
  print("Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}".format(n, antecessor, sucessor))

def desafio006():
  n = int(input("Digite um número:"))
  dobro = n * 2
  triplo = n * 3
  raiz = n ** (1/2)
  print("O dobro de {} vale {}".format(n, dobro))
  print("O triplo de {} vale {}".format(n, triplo))
  print("A raiz quadrada de {} é igual a {:.2f}".format(n,raiz))

def desafio007():
  n1 = float(input("Primeira nota do aluno:"))
  n2 = float(input("Segunda nota:"))
  média = (n1 + n2) / 2
  print("A média entre {} e {} é igual a {}".format(n1, n2, média))


def desafio008():
  medida = float(input("Uma distância em metros:"))
  cm = medida * 100
  mm = medida * 100
  print("A média de {}m corresponde a {}mm".format(medida,cm, mm))


def desafio009():
  n = int(input("Digite um número para ver sua tabuada:"))  
  print("{} x {} = {}".format(n, 1, n*1))
  print("{} x {} = {}".format(n, 2, n*2))
  print("{} x {} = {}".format(n, 3, n*3))
  print("{} x {} = {}".format(n, 4, n*4))
  print("{} x {} = {}".format(n, 5, n*5))
  print("{} x {} = {}".format(n, 6, n*6))
  print("{} x {} = {}".format(n, 7, n*7))
  print("{} x {} = {}".format(n, 8, n*8))
  print("{} x {} = {}".format(n, 9, n*9))
  print("{} x {} = {}".format(n, 10, n*10))

def desafio010():
  real = float(input("Quanto dinheiro você tem na carteira? R$"))
  dolar = real / 1.00
  print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))


def desafio011():
  largura = float(input("Largura da parede:"))
  altura = float(input("Altura da parede:"))
  área = largura * altura
  print("Sua parede tem a dimensão {}x{} e sua área é de {}m².".format(largura, altura, área))


def desafio012():
  preço = float(input("Qual é o preço do produto? R$"))
  novo = preço - (preço * 5 / 100)
  print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${}".format(preço, novo))


def desafio013():
  salário = float(input("Qual é o salário do funcionário? R$"))
  novo = salário + (salário * 15 / 100)
  print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário, novo))


def desafio014():
  c = float(input("Informe a temperatura em °c:"))
  f = ((9*c)/5)+32
  print("A temperatura de {} °c corresponde a {} °f!".format(c, f))


def desafio015():
  dias = int(input("Quantos dias alugados?"))
  km = float(input("Quantos km rodados?"))
  pago = (dias * 60) + (km *0.15)
  print("O total a pagar é de R$ {}".format(pago))


def desafio016():
  from math import trunc
  número = float(input("Digite um valor:"))
  print("O valor digitado foi {} e sua porção inteira é {}".format(número, trunc(número)))


def desafio017():
  from math import hypot
  co = float(input("Comprimento do cateto oposto:"))
  ca = float(input("Comprimento do cateto adjente:"))
  hi = hypot(co, ca)
  print("A Hipotenusa vai medir {}".format(hi))


def desafio018():
  from math import radians, sin, cos, tan
  ângulo = float(input("Digite o ângulo que você deseja:"))
  seno = sin(radians(ângulo))
  print("O ângulo de {} tem o seno de {}".format(ângulo, seno))
  cosseno = cos(radians(ângulo))
  print("O ângulo de {} tem e o cosseno de {}".format(ângulo, cosseno))
  tangente = tan(radians(ângulo))
  print("O ângulo de {} tem a tangente de {}".format(ângulo, tangente))


def desafio019():
  import random
  n1 = str(input("Primeiro aluno:"))
  n2 = str(input("Segundo aluno:"))
  n3 = str(input("Terceiro aluno:"))
  n4 = str(input("Quarto aluno:"))
  lista = (n1, n2, n3, n4)
  escolhido = random.choice(lista)
  print("O aluno escolhido foi {}".format(escolhido))


def desafio020():
  import random
  n1 = str(input("Primeiro aluno:"))
  n2 = str(input("Segundo aluno:"))
  n3 = str(input("Terceiro aluno:"))
  n4 = str(input("Quarto aluno:"))
  lista = [n1, n2, n3, n4]
  random.shuffle(lista)
  print("A ordem de apresentação será")
  print(lista)
  

def desafio021():
  '''
#def desafio021():
  #import pygame
  #pygame.init()
  #pygame.mixer.music.load("ex021.mp3")
  #pygame.mixer.music.play()
  #pygame.event.wait()
'''


def desafio022():
  nome = str(input("Digite seu nome completo:")).strip()
  print("Analisando seu nome...")
  print("Seu nome em maiúsculo é {}".format(nome.upper()))
  print("Seu nome em maiúsculo é {}".format(nome.lower()))
  print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
  print("Seu primeiro nome tem {} letra".format(nome.find(" ")))
  

def desafio023():
  número = int(input("Informe um número:"))
  unidade = número // 1 % 10
  dezena = número // 10 % 10
  centena = número // 100 % 10
  milhar = número // 1000 % 10
  print("Analisando o número {}".format(número))
  print("Unidade: {}".format(unidade))
  print("Dezena: {}".format(dezena))
  print("Centena: {}".format(centena))
  print("Milhar: {}".format(milhar))


def desafio024():
  cidade = str(input("Em que cidade você nasceu?"))
  print(cidade[:5].upper() == "Santo")


def desafio025():
  nome = str(input("Qual seu nome completo?"))
  print("Seu nome tem Silva? {}".format("silva" in 
  nome.lower()))


def desafio026():
  frase = str(input("Digite uma frase:")).upper().strip()
  print("A letra A que aparece {} vezes na frase.".format(frase.count("A")))
  print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
  print("A última letra A apareceu na posição {}".format(frase.rfind("A")+1))


def desafio027():
  nome = str(input("Digite seu nome completo:")).strip()
  nome = nome.split()
  print("Muito prazer em te conhecer!")
  print("Seu primeiro nome é {}".format(nome[0]))
  print("Seu último nome é {}".format(nome[len(nome)-1]))


def desafio028():
  from random import randint
  computador = randint(0, 5)
  print("-=-" * 20)
  print("Vou pensar em um número entre 0, 5. Tente advinhar..")
  print("-=-" * 20)
  jogador = int(input("Em que número eu pensei? "))
  if jogador == computador:
   print("PARABÉNS! Você conseguiu me vencer!")
  else:
   print("GANHEI! Eu pensei no número {} e não no {}!".format(computador, jogador))


def desafio029():
  velocidade = float(input("Qual é a velocidade atual do carro?"))
  if velocidade > 80:
   print("MULTADO! Você excedeu o limite permitido que é de 80km/h")
   multa = (velocidade-80) * 7
   print("Você deve pagar uma multa de R$ {:.2f}!".format(multa))
  print("Tenha um bom dia! Dirija com segurança")



def desafio030():
  número = int(input("Me diga um número qualquer: "))
  resultado = número % 2
  if resultado == 0:
   print("O número {} É PAR".format(número))
  else:
   print("O número {} é IMPAR".format(número))


def desafio031():
  distância = float(input("Qual é a distância da sua viagem? "))
  print("Você está prestes a começar uma viagem de {}Km.".format(distância))
  if distância <= 200:
   preço = distância * 0.50
  else:
   preço = distância * 0.45
  print("E o preço da sua passagem será de R$ {:.2f}".format(preço))


def desafio032():
  ano = int(input("Que ano quer analisar? "))
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print("O ano {} é BISSEXTO".format(ano))
  else:
   print("O ano {} não é BISSEXTO".format(ano))


def desafio033():
  a = int(input("Primeiro valor: "))
  b = int(input("Segundo valor: "))
  c = int(input("Terceiro valor: "))
  menor = a
  if b<a and b<c:
   menor = b
  if c<a and c<b:
   menor = c
   maior = a
  if b>a and b>c:
   maior = b
  if c>a and c>b:
   maior = c
  print("O menor valor digitado foi {}".format(menor))
  print("O maior valor digitado foi {}".format(maior))


def desafio034():
  salário = float(input("Qual é o salário do funcionário? R$"))
  if salário <= 1250:
   novo = salário + (salário * 15 / 100)
  else:
   novo = salário + (salário * 10 / 100)
  print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salário, novo))


def desafio035():
  print("-="*20)
  print("Analisador de Triângulos")
  print("-="*20)
  r1 = float(input("Primeiro segmento: "))
  r2 = float(input("Segundo segmento: "))
  r3 = float(input("Terceiro segmento: "))
  if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print("Os segmentos acima PODEM FORMAR triângulos!")
  else:
   print("Os segmentos acima NÃO PODEM FORMAR triângulo")
   
    







