import streamlit as st
from PIL import Image
import random

st.title("¿A QUÉ PERSONAJE TE PARECES?:sunglasses:")

opciones1 = ("Introvertida","Extrovertida")
pregunta1 = st.radio("Me describiría una persona...",opciones1)

opciones2 = ("Baja","Medio","Alta")
pregunta2 = st.radio("¿Cuál es tu nivel socioeconómico?",opciones2)

opciones3 = ("Dejarte llevar","Planificarte")
pregunta3 = st.radio("Prefieres:",opciones3)

if pregunta1 == "Introvertida" :
	image = Image.open("eleven.jpg")
	st.image(image,caption="Eleven de la serie stranger things")
	
	if pregunta2 == "Medio" :
		imagemedio = Image.open ("rory gilmore.jpg")
		st.image(imagemedio,caption="Rory gilmore de la serie gilmore girls")
	
	if pregunta2 == "Baja" :
		imagebruno = Image.open("bruno.jpg")
		st.image(imagebruno,caption="Bruno Madrigal de la película Encanto")
		
	if pregunta2 == "Alta" :
		imagealta = Image.open("Li Shang.png")
		st.image(imagealta,caption="Li Shang de la película Mulán")
	
if pregunta1 == "Extrovertida" :
	imageextro = Image.open("bobesponja.jpg")
	st.image(imageextro,caption="Bob esponja")
	
	if pregunta2 == "Medio" :
		imagelorelai = Image.open ("lorelai.jpg")
		st.image(imagelorelai,caption="lorelai gilmore de la serie las chicas glimore")
		
		if pregunta3 == "Dejarte llevar" :
			st.image(imagelorelai,caption="lorelai gilmore de la serie las chicas glimore")
		
		else :
			imagehermione = Image.open ("hermione.jpg")
			st.image(imagehermione,caption="Hermione de Harry Potter")
		
	if pregunta2 == "Baja" :
		imagemedio = Image.open("sabio blancanieves.jpg")
		st.image(imagemedio,caption="sabio de los siete enanitos")
		
		if pregunta3 == "Dejarte llevar" :
			imagecenicienta = Image.open("cenicienta.png")
			st.image(imagecenicienta,caption="La princesa cenicienta al principio")
			
		else :
			st.image(imagemedio,caption="sabio de los siete enanitos")
		
	if pregunta2 == "Alta" :
		imagealta = Image.open("jasmín.jpg")
		st.image(imagealta,caption="la princesa jasmín")
		
		if pregunta3 == "Dejarte llevar" :
			st.image(imagealta,caption="la princesa jasmín")
		
		else :
			imageemily = Image.open ("emily.jpeg")
			st.image(imageemily,caption="Emily Gilmore de las chicas gilmore")
		
		

		
