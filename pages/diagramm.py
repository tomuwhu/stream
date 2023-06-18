import streamlit as st
import pandas as pd
import altair as alt

s = open("input.txt").read()
s

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

st.altair_chart(c, use_container_width=False)

