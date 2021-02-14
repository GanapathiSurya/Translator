from django.shortcuts import render
from googletrans import Translator
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import easygui
import pytesseract
# Create your views here.
def index(req):
	if req.method=="POST":
		txtEntered=req.POST['txtEntered']
		langChosen=req.POST['langChosen']
		translator=Translator()
		txtOutput = translator.translate(txtEntered,dest=langChosen)
		return render(req,"app/index.html",{"txtEntered":txtEntered,"txtOutput":txtOutput.text,"langChosen":langChosen})
	return render(req,"app/index.html")

def filetranslate(req):
	if req.method=="POST":
		langChoosen = req.POST['langChoosen']
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
		Tk().withdraw()
		#filename = easygui.fileopenbox()
		filename = askopenfilename()
		#var = input()
		#filename="E:\CSITechtonic.png"
		#print(filename)
		#print(pytesseract.image_to_string(filename))
		txtTranslated = pytesseract.image_to_string(filename)
		translator = Translator()
		textOutput = translator.translate(txtTranslated, dest=langChoosen)
	return render(req,"app/index.html",{"textOutput":textOutput.text,"langChoosen":langChoosen})