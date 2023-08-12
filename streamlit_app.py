import streamlit as st
import PyPDF2

# Carica il file pdf
uploaded_file = st.file_uploader("Scegli un file PDF", type="pdf")

# Se il file è caricato, leggi il contenuto
if uploaded_file is not None:
    # Crea un oggetto PdfFileReader dal file caricato
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    # Ottieni il numero di pagine del pdf
    num_pages = pdf_reader.numPages
    # Inizializza una lista vuota per contenere il testo di ogni pagina
    pages = []
    # Itera su ogni pagina e aggiungi il testo alla lista
    for i in range(num_pages):
        page = pdf_reader.getPage(i)
        text = page.extractText()
        pages.append(text)
    # Unisci il testo di tutte le pagine in una stringa
    pdf_text = "\n".join(pages)
    # Mostra il testo del pdf
    st.write(pdf_text)

