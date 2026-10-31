from abc import ABC, abstractmethod
from random import randint, choice
from rich import print

class Personagem(ABC):
    golpes = [
        ['Lâmina Giratória', 'Assalto Feroz', 'Corte de Sangue'],
        ['Sabre de Luz', 'Julgamento', 'Fúria da Natureza']
    ]
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = self.__class__.golpes
        self.vida_inicial = self.vida
        
    def atacar(self, alvo, forca = 100):
        print(f'[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red]{alvo.nome}[/]([cyan]{alvo.vida}[/]) com um ', end='')
        print(f'[blue]{choice(self.golpes)}[/] de força {forca}')
        
        alvo.vida -= alvo.receber_dano(forca)
    
    def receber_dano(self, dano):
        # É chamado pelo método atacar
        dmg = randint(20, dano)
        print(f'[blue]{self.nome}[/] recebeu [red]dano de {dmg}[/]!')
        
        return dmg
    
    @abstractmethod
    def curar():
        pass
    

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Lâmina Giratória', 'Assalto Feroz', 'Corte de Sangue']
        
    
    def curar(self):
        cura = randint(5, 100)
        self.vida += cura
        
        if self.vida > self.vida_inicial:
            cura = self.vida - self.vida_inicial
            self.vida = self.vida_inicial 
        
        cura_mensagens = [
            'cauterizou a ferida com uma tocha',
            'Rasgou um trapo da camisa, enrolou sobre a ferida'
            'Enrolou uma atadura sobre os ferimentos'
        ] 
        print(f'[blue]{self.nome}[/] {choice(cura_mensagens)} e [green]recuperou {cura} pontos de vida[/]!')
    
    
class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Sabre de Luz', 'Julgamento', 'Fúria da Natureza'] 
                
    def curar(self):
        cura = randint(5, 100)
        self.vida += cura
        
        if self.vida > self.vida_inicial:
            cura = self.vida - self.vida_inicial
            self.vida = self.vida_inicial 
         
        cura_mensagens = [
            'utilizou magia de cura',
            'clamou pela Deusa'
            'absorveu mana do ambiente'
        ]
        print(f'[blue]{self.nome}[/] {choice(cura_mensagens)} e [green]recuperou {cura} pontos de vida[/]!')