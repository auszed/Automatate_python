from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

# with this will import the options to enable to run Selenium in the background
from selenium.webdriver.chrome.options import Options

# make an executable
import os
import sys


# importing the day and time 
import datetime
import time

# export the file where we are running the file
aplication_path = os.path.dirname(sys.executable)

# select the path we are using
website = "https://www.reuters.com/"

opciones = Options()
opciones.headless = True

# path = "/Users/hanns/OneDriveDocumentos/Automate_with_Python/3_Automate_The_News/chromedriver.exe"
# services = Service(executable_path = path)

# # we run the driver in Selenium 4 to run on the Chrome browser
driver = webdriver.Chrome(r"C:\Users\hanns\OneDrive\Documentos\Data_science_code\codewithmosh\Browser_Automation_Selenium/chromedriver.exe", options = opciones)
# driver = webdriver.Chrome()


# link for the website
driver.get(website)


driver.implicitly_wait(0.2)
# maximaze the window
driver.maximize_window()
# accept all the conditions
accept_terms = driver.find_element(by = "xpath", value='//div[@id="onetrust-button-group"]/button')

driver.implicitly_wait(0.2)
# we click the bottom
accept_terms.click()
driver.implicitly_wait(2)



# import the container of the website
container = driver.find_elements(by = "xpath", value='//div[@data-testid="MediaStoryCard"]')

# add the items in a lists
titles = []
links_a = []


# for look for extracting the element inside the box
for contain in container:
    # older xpath
    # //a[@data-testid="Heading"]/span
    title = contain.find_element(by = "xpath", value = './/a[@data-testid="Heading"]/span').text

    # link_a = contain.find_element(by = "xpath", value = './/a[@data-testid="Heading"]').get_attribute("href")
    link_a = contain.get_attribute("href")

    # append or add the text to the lists
    titles.append(title)
    links_a.append(link_a)

# use a dictionary to add the values from the list to the dictionary
my_dictionay = {'titles': titles, 'links': link_a}

# transform into the pandas format
df_headline = pd.DataFrame(my_dictionay)




print(df_headline)
# add the todays day variable to add to the name of the file
# find the sheetcheet for strftime = https://strftime.org/
# todays_date = datetime.now() 
# # this was other option
todays_date = datetime.date.today() 
#year, month and day
tmd_day = todays_date.strftime('%Y-%m-%d') 
print(tmd_day)
# f'{today_text}_reuters.csv'
file_name = f'{tmd_day}_reuters.csv'
print(file_name)
# final path where we export the .exe file  and the join take care of the path
final_path = os.path.join(aplication_path, file_name)
print(final_path)

# convert to csv
df_headline.to_excel(final_path)
print("sfdf")
# close the driver so the program will stop to work
drive.close()
driver.quit()

csv.writer














