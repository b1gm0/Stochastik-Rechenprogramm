#Input-Variablen
print(f"")
print(f"Bitte Werte eingeben")
print(f"")
a_Häufigkeit = float(input("Gib die absolute Häufigkeit ein: "))
Gesamtwert = float(input("Gib den Gesamtwert ein: "))

#Variablen & Rechenvorgänge
r_Häufigkeit = round(a_Häufigkeit / Gesamtwert * 100, 2)
Häufigkeit_zähler = 0
Häufigkeit_nenner = 0
Gegenhäufigkeit = round(100 - r_Häufigkeit, 2)

#Bruchberechnungen
if r_Häufigkeit  == 0.5:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 200
elif r_Häufigkeit  == 1:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 2:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 3:
    Häufigkeit_zähler = 3
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 4:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 5:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 20
elif r_Häufigkeit  == 6:
    Häufigkeit_zähler = 3
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 7:
    Häufigkeit_zähler = 7
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 8:
    Häufigkeit_zähler = 2
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 9:
    Häufigkeit_zähler = 9
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 10:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 10
elif r_Häufigkeit  == 11:
    Häufigkeit_zähler = 11
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 12:
    Häufigkeit_zähler = 3
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 12.5:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 8
elif r_Häufigkeit  == 13:
    Häufigkeit_zähler = 13
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 14:
    Häufigkeit_zähler = 7
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 15:
    Häufigkeit_zähler = 3
    Häufigkeit_nenner = 20
elif r_Häufigkeit  == 16:
    Häufigkeit_zähler = 4
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 16.67:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 6
elif r_Häufigkeit  == 17:
    Häufigkeit_zähler = 17
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 18:
    Häufigkeit_zähler = 9
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 19:
    Häufigkeit_zähler = 19
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 20:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 5
elif r_Häufigkeit  == 21:
    Häufigkeit_zähler = 21
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 22:
    Häufigkeit_zähler = 11
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 23:
    Häufigkeit_zähler = 23
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 24:
    Häufigkeit_zähler = 6
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 25:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 4
elif r_Häufigkeit  == 26:
    Häufigkeit_zähler = 13
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 27:
    Häufigkeit_zähler = 27
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 28:
    Häufigkeit_zähler = 7
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 29:
    Häufigkeit_zähler = 29
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 30:
    Häufigkeit_zähler = 3
    Häufigkeit_nenner = 10
elif r_Häufigkeit  == 31:
    Häufigkeit_zähler = 31
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 32:
    Häufigkeit_zähler = 8
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 33:
    Häufigkeit_zähler = 33
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 33.33:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 3
elif r_Häufigkeit  == 34:
    Häufigkeit_zähler = 17
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 35:
    Häufigkeit_zähler = 7
    Häufigkeit_nenner = 20
elif r_Häufigkeit  == 36:
    Häufigkeit_zähler = 9
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 37:
    Häufigkeit_zähler = 37
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 37.5:
    Häufigkeit_zähler = 3
    Häufigkeit_nenner = 8
elif r_Häufigkeit  == 38:
    Häufigkeit_zähler = 19
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 39:
    Häufigkeit_zähler = 39
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 40:
    Häufigkeit_zähler = 2
    Häufigkeit_nenner = 5
elif r_Häufigkeit  == 41:
    Häufigkeit_zähler = 41
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 42:
    Häufigkeit_zähler = 21
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 43:
    Häufigkeit_zähler = 43
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 44:
    Häufigkeit_zähler = 11
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 45:
    Häufigkeit_zähler = 9
    Häufigkeit_nenner = 20
elif r_Häufigkeit  == 43:
    Häufigkeit_zähler = 43
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 46:
    Häufigkeit_zähler = 23
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 47:
    Häufigkeit_zähler = 47
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 48:
    Häufigkeit_zähler = 12
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 49:
    Häufigkeit_zähler = 49
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 50:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 2
elif r_Häufigkeit  == 51:
    Häufigkeit_zähler = 51
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 52:
    Häufigkeit_zähler = 13
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 53:
    Häufigkeit_zähler = 53
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 54:
    Häufigkeit_zähler = 27
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 55:
    Häufigkeit_zähler = 11
    Häufigkeit_nenner = 20
elif r_Häufigkeit  == 56:
    Häufigkeit_zähler = 14
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 57:
    Häufigkeit_zähler = 57
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 58:
    Häufigkeit_zähler = 29
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 59:
    Häufigkeit_zähler = 59
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 60:
    Häufigkeit_zähler = 3
    Häufigkeit_nenner = 5
