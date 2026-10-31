from personagens_rpg import *

def main():
    p1 = Guerreiro('Megaman', 1000)
    p2 = Mago('Merlin', 5000)
    p3 = Guerreiro('Kratos', 1500)

    p1.atacar(p2)
    p3.atacar(p1)
    p2.atacar(p3)
    
    p1.curar()
    p2.curar()
if __name__ == "__main__":
    main()