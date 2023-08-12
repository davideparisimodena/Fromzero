import streamlit as st
import PyPDF2

# Carica il file pdf
uploaded_file = st.file_uploader("Scegli un file PDF", type="pdf")

# Se il file è caricato, leggi il contenuto
if uploaded_file is not None:
   with open('uploaded_file.pdf', 'wb') as f:
        f.write(uploaded_file.getbuffer())
    pdf = PdfReader('uploaded_file.pdf')
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    #pdf_to_text('uploaded_file.pdf')
    #return text 
    st.write(text)

