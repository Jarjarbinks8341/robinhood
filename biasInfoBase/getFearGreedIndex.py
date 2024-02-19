from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_dynamic_content(url):                                           

    chrome_driver_path = r'.\chromedriver_linux64\chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_driver_path
    chrome_options.add_argument("--no-sandbox");
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()
    driver.get(url)
    css_selector = 'body > div.layout__content-wrapper.layout-with-rail__content-wrapper > section.layout__wrapper.layout-with-rail__wrapper > section.layout__main-wrapper.layout-with-rail__main-wrapper > section.layout__main.layout-with-rail__main > div > section > div.market-tabbed-container > div.market-tabbed-container__content > div.market-tabbed-container__tab.market-tabbed-container__tab--1 > div > div.market-fng-gauge__overview > div.market-fng-gauge__meter-container > div > div.market-fng-gauge__dial-number > span'
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )
    dynamic_content = driver.page_source
    return dynamic_content

def getFNGIndex(dynamic_content):
    if not dynamic_content:   
        return NULL
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(dynamic_content, 'html.parser')
    extracted_data = []
    spans = soup.find_all('span', {'class':'market-fng-gauge__dial-number-value'})
    lines = [span.get_text() for span in spans]
    return lines[0]

target_url = 'https://edition.cnn.com/markets/fear-and-greed?utm_source=business_ribbon'                            
dynamic_content = scrape_dynamic_content(target_url)
print(getFNGIndex(dynamic_content))
