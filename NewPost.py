from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import time
import re, datetime
import instapy
import autoit
import pathlib
from PIL import Image, ImageDraw, ImageFont
from matplotlib.pyplot import imshow
from matplotlib.pyplot import figure
import numpy as np
from shutil import copyfile
from time import gmtime, strftime

def newPost(uname,passwd,post_caption):
    #try:
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    mobile_emulation = {"deviceName": "iPhone 8"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome("./driver/chromedriver", chrome_options=options)
    driver.set_page_load_timeout(-1)
    #except Exception as e:
    #    print(e)

    page="https://www.instagram.com/accounts/login/?hl=en"
    driver.get(page)
    time.sleep(4)
    userID = driver.find_element_by_name("username")
    #userID.send_keys('covid.times')
    userID.send_keys(uname)
    Password = driver.find_element_by_name("password")
    Password.send_keys(passwd)
    Password.send_keys(u'\ue007')
    time.sleep(4)
    try:
        Cancel = driver.find_element_by_class_name("aOOlW.HoLwm ")
        Cancel.click()
        time.sleep(3)
    except Exception as e:
        print(e)
    try:
        NotNow = driver.find_element_by_class_name("cmbtv")
        NotNow.click()
        time.sleep(3)
    except Exception as e:
        print(e)
    try:
        Cancel = driver.find_element_by_class_name("aOOlW.HoLwm")
        Cancel.click()
        time.sleep(3)
    except Exception as e:
        print(e)
    try:
        NotNow = driver.find_element_by_class_name("cmbtv")
        NotNow.click()
        time.sleep(3)
    except Exception as e:
        print(e)
    try:
        NotNow = driver.find_element_by_class_name("aOOlW.HoLwm")
        NotNow.click()
        time.sleep(3)
    except Exception as e:
        print(e)
    NewPost = driver.find_element_by_class_name("q02Nz._0TPg")
    NewPost.click()
    time.sleep(3)


    autoit.win_active("Open")
    time.sleep(2)
    #ImagePath=str(pathlib.Path().absolute()) + "\\test.png"
    ImagePath="stat.png"
    autoit.control_send("Open","Edit1",ImagePath)
    time.sleep(1)
    autoit.control_send("Open","Edit1","{ENTER}")
    time.sleep(3)

    Next = driver.find_element_by_class_name("UP43G")
    Next.click()
    time.sleep(3)

    Caption = driver.find_element_by_class_name("_472V_")
    Caption.send_keys(post_caption)

    Share = driver.find_element_by_class_name("UP43G")
    Share.click()
    time.sleep(5)

    driver.close()

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

def createImage(total_cases, total_death, total_recovered, stat_per_country):

    img = Image.open('sample.png')
    fnt = ImageFont.truetype('Arial.ttf', 50)
    texts = ImageDraw.Draw(img)

    texts.text((70,290), total_cases, font=fnt, fill=(255, 42, 42))
    texts.text((70,415), total_death, font=fnt, fill=(128, 128, 128))
    texts.text((70,535), total_recovered, font=fnt, fill=(89, 131, 29))

    stat_day = time.strftime("%A", time.gmtime())
    stat_date = time.strftime("%d %b %Y", time.gmtime())
    stat_time = time.strftime("%I:%M\n  %p", time.gmtime())

    texts.text((30,205), stat_day, font=ImageFont.truetype('Arial.ttf', 30), fill=(80, 80, 80))
    texts.text((190,205), stat_date, font=ImageFont.truetype('Arial.ttf', 30), fill=(80, 80, 80))
    #texts.text((660,190), stat_time, font=ImageFont.truetype('Arial.ttf', 24), fill=(80, 80, 80))

    texts.text((410,310), "Country", font=ImageFont.truetype('Arial.ttf', 17), fill=(40, 40, 40))
    texts.text((530,300), "Total\ncases", font=ImageFont.truetype('Arial.ttf', 17), fill=(40, 40, 40))
    texts.text((600,300), "Total\ndeaths", font=ImageFont.truetype('Arial.ttf', 17), fill=(40, 40, 40))
    texts.text((670,300), "Cases\nper M", font=ImageFont.truetype('Arial.ttf', 17), fill=(40, 40, 40))
    texts.text((740,300), "Deaths\nper M", font=ImageFont.truetype('Arial.ttf', 17), fill=(40, 40, 40))

    texts.text((400,325), "_____________________________________________", font=ImageFont.truetype('Arial.ttf', 16), fill=(160, 160, 160))

    pos_vertical=350
    print(stat_per_country)
    counter=1
    for country_string in stat_per_country:
        if counter==23:
            break

        country_stats = country_string.split(" ")
        if str(country_stats[0])=="0":
            continue
        texts.text((410,pos_vertical), country_stats[1].replace("_"," "), font=ImageFont.truetype('Arial.ttf', 17), fill=(40, 40, 40))
        pos_horizontal=530
        for i in [2,4,9,10]:
            #print(str(i) + ": " + country_stats[i])
            #print(str(pos_horizontal)+ " : " + str(pos_vertical))
            texts.text((pos_horizontal,pos_vertical), country_stats[i].replace("_"," "), font=ImageFont.truetype('Arial.ttf', 15), fill=(80, 80, 80))
            pos_horizontal=pos_horizontal+70

        pos_vertical=pos_vertical+20
        counter=counter+1
    figure(figsize=(5,5))
    imshow(np.asarray(img), aspect='equal')


    img.save('stat.png')

    
[total_cases, total_death, total_recovered, stat_per_country] = getStat(30)
#print(stat_per_country)
createImage(total_cases, total_death, total_recovered, stat_per_country)
