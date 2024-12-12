import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import streamlit as st

st.set_page_config(
    page_title="LinkedIn User Scrapper",  # Título de la pestaña
    page_icon="🌟",  # Ícono de la pestaña
    layout="wide"  # Diseño (opcional)
)

st.title('LinkedIn User Info')
st.subheader('Enter the LinkedIn profile link of the user you want to get the data from')
st.write('This is a simple web scraper that gets the name, location, description, experience, and about section of a LinkedIn user. It uses Selenium to scrape the data and BeautifulSoup to parse the HTML content.')
link = st.text_input('Link')

max_attempts = 3
attemps = 0

if st.button('Get Info'):

    while attemps < max_attempts:
        try: 
            driver = webdriver.Edge()
            driver.get(link)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            about_all = soup.find_all('div', {'class': 'core-section-container__content break-words'})
            def get_about():
                for i in about_all:
                    if len(i.get_text().strip()) < 1000:
                        xd = i.get_text().strip()
                        return xd
            name = soup.find('h1', {'class': "top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0"}).get_text().strip()
            live_in = soup.find('div', {'class': 'not-first-middot'}).find_all('span')[0].get_text().strip()
            description = soup.find('h2', {'class': 'top-card-layout__headline break-words font-sans text-md leading-open text-color-text'}).get_text().strip()
            experience = soup.find_all('span', {'class': 'experience-item__title'})
            companies = soup.find_all('span', {'class': 'experience-item__subtitle'})
            experience = [x.get_text().strip() for x in experience]
            companies = [x.get_text().strip() for x in companies]
            about = get_about()
            driver.close()
            break
        except:
            attemps += 1
    else:

        st.write('An error occurred, please try again later.')

    st.write('**Name:**', name)
    st.write('**Location:**', live_in)
    st.write('**Description:**', description)
    st.write('**Experience:**')
    for i in range(len(experience)):
        st.write(f'{experience[i]} at {companies[i]}')
    st.write('**About**: ', about)
