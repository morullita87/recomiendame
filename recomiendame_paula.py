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
	
	if pregunta2 == "Medio" :
		imagemedio = Image.open ("rory gilmore.jpg")
		st.image(imagemedio,caption="rory gilmore de la serie gilmore girls")
	
	if pregunta2 == "Baja" :
		imagemedio = Image.open("")
		st.image(imagemedio,caption="")
		
	if pregunta2 == "Alta" :
		imagealta = Image.open("")
		st.image(imagealta,caption="")
	
if pregunta1 == "Extrovertida" :
	imageextro = Image.open("bobesponja.jpg")
	st.image(imageextro,caption="bob esponja")
	
	if pregunta2 == "Medio" :
		imagemedio = Image.open ("lorelai.jpg")
		st.image(imagemedio,caption="lorelai gilmore de la serie las chicas glimore")
	
	if pregunta2 == "Baja" :
		imagemedio = Image.open("sabio blancanieves.jpg")
		st.image(imagemedio,caption="sabio de los siete enanitos")
		
	if pregunta2 == "Alta" :
		imagealta = Image.open("jasmín.jpg")
		st.image(imagealta,caption="la princesa jasmín")
		