elif r_Häufigkeit  == 61:
    Häufigkeit_zähler = 61
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 62:
    Häufigkeit_zähler = 31
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 62.5:
    Häufigkeit_zähler = 5
    Häufigkeit_nenner = 8
elif r_Häufigkeit  == 63:
    Häufigkeit_zähler = 63
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 64:
    Häufigkeit_zähler = 16
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 65:
    Häufigkeit_zähler = 13
    Häufigkeit_nenner = 20
elif r_Häufigkeit  == 66:
    Häufigkeit_zähler = 33
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 66.67:
    Häufigkeit_zähler = 2
    Häufigkeit_nenner = 3
elif r_Häufigkeit  == 67:
    Häufigkeit_zähler = 67
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 68:
    Häufigkeit_zähler = 17
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 69:
    Häufigkeit_zähler = 69
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 70:
    Häufigkeit_zähler = 7
    Häufigkeit_nenner = 10
elif r_Häufigkeit  == 71:
    Häufigkeit_zähler = 71
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 72:
    Häufigkeit_zähler = 18
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 73:
    Häufigkeit_zähler = 73
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 74:
    Häufigkeit_zähler = 37
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 75:
    Häufigkeit_zähler = 3
    Häufigkeit_nenner = 4
elif r_Häufigkeit  == 76:
    Häufigkeit_zähler = 19
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 77:
    Häufigkeit_zähler = 77
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 78:
    Häufigkeit_zähler = 39
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 79:
    Häufigkeit_zähler = 79
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 80:
    Häufigkeit_zähler = 4
    Häufigkeit_nenner = 5
elif r_Häufigkeit  == 81:
    Häufigkeit_zähler = 81
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 82:
    Häufigkeit_zähler = 41
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 83:
    Häufigkeit_zähler = 83
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 83.33:
    Häufigkeit_zähler = 5
    Häufigkeit_nenner = 6
elif r_Häufigkeit  == 84:
    Häufigkeit_zähler = 21
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 85:
    Häufigkeit_zähler = 17
    Häufigkeit_nenner = 20
elif r_Häufigkeit  == 86:
    Häufigkeit_zähler = 43
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 87:
    Häufigkeit_zähler = 87
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 87.5:
    Häufigkeit_zähler = 7
    Häufigkeit_nenner = 8
elif r_Häufigkeit  == 88:
    Häufigkeit_zähler = 22
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 89:
    Häufigkeit_zähler = 89
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 90:
    Häufigkeit_zähler = 9
    Häufigkeit_nenner = 10
elif r_Häufigkeit  == 91:
    Häufigkeit_zähler = 91
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 92:
    Häufigkeit_zähler = 23
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 93:
    Häufigkeit_zähler = 93
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 94:
    Häufigkeit_zähler = 47
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 95:
    Häufigkeit_zähler = 19
    Häufigkeit_nenner = 20
elif r_Häufigkeit  == 96:
    Häufigkeit_zähler = 24
    Häufigkeit_nenner = 25
elif r_Häufigkeit  == 97:
    Häufigkeit_zähler = 97
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 98:
    Häufigkeit_zähler = 49
    Häufigkeit_nenner = 50
elif r_Häufigkeit  == 99:
    Häufigkeit_zähler = 99
    Häufigkeit_nenner = 100
elif r_Häufigkeit  == 100:
    Häufigkeit_zähler = 1
    Häufigkeit_nenner = 1
else:
    Häufigkeit_zähler = a_Häufigkeit
    Häufigkeit_nenner = Gesamtwert

Gegenhäufigkeit_zähler = Häufigkeit_nenner - Häufigkeit_zähler
Gegenhäufigkeit_nenner = Häufigkeit_nenner

#Druckvorgang
print(f"")
print(f"absolute Häufigkeit: {a_Häufigkeit}")
print(f"Gesamtwert: {Gesamtwert}")
print(f"relative Häufigkeit: {r_Häufigkeit}%, {Häufigkeit_zähler}/{Häufigkeit_nenner}")
print(f"Gegenhäufigkeit: {Gegenhäufigkeit}%, {Gegenhäufigkeit_zähler}/{Gegenhäufigkeit_nenner}")
print(f"")
input("Drücken einer Taste zum Beenden")
