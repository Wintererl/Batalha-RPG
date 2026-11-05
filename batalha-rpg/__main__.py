from personagens_rpg import *
from time import sleep
from rich import print
from random import randint, choice

def inicializar_inimigo():
    ini_guerreiro = [
        'surge cortando entre as grossas vinhas com um imenso machado. Ele está com [red]sangue[/] nos olhos.',
        'lança uma faca de arremeso próximo a sua cabeça. Você tenta conversar -- [red]Ele não parece interessado nas suas palavaras.[/]',
        'em uma fogueira à distância, um armadurado encara você entre as finas frestas do metal enferrujado. [red]Ele não gostou da sua preseça.[/]'  
    ]
    
    ini_mago = [
        'teleporta junto a um clarão azulado atrás de você. [red]Você sente que esteve sendo observado há séculos.[/]',
        'move lentamente o cajado à distância. Um [cyan]domo espelhado[/] surge ao seu redor. Você vê seu reflexo em todas as direções. [red]É um ataque.[/]',
        'murmura algo para si mesmo. [red]Uma névoa negra envolve seus pés.[/]'
    ]
    
    escolher_classe = choice(['g', 'm'])
    
    inimigo_nome = choice(['Megaman', 'Kratos', 'Merlin', 'Viola', 'Anny', 'Misty', 'Leth', 'Larkin', 'Quirrel', 'Grimm', 'Lace'])
    inimigo_classe = Guerreiro(inimigo_nome, 2000) if escolher_classe == 'g' else Mago(inimigo_nome, 1750)
    mensagem = choice(ini_guerreiro) if escolher_classe == 'g' else choice(ini_mago)
    
    return inimigo_classe, mensagem
    
def main():
    
    print('Bem-vindo ao [green]Mini-RPG![/] Digite abaixo o seu nome. ')
    nome = input('Nome: ')
    
    print('Qual [blue]classe[/] você quer ser?')
    print('[1] [red]Guerreiro (hp: 2000 / dmg: 80)[/] | \n[2] [cyan]Mago (hp: 1750 / dmg: 100)[/]')
    
    while True:
        escolher_classe = int(input('Digite o número da classe: '))
        if escolher_classe == 1 or escolher_classe == 2:
            break
        print('Por favor, digite 1 ou 2 para escolher sua classe.')
    
    print('[green]O jogo está para começar![/]')
    
    p1 = Guerreiro(nome, 2000) if escolher_classe == 1 else Mago(nome, 1750)
    p2, ini_mensagem = inicializar_inimigo()
    
    sleep(2)
    print(f'[red]{p2.nome}[/] {ini_mensagem}')
    sleep(2)
    
    print('Uma batalha começa!')
    resultado, turnos = 0, 0
    while True:
        print('[blue]Qual será a sua próxima ação? [/]')
        print()
        print(f'[1] Atacar [red](20-{p1.dmg})[/]\n[2] Curar [green](5-100)[/]')
        acao = int(input('Ação: '))
        
        if acao == 1:
            p1.atacar(p2, p1.dmg)
        else:
            p1.curar()
        print()
        
        if p2.vida <= 0:
            resultado = 1
            break
        sleep(2)
        
        if p2.vida > p2.vida * 0.20:
            acao_inimigo = randint(1, 100)
        else:
            acao_inimigo = randint(50, 100)
        
        if acao_inimigo < 90:
            p2.atacar(p1, p2.dmg)
        else:
            p2.curar()
        print()
        if p1.vida <= 0:
            resultado = 2
            break
        turnos += 1
        sleep(2)

    if resultado == 1:
        print('Parabéns, você venceu em {turnos} turnos!')
    else:
        print('Você perdeu em {turnos} turnos... Boa sorte na próxima!')
        
        
if __name__ == "__main__":
    main()