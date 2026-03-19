def turno ():
    turno_h = int(input("Elige tu proximo movimiento.\n" \
                    "1. Ataque basico\n" \
                    "2. Usar pocion\n" \
                    "3. Ultimate\n" \
                    ": "))
    if turno_h == 1:
        return 1
    elif turno_h == 2:
        return 2
    else:
        return 3
    
    
