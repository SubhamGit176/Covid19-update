from selenium import webdriver

wait_imp = 10
driver = webdriver.Chrome('/home/subham/chromedriver')


src = 'https://www.worldometers.info/coronavirus/country/india/'

driver.get(src)

driver.implicitly_wait(wait_imp)

new_cases = driver.find_element_by_class_name('news_li')


new_c = new_cases.text.split()[0]

print('New cases : ' + new_c)

deaths = new_cases.text.split()[4]

new_deaths = ''

try:
    if(type(int(deaths[0])) == type(1)):
        new_deaths += deaths
except:
    new_deaths += '0'


print('New deaths : '+new_deaths)
