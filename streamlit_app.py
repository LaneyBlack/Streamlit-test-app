import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek

# st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji
st.write("# The German Zug Translator")
st.write("Please rate our app, our we will come and convince you to leave a good rating :)")
st.image('german-tank.jpg', caption='The German Zug')
# Instrukcja i opis aplikacji
st.write("### Instructions:")
st.write("""
1. Enter the text for analysis.
2. Choose an analysis option.
3. View the generated results and analysis based on the input data.
4. Be satisfied with the results, soldier!
""")
st.write("### Goal:")
st.write("""
This app's goal is to succeed in translating British and American communications, to german.
""")

# st.header('Wprowadzenie do zajęć')
# # header to jeden z podtytułów wykorzystywnaych w Streamlit
#
# st.subheader('O Streamlit')
# # subheader to jeden z podtytułów wykorzystywnaych w Streamlit
#
# st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
# # text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.
#
# st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# # write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.
#
# st.code("st.write()", language='python')
# # code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji
#
# with st.echo():
#     st.write("Echo")
# # możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy
#
# df = pd.read_csv("DSP_4.csv", sep =';')
# st.dataframe(df)
# # musimy tylko pamiętać o właściwym określeniu separatora (w tym wypadku to średnik)
# # masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# # os.getcwd() # pokaż bieżący katalog
# # os.chdir("") # zmiana katalogu

st.header('Natural Language Processing')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Choose a function:",
    [
        "Text sentiment analysis (ENG)",
        "Translate from English to German",
    ],
)

if option == "Text sentiment analysis (ENG)":
    text = st.text_area(label="Enter text")
    if text:
        with st.spinner("Analyzing..."):
            classifier = pipeline("sentiment-analysis")
            answer = classifier(text)
        st.success('Successfully analysed!')
        st.write(answer)
elif option == "Translate from English to German":
    text = st.text_area(label="Enter text")
    if text:
        try:
            with st.spinner("Translating..."):
                translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
                translation = translator(text)
                translated_text = translation[0]['translation_text']
            st.success("Translation success")
            st.write("Translated text: ")
            st.write(translated_text)
        except Exception as e:
            st.write('An exception occurred')
            st.write(e)

st.write("### S24382 - Anton Reut")

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/docs/transformers/index')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
