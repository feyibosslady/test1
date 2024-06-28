import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


#slt.header('My first streamlit app')
#slt.subheader('BY Feyisayo Awopetu')
st.sidebar.selectbox('Select Page',['Home','model'])
st.title('Micrograd Model')

st.subheader("Image :")
st.image('/Users/mac/Documents/Screenshot 2024-06-28 at 15.46.13.png')
st.write("This is the visual representation of micrograd")
rand = np

fig,ax = plt.subplots()
plt.plot(np.arange(-5,5,0.2), np.tanh(np.arange(-5,5,0.2))); plt.grid();
st.pyplot(fig)
st.write("This is the graphical representation of micrograd")