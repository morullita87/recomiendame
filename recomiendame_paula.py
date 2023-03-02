import streamlit as st
from PIL import Image
import random

st.header = ("¿A QUÉ PERSONAJE TE PARECES?")

opciones1 = ("Introvertida","Extrovertida")
pregunta1 = st.radio("Me describiría una persona...",opciones1)

opciones2 = ("Baja","Medio","Alta")
pregunta2 = st.radio("¿Cuál es tu nivel socioeconómico?",opciones2)

if pregunta1 == "Introvertida" :
	image = Image.open("eleven.jpg")
	st.image(image,caption="Eleven de la serie stranger things")
	
if pregunta1 == "Extrovertida" :
	imageextro = Image.open("bobesponja.jpg")
	st.image(imageextro,caption="bob esponja")
	
	if pregunta2 == "Medio" :
		imagemedio = Image.open ("lorelai.jpg")
		st.image(imagemedio,caption=("lorelai gilmore de la serie gilmore girls")
		
	elif pregunta2 == "Baja":
		imagealta = Image.open("doc sieteenanitos.png)
		st.image(imagealta,caption="Sabio de los siete enanitos")
	

