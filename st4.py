import streamlit as st
import pandas as pd
import altair as alt

"""
Az $ax^2+bx+c=0$ alakú másodfokú egyenlet gyökei:
$$
x_{1,2}=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}
$$
[Biz.:](#)

A fenti egyenlet mindkét oldalát $2a$-val beszorozzuk, majd hozzáadunk $b$-t:
$$
2ax+b=\\pm\\sqrt{b^2-4ac}
$$
Mindkét oldalt négyzetre emeljük:
$$
4a^2x^2+4abx+b^2=b^2-4ac
$$
$$
4a^2x^2+4abx=-4ac
$$
4a-val elosztva, majd c-t hozzáadva:
$$
ax^2+bx+c=0
$$
[Példa:](#)

Az $x^2-x-2$ egyenlet gyökei $(a=1, b=-1, c=-2)$:
$$
x_{1,2}=\\frac{-(-1)\\pm\\sqrt{(-1)^2-4(1)(-2)}}{2(1)}=\\frac{1\\pm\\sqrt{1+8}}{2}=\\frac{1\\pm3}{2},
$$
$$
x_1=2, x_2=-1
$$
"""

chart_data = pd.DataFrame(
    [[i / 5, (i / 5) ** 2 - i / 5 - 2] for i in range(-12, 18)],
    columns = ['x', 'f(x)']
)

def black_marks():
    return {
        'config': {
            'view': {
                'height': 600
            }
        }
    }

alt.themes.register('black_marks', black_marks)
alt.themes.enable('black_marks')

c = alt.Chart(
        chart_data
    ).encode(
        x = 'x', y = 'f(x)', tooltip = ['x', 'f(x)']
    ).mark_line(
        color = 'yellow'
    ).configure_axis(
        gridColor = 'lightblue'
    )

"""
Az $f(x) = x^2-x-2 = (x-2)(x+1)$ függvény grafikonja:
"""

st.altair_chart(c, use_container_width=True)

