from streamlit import line_chart, slider, audio, text_input
from math import sin
from requests import get

p = slider("Megjelenítendő kesesési eredmény száma", 1, 50, 8)

i = text_input("Keresés")
r = get(f"https://itunes.apple.com/search?limit={p}&term={i}").json()

if (r["results"]):
    for e in r["results"]:
        if "artistName" in e and "trackName" in e and "previewUrl" in e:
            e["artistName"] + ": " + e["trackName"]
            audio(e["previewUrl"])
else:
    "Nincs találat"

l = [[sin((i + 7*j) / 10) + 1 for j in range(1, 10)] for i in range(1, 200)]

line_chart(l)
