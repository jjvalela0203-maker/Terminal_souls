def verificar_ganador (h_hp, e_hp):
    if h_hp <= 0:
        print("Tu vida ha llegado a 0, has sido derrotado")
        return True
    if e_hp <= 0:
        print("Has derrotado a tu enemigo")
        return True 
    else:
        return False