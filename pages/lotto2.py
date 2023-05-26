from random import randrange as sz
l = sorted(
    range(1,90), 
    key = lambda _: 
        sz(100)/100 - 0.5
    )[:5]
l.sort()
l