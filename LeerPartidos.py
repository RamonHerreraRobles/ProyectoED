import csv
def LeerPartidos(file):
    partidos = []
    
    with open(file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #Usamos DictReader porque es un lista. 
        for row in reader:
            partido = {
                'Date': row['Date'],
                'Team 1': row['Team 1'],
                'Team 2': row['Team 2'],
                'FT': row['FT'],
                'HT': row['HT']
            }
            print(partido)
            partidos.append(partido)

    
    return partidos
