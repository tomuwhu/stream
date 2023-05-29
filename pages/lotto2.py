from random import randrange as sz
type = {
    "ötös": {"n": 5, "l": range(1,90)}, 
    "hatos": {"n": 6, "l": range(1,45)}
}

typ = "ötös"
l = sorted(
    type[typ]["l"], 
    key = lambda _: 
        sz(100)/100 - 0.5
    )[:type[typ]["n"]]
l.sort()
{i+1: j for i, j in enumerate(l)}
