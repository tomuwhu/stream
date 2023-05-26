from random import randrange as egyszam
szamok = set()
while len(szamok) < 5: szamok.add(egyszam(1,90))
l = sorted(list(szamok))
l