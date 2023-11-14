###############################################################
#
#   Author: GudiGorazdo
#   Date: 14/10/2023
#   Version: 1.0 alpha
#
#   Description:
#   This library provides basic functions to
#   interact with PowerCute Business Edition v10.0.5
#   web interface.
#
#   PowerChute Business Edition Agent Version-10.0.5.301-EN.x86_64.rpm.
#
###############################################################

import requests
import json
from bs4 import BeautifulSoup

class PowerChute:
def __init__(self, server_ip, port, username, password, pages = ['status', 'batterymanagement', 'diagnostics']):
    self.__server_ip = server_ip
    self.__port = port
    self.__username = username
    self.__password = password
    self.pages = pages
    # Create a session to save cookies and session state
    self.session = requests.Session()
    # Disable TLS warnings (not recommended for production environments)
    requests.packages.urllib3.disable_warnings()

# Authentication using username and password
def __auth(self):
    logon_page = f"https://{self.__server_ip}:{self.__port}/logon"
    r = self.session.get(url=logon_page, verify=False)
    formtoken = BeautifulSoup(r.content, "html.parser").find(id="formtoken").get("value")
    auth_page = f"https://{self.__server_ip}:{self.__port}/j_security_check"
    PARAMS = {
        "j_username": self.__username,
        "j_password": self.__password,
        "formtoken": formtoken,
        "formtokenid": "/logon_formtoken",
        "login": "Log On"
    }
    self.session.post(url=auth_page, data=PARAMS, verify=False)

# De-authenticate the token
def __logoff(self):
    logoff_page = f"https://{self.__server_ip}:{self.__port}/logoff"
    self.session.get(url=logoff_page, verify=False)

# Getting the content of the status page
def __get_page_content(self, page):
    self.__auth()
    status_page = f"https://{self.__server_ip}:{self.__port}/{page}"
    r = self.session.get(url=status_page, verify=False)
    self.__logoff()
    return str(r.content)

# Getting all HTML field IDs
def get_all_html_fields_ids(self, content):
    soup = BeautifulSoup(content, "html.parser")
    elements_with_class_value = soup.find_all(class_="value")  # Find all elements with class 'value'
    fields = [element.get('id') for element in elements_with_class_value if element.get('id')]  # Get a list of IDs of these elements, if they exist
    return fields

# Getting the field value by HTML ID
def get_field_by_html_id(self, content, id):
    element = BeautifulSoup(content, "html.parser").find(id=id)
    if element and element.contents:
        return element.contents[0] if element.contents else "No data"
    else:
        return "Element not found"

def get_all_fields_values_as_json(self):
    all_page_values = {}

    for page in self.pages:
        content = self.__get_page_content(page)
        field_ids = self.get_all_html_fields_ids(content)
        field_values = {}

        for field_id in field_ids:
            try:
                field_value = self.get_field_by_html_id(content, field_id)
                field_values[field_id.replace("value_", "")] = field_value
            except Exception as e:
                print(f"Error getting value for {field_id} on page {page}: {e}")

        all_page_values[page] = field_values

    return json.dumps(all_page_values, ensure_ascii=False)
