from tkinter import *
from tkinter import ttk, font, filedialog, Entry
from tkinter.messagebox import askokcancel, showinfo, WARNING
import getpass
from PIL import ImageTk, Image
import csv
import pyautogui
import tkcap
import img2pdf
import numpy as np
import time
# -----------------------------
#   OWN SCRIPTS
import read_img
import integrator
def save_results_csv(self):
        with open('historial.csv', 'a') as csvfile:
            w=csv.writer(csvfile, delimiter='-')
            w.writerow([self.text1.get(), self.label, '{:.2f}'.format(self.proba)+'%'])
            showinfo(title='Guardar', message='Los datos se guardaron con éxito.')

def create_pdf(self):
        cap = tkcap.CAP(self.root)
        ID = 'Reporte' + str(self.reportID)+'.jpg'
        img = cap.capture(ID)
        img = Image.open(ID)
        img = img.convert('RGB')
        pdf_path = r'Reporte' + str(self.reportID)+'.pdf'
        img.save(pdf_path)
        self.reportID += 1
        showinfo(title='PDF', message='El PDF fue generado con éxito.')

def delete(self):
        answer = askokcancel(title='Confirmación', message='Se borrarán todos los datos', icon=WARNING)
        if answer:
            self.text1.delete(0, 'end')
            self.text2.delete(1.0, 'end')
            self.text3.delete(1.0, 'end')
            self.text_img1.delete(self.img1, 'end')
            self.text_img2.delete(self.img2, 'end')
            showinfo(title='Borrar', message='Los datos se borraron con éxito')