
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.malt.fr/s?q=java")

cols = ['name', 'title', 'rate', 'skill', 'badge']
df = pd.DataFrame([(1,2,3,4,5)], columns = cols)

i=1
url = "https://www.malt.fr/s?q=java&p=" + str(i)
while True:
    i = i+1
    url = "https://www.malt.fr/s?q=java&p=" + str(i)
    page = driver.get(url)
    page = driver.page_source
    print(url)
    testpage = requests.get(url)
    if testpage.status_code != 200:
        break
    soup = BeautifulSoup(page, 'html.parser')
    name = soup.find_all(class_="profile-card-header__full-name") ###### Name
    titre = soup.find_all(class_="link quiet") ###### Titre
    rate = soup.find_all(class_="profile-card-reputation__rate") ###### Rate
    skill = soup.find_all(class_="profile-card-body__skills malt-tag-list cropped loaded")
    badge_level = soup.find(class_="profile-card__badge-level")

    skills = list()
    for sk in skill:
       skills.append(sk.get_text())

    badges = list()
    for bd in badge_level:
       badges.append(badge_level.get_text())
        
    rates = list()
    for amount in rate:
        rates.append(amount.get_text())

    titles = list()
    for nom in titre:
        titles.append(nom.get_text())
    del(titles[0]) # Drop "Accueuil"

    names = list()
    for nom in name:
        names.append(nom.get_text())

    title_df = pd.DataFrame(titles)
    name_df = pd.DataFrame(names)
    rate_df = pd.DataFrame(rates)
    skill_df = pd.DataFrame(skills)
    badge_df = pd.DataFrame(badges)

    df_to_add = [name_df, title_df, rate_df, skill_df, badge_df]
    df_to_add = pd.concat(df_to_add, axis=1)
    df =  df.append(df_to_add)
