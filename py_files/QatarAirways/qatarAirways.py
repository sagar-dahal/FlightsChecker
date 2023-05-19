import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os


class QatarAirways(webdriver.Chrome):
    def __init__(self, driver_path='D:\CODES\selenium\chromedriver'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(QatarAirways, self).__init__()
        self.implicitly_wait(30)
        self.maximize_window()
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.url = 'https://www.qatarairways.com/en-us/homepage.html'
    
    def land_first_page(self):
        self.get(self.url)
        cookieAcceptBtn = self.find_element(By.ID, 'cookie-close-accept-all')
        cookieAcceptBtn.click()
    
    def enterOrigin(self, origin):
        originField = self.find_element(By.ID, 'bw-from')
        originField.send_keys(f'{origin}')
        originField.send_keys(Keys.ARROW_DOWN)
        originField.send_keys(Keys.ENTER)
    
    def enterDestination(self, destination):
        destinationField = self.find_element(By.ID, 'bw-to')
        destinationField.send_keys(f'{destination}')
        destinationField.send_keys(Keys.ARROW_DOWN)
        destinationField.send_keys(Keys.ENTER)
    
    def enterTripType(self, tripType='onewayTrip'):
        dropdown = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.ID, "tripType")))
        dropdown.click()
        option = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.ID, tripType)))
        option.click()

    def departDate(self, date):
        month = date.split('-')[1]
        month = int(month.lstrip('0'))-1
        month = self.months[month]
        monthRange = self.find_element(By.XPATH, f"//a[contains(@data-month1, '{month}') or contains(@data-month2, '{month}')]")
        monthRange.click()
        dateSelected = self.find_element(By.CSS_SELECTOR, f'td[data-t-fulldate="{date}"]')
        dateSelected.click()
        continueBtn = self.find_element(By.CSS_SELECTOR, 'button.btn.btn-dark.confirmBtn')
        self.execute_script("arguments[0].click();", continueBtn)
    
    def showFlights(self):
        submitBtn = self.find_element(By.CSS_SELECTOR, 'div.formsubmit')
        submitBtn.click()
    
    def getResult(self):
        flights = self.find_elements(By.TAG_NAME, 'booking-flight-result-card')
        self.flightLists = []
        for flight in flights:
            flightDetails = {}
            try:
                departTime = (flight.find_element(By.CSS_SELECTOR, 'h3.at-flight-card-depart-time')).get_attribute('innerHTML')
                arrivalTime = (flight.find_element(By.CSS_SELECTOR, 'span.at-flight-card-arrival-time')).get_attribute('innerHTML')
                stopInfo = flight.find_element(By.CSS_SELECTOR, 'p.flight-card__stop-info').get_attribute('innerHTML')
                flightDetails['Total Time'] = stopInfo.replace('<!---->', '')
                flightDetails['departTime'] = departTime
                flightDetails['arrivalTime'] = arrivalTime

                classes = flight.find_elements(By.CSS_SELECTOR, 'div.ng-star-inserted')
                for cls in classes:
                    clsType = cls.find_element(By.CSS_SELECTOR, 'h5 span').get_attribute('innerHTML')
                    price = cls.find_element(By.CSS_SELECTOR, 'h3 span').get_attribute('innerHTML')
                    price = int(''.join(c for c in price if c.isdigit()))
                    flightDetails[clsType] = price
                
                self.flightLists.append(flightDetails)
            except:
                print('Some error')
        self.flightLists = sorted(self.flightLists, key = lambda k: k['Economy'])
        return self.flightLists