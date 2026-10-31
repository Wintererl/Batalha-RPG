from abc import ABC, abstractmethod
from random import randint
from rich import print

class Personagem(ABC):
    
    golpes = [
        ['Lâmina Giratória', 'Assalto Feroz', 'Corte de Sangue'], # Golpes do Guerreiro
        ['Sabre de Luz', 'Julgamento', 'Fúria da Natureza'] # Golpes do Mago
    ]
    
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.vida_inicial = vida
        self.golpes = self.__class__.golpes
        
    def atacar(alvo, forca):
        pass
    
    def receber_dano(dano):
        pass
    
    @abstractmethod
    def curar():
        pass
    

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida, Personagem.golpes[0], Personagem.vida_inicial)
    
    def curar(self):
        cura = randint(5, 100)
        cura = self.vida_inicial - self.vida
        self.vida += cura
        
        if self.vida > self.vida_inicial:
            self.vida = self.vida_inicial 
        
        cura_mensagens = [
            'cauterizou a ferida com uma tocha',
            'Rasgou um trapo da camisa, enrolou sobre a ferida'
            'Enrolou uma atadura sobre os ferimentos'
        ]
        return f'[blue]{self.nome}[/] {cura_mensagens} e [green]recuperou {cura} pontos de vida![/]'
    
    
class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida, Personagem.golpes[1], Personagem.vida_inicial)
        
    def curar(self):
        cura = randint(5, 100)
        self.vida += cura
        
        if self.vida > self.vida_inicial:
            cura = self.vida_inicial - self.vida
            self.vida = self.vida_inicial 
         
        cura_mensagens = [
            'utilizou magia de cura',
            'clamou pela Deusa'
            'absorveu mana do ambiente'
        ]
        return f'[blue]{self.nome}[/] {cura_mensagens} e [green]recuperou {cura} pontos de vida![/]'