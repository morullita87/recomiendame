import streamlit as st
from PIL import Image
import random

st.title("¿A QUÉ PERSONAJE TE PARECES?:sunglasses::slightly-happy")

opciones1 = ("Introvertida","Extrovertida")
pregunta1 = st.radio("Me describiría una persona...",opciones1)

opciones2 = ("Baja","Medio","Alta")
pregunta2 = st.radio("¿Cuál es tu nivel socioeconómico?",opciones2)

if pregunta1 == "Introvertida" :
	image = Image.open("eleven.jpg")
	st.image(image,caption="Eleven de la serie stranger things")
	
	if pregunta2 == "Medio" :
		imagemedio = Image.open ("rory gilmore.jpg")
		st.image(imagemedio,caption="Rory gilmore de la serie gilmore girls")
	
	if pregunta2 == "Baja" :
		imagemedio = Image.open("pumbareyleon.jpg")
		st.image(imagemedio,caption="Pumba de la película el rey león")
		
	if pregunta2 == "Alta" :
		imagealta = Image.open("Li Shang.png")
		st.image(imagealta,caption="Li Shang de la película Mulán")
	
if pregunta1 == "Extrovertida" :
	imageextro = Image.open("bobesponja.jpg")
	st.image(imageextro,caption="Bob esponja")
	
	if pregunta2 == "Medio" :
		imagemedio = Image.open ("lorelai.jpg")
		st.image(imagemedio,caption="lorelai gilmore de la serie las chicas glimore")
	
	if pregunta2 == "Baja" :
		imagemedio = Image.open("sabio blancanieves.jpg")
		st.image(imagemedio,caption="sabio de los siete enanitos")
		
	if pregunta2 == "Alta" :
		imagealta = Image.open("jasmín.jpg")
		st.image(imagealta,caption="la princesa jasmín")
		
