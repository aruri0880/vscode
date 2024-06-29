'''Definir una función denominada “rango_etario”, que reciba por parámetro un número natural (que representa una edad) y devuelva como resultado la denominación de su respectivo grupo etario. Considere la siguiente clasificación: “primera infancia” (0 a 5 años), “infancia” (6 a 11 años), “adolescencia” (12 a 18 años), “juventud” (19 a 29 años), “adultez” (30 - 64 años) y “vejez” (65 años o más).'''

def rango_etario(edad):
    if edad>=0 and edad<=5:
        return 'primera infancia'
    elif edad>=6 and edad<=11:
        return 'infancia'
    else:
        if edad>=12 and edad<=18:
            return 'adolescencia'
        elif edad>=19 and edad<=29:
            return 'juventud'
        else:
            if edad>=30 and edad<=64:
                return 'adultez'
            elif edad>=65 and edad<=100:
                return 'vejez'
            else:
                if edad>=101:
                    return 'estas morido flaco'