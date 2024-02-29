def QuienGana(resultado):
    goles_local, goles_visitante = map(int, resultado.split('-'))

    if goles_local == goles_visitante:
        return 0  # Empate
    elif goles_local > goles_visitante:
        return 1  # Equipo de casa gana
    else:
        return -1  # Equipo visitante gana