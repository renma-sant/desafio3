class heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo


nome = input('Como se chama, aventureiro? ')
print("Seja bem vindo a aventura, " + nome + "!")
idade = int(input("Qual é a sua idade? "))

while idade < 0:
    print('Pare de trollar, nenhum personagem tem idade negativa.')
    idade = int(input('Coloque aqui uma idade válida: '))

print('Neste jogo você pode optar pelas seguintes classes: \nMago, Guerreiro, Monge, Ninja')
tipo = input('Qual é a sua escolha? ')

i = 0
while tipo.lower() not in ['mago', 'guerreiro', 'monge', 'ninja', 'programador']:
    print('Esse tipo é inválido, aventureiro, escolha uma opção válida: ')
    if i < 3:
        tipo = input('Faça uma escolha válida: ')
        i += 1
    else:
        print('Tudo bem, você venceu, a partir de agora você é tipo especial programador...')
        tipo = 'programador'
        break

heroiPersonalizado = heroi(nome, idade, tipo)

if heroiPersonalizado.tipo ==  'Mago':
    ataque = 'magia'
elif heroiPersonalizado.tipo ==  'Guerreiro':
    ataque = 'espada'
elif heroiPersonalizado.tipo ==  'Monge':
    ataque = 'artes marciais'
elif heroiPersonalizado.tipo ==  'Ninja':
    ataque = 'shuriken'
else:
    ataque = 'hacking'
    
print('Seu herói tipo {} atacou usando {}!'.format(heroiPersonalizado.tipo, ataque))