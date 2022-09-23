from bs4 import BeautifulSoup
import requests

from selenium import webdriver

chrome_drive_path_link = "D:/chromedriver.exe"
google_form_link = "https://forms.gle/16Bs75itt6Fe9sV56"
zillow_link = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
              "%22mapBounds%22%3A%7B%22west%22%3A-122.8563026328125%2C%22east%22%3A-122.0103553671875%2C%22south%22" \
              "%3A37.63132609046918%2C%22north%22%3A37.91897701912%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22" \
              "%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B" \
              "%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C" \
              "%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value" \
              "%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C" \
              "%22isListVisible%22%3Atrue%7D "

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/61.0.3163.100 Safari/537.36 '
}

response = requests.get(url=zillow_link, headers=req_headers)
data = response.content

soup = BeautifulSoup(data, "html.parser")
rent_data = soup.find(name="ul", class_="photo-cards photo-cards_wow photo-cards_short")

data_2 = rent_data.select(selector="li article")
total_address = []
total_links = []
total_price = []
for each_data in data_2:
    try:
        data_1 = (each_data.find(name="div", class_="list-card-info"))
        address = data_1.select_one(selector="address").text
        link = data_1.select_one(selector="a").get_attribute_list("href")[0]
        price = data_1.find(name="div", class_="list-card-price").text
        if "http" not in link:
            final_link = "https://www.zillow.com/" + link
        else:
            final_link = link
        total_price.append(price)
        total_links.append(final_link)
        total_address.append(address)
    except AttributeError:

        continue
# this to fill the google form
driver = webdriver.Chrome(chrome_drive_path_link)
for i in range(len(total_price)):
    driver.get(google_form_link)

    address_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div['
                                                 '2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(total_address[i])

    price_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div['
                                               '2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(total_price[i])

    link_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div['
                                              '2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(total_links[i])

    submit_botton = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div')
    submit_botton.click()
