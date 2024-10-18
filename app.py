import streamlit as st 


st.markdown( "## This is my first website") 

st.write("trying to define my backgroud as green ")


st.write ('hello world')
st.balloons()

with st.form("my_form"):
   st.write("Devine un chiffre")
   my_number = st.slider('choisis en un entre 1 et 15', 1, 15)
   my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   st.form_submit_button('Submit my picks')

st.write(my_number)
st.write(my_color)