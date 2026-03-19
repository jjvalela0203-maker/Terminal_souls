import random

def ataque():

    dano_h=random.randint(10,25)
    s_p=random.randint(30,50)
    dano_e=random.randint(15,20)

    h_hp=100
    e_hp= 120

    if turno_h == 3:
        e_hp= e_hp-s_p
    else:
        e_hp= e_hp-dano_h

    return h_hp, e_hp, dano_e, dano_h
