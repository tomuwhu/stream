from random import randrange as egyszam
l = sorted(sorted(range(1,90), key=lambda x: egyszam(100)/100 - 0.5)[:5])
l