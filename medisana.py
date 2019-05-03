import requests
from bs4 import BeautifulSoup
import os
import json

from datetime import date
from functions.readConfig import readConfig

class Medisana:
    def __init__(self):

        cf = readConfig()
        self.config = cf.config
        self.datum = '{:%d-%b-%Y}'.format(date.today())

        dir_path = os.path.dirname(os.path.realpath(__file__))
        folder = os.path.join(dir_path, "data")
        data_file_name = "{}_weights.json".format(self.datum)
        self.data_file =  os.path.join(folder, data_file_name)
        
        self.weight_data = {}
        
        self.start_url = "https://cloud.vitadock.com/signin"
        self.login_url = "https://cloud.vitadock.com/resources/j_spring_security_check"
        self.weight_page = "https://cloud.vitadock.com/portal/target.php?lang=nl_NL"
        self.weight_json = "https://cloud.vitadock.com/portal/server/target_server.php?lang=nl_NL&rnd=12345"

        self.get_data()


    def get_data(self, file=None):
        if file is not None:
            self.data_file = file
        
        exists = os.path.isfile(self.data_file)
        if exists:
            print('Found pagespeed json file')
            
            file = os.path.basename(self.data_file)
            file_date = file.split("_")
            
            if file_date[0] == self.datum:
                print('Using data from pagespeed json file')
                self.weight_data = self.open_file_with_contents()
                return 
    
        print('get data from medisana')
        self.weight_data = self.get_data_from_url()
        if self.weight_data is not None:
            print('Create file with medisana json file')
            self.save_file_with_contents()
        
    def get_data_from_url(self):
        
        s = requests.Session()  # Set session for cookies
        r = s.get(self.start_url)   # Get first page for the csrf code (generated each time)
        soup = BeautifulSoup(r.content, 'html.parser')
    
        csrf = soup.find('input', {'name': '_csrf'}).get('value')   # get the csrf data from the input field

        data = {"j_username": self.config['username'], "j_password": self.config['password'], "_spring_security_remember_me": "", "oauth_token": "", "marketingid": "", "code": "", "loginBtn": "Log in", "_csrf": csrf  }
        
        r = s.post(self.login_url, data=data)   #login to the site
        r = s.get(self.weight_page)  # get the weight page, needed before you can grab the json
        r = s.get(self.weight_json)  # get the json weight file!
        return r.json()

    def open_file_with_contents(self, file=None):
        if file is not None:
            self.data_file = file
            
        with open(self.data_file, 'r') as json_file:
            return json.load(json_file)

    def save_file_with_contents(self, file=None):
        if file is not None:
            self.data_file = file

        with open(self.data_file, 'w+') as output:
            json.dump(self.weight_data, output)

if __name__ == '__main__':
    m = Medisana()