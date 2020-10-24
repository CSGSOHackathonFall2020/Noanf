from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string


def getStat(n):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome("./driver/chromedriver", chrome_options=options)
        driver.set_page_load_timeout(-1)
    except Exception as e:
        print(e)

    page="https://www.worldometers.info/coronavirus/"
    div_total="maincounter-number"
    div_countries="main_table_countries_today"

    driver.get(page)
    total_stats = driver.find_elements_by_class_name(div_total)
    total_cases = total_stats[0].text
    total_death = total_stats[1].text
    total_recovered = total_stats[2].text

    countries_table = driver.find_elements_by_id(div_countries)[0]
    countries_stats = countries_table.find_elements_by_tag_name('tr')

    stat_per_country=[]

    for i in range(1,n+1):
        country_stats = countries_stats[i].find_elements_by_tag_name('td')
        country=""
        for j in range (0,len(country_stats)):
            if country_stats[j].text=="":
                country=country+" 0"
            else:
                country= country + " " + country_stats[j].text.replace(" ","_")

        stat_per_country.append(country.strip())

    return ([total_cases, total_death, total_recovered, stat_per_country])
