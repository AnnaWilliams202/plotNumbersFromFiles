import glob
import streamlit as st

data = {}
filepath = sorted(glob.glob('/Users/annawilliams/Desktop/plotData/*.txt'))

for filename in filepath:
    with open(filename, 'r') as f:
        content = f.read()
        letter,number = content.split(':')
        data[letter] = float(number)
chart_data ={
    'Letters':list(data.keys()),
    'Numbers':list(data.values())
}

st.title('Numbers From Text Files')
st.line_chart(chart_data, x='Letters', y='Numbers')

st.write('Letters and Their Corresponding numbers')
for letter,number in data.items():
    st.write(f'{letter} : {number}')