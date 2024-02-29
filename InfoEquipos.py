import csv
import Puntos
import QuienGana
def InfoEquipos(datosliga, equipos):
    info_equipos = []

    for equipo in equipos:
        partidos_ganados = 0
        partidos_empatados = 0
        partidos_perdidos = 0

        for partido in datosliga:
            if equipo == partido['Team 1']:
                resultado = QuienGana(partido['FT'])
                if resultado == 1:
                    partidos_ganados += 1
                elif resultado == 0:
                    partidos_empatados += 1
                else:
                    partidos_perdidos += 1
            elif equipo == partido['Team 2']:
                resultado = QuienGana(partido['FT'])
                if resultado == -1:
                    partidos_ganados += 1
                elif resultado == 0:
                    partidos_empatados += 1
                else:
                    partidos_perdidos += 1

        puntos = Puntos([partidos_ganados, partidos_empatados, partidos_perdidos])
        info_equipos.append((equipo, partidos_ganados, partidos_empatados, partidos_perdidos, puntos))

    return info_equipos
