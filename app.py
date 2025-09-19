import streamlit as st
import numpy as numpy
import matplotlib.pyplot as pyplot
import seaborn as sns
import pandas as pd
import numpy as np

#st.title("Hello many world!")

#df = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})

#st.write("st.write:")
#st.write(df)

#st.write("st.table:")
#st.table(df)

#st.write("st.dataframe:")
#st.dataframe(df)

#chart_data = pd.DataFrame(
#    np.random.randn(20,3),
#    columns=['a','b','c'])

#st.write("st.line_chart:")
#st.line_chart(chart_data)

#st.write("st.area_chart:")
#st.area_chart(chart_data)

#st.write("st.bar_chart:")
#st.bar_chart(chart_data)

#map_data = pd.DataFrame(
#    np.random.randn(1000,2) / [50,50] + [52, 13], columns = ['lat','lon'])

#st.write("st.map:")
#st.map(map_data)

x = np.linspace(0, np.pi*2, 100)
t = st.slider('t', 0.0, 10.0, 1.0)
x0 = st.slider("x0", 0.0, np.pi*2, 0.0) 
y = np.sin(x*t+x0)

#st.line_chart(pd.DataFrame({"x":x, "y":y}))

#st.text_input("Your name", key = "name")
#st.session_state.name

#if st.checkbox("Show line chart"):
#    st.line_chart(pd.DataFrame({"sin(x*t+x0)": y}))

function_name = st.selectbox("Function",["sin","cos","tan"])
function_dict = {"sin": np.sin, "cos": np.cos, "tan": np.tan} 

if st.checkbox("Show line chart"):
    y = function_dict[function_name](x*t+x0)
    st.line_chart(pd.DataFrame({f"{function_name}(x*t+x0)": y},))

#with st.sidebar:
#    st.write("This is the sidebar")