# >>>>>>>LEIA<<<<<<
# Esse é apenas um protótipo inicial que eu fiz do programa.
# Ele é completamente À PARTE do programa principal.
# Fiz ele antes de aprender POO. O "batalha-rpg" veio como uma versão 2.0 desse projeto.
# Resolvi deixá-lo aqui de qualquer forma.
# Este programa é perfeitamente funcional, aliás.
# --------------------------


import random as r
from time import sleep

def gerar_monstro(dificuldade: str) -> int:
    
    if dificuldade == 'dificil':
        nome = 'Golem Ancião'
        hp = [250, 300]
    elif dificuldade == 'medio':
        nome = 'Caçador Corrompido'
        hp = [150, 200]
    else:
        nome = 'Goblin'
        hp = [80, 100]
    
    return nome, r.randint(hp[0], hp[1])

def critico(tipo: str) -> float:
    chance = 5 if tipo == 'mob' else 15
    num = r.randint(1, 100)
    
    if num > (100 - chance):
        print('\n')
        print('Acerto crítico!')
        return 1.5
    else:
        return 1

def atk_monstro(dificuldade: str) -> int:
    if dificuldade == 'dificil':
        dano = r.randint(10, 20)
    elif dificuldade == 'medio':
        dano = r.randint(8, 15)
    else:
        dano = r.randint(5, 10)
    
    dano = dano * critico('monstro')
    return int(dano)
    
def atk_player() -> int:
    dano =  r.randint(30, 50)
    dano = dano * critico('player')
    
    return int(dano)

def simular_turno(dificuldade: str, turnos: int, monstro: str, mob_hp: int, player_hp: int) -> int:
    if turnos % 2 == 0:
        dano = atk_player()
        mob_hp = mob_hp - dano
        
        print('\n')
        print(f'Você acerta o {monstro} e causa {dano} de dano! \n')
        print(f'Vida restante do {monstro}: {mob_hp}')
        
        if mob_hp <= 0:
            return 1, mob_hp
        return 0, mob_hp
    
    else:
        dano = atk_monstro(dificuldade)
        player_hp = player_hp - dano
        
        print('\n')
        print(f'O {monstro} te acerta. Você sofre {dano} de dano! \n')
        print(f'Sua vida restante: {player_hp}')
                
        if player_hp <= 0:
            return 2, player_hp
        return 0, player_hp
        
def comecar_partida(dificuldade: str, monstro: str, mob_hp: int) -> int:
    player_hp, turnos = 100, 0
    
    while True:
        if turnos % 2 == 0:
            resultado, mob_hp = simular_turno(dificuldade, turnos, monstro, mob_hp, player_hp)
        else:
            resultado, player_hp = simular_turno(dificuldade, turnos, monstro, mob_hp, player_hp)
        
        if resultado != 0:
            return resultado, turnos

        turnos += 1
        sleep(2)
    

dificuldade = str(input('Digite a dificuldade: ')).lower()
monstro, mob_hp = gerar_monstro(dificuldade)


while True:
    resultado, turnos = comecar_partida(dificuldade, monstro, mob_hp)
    if resultado == 1:
        print(f'Você venceu! Parabéns!')
        print(f'Turnos totais: {turnos}')
        break
    else:
        retry = str(input(f'Você perdeu em {turnos} turnos... Deseja tentar novamente [y/n]? ')).lower()
        if retry == 'n':
            break
        