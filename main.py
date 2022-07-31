from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import ctypes
import random
import string
import os

hits = 0

def id(chars = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(random.choice([3, 4])))

def logid(path, current):
    assert os.path.isfile(path)
    with open(path, "a") as f:
            f.write(f"avaliable: https://steamcommunity.com/id/{current}\n")

def checkid():
    crandom = id()
    global hits
    ctypes.windll.kernel32.SetConsoleTitleW(f"Steam lowid checker | by fema3832 | Current hits: {str(hits)}")

    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    option.add_argument("disable-logging")
    option.add_argument("log-level=3")
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
    driver.get(f"https://steamcommunity.com/id/{crandom}")

    #* CHECKING AND LOGGING =============================
    if driver.find_element(By.XPATH, r'//*[@id="responsive_page_template_content"]/div').get_property('className') == "error_ctn":
        print(f"https://steamcommunity.com/id/{crandom} is avaliable")
        hits = hits + 1

        if len(crandom) == 3:
            path = fr"{os.path.dirname(os.path.realpath(__file__))}\three.txt"
            logid(path, crandom)
        elif len(crandom) == 4:
            path = fr"{os.path.dirname(os.path.realpath(__file__))}\four.txt"
            logid(path, crandom)
    else:
        print(f"https://steamcommunity.com/id/{crandom} not avaliable")

    ctypes.windll.kernel32.SetConsoleTitleW(f"Steam lowid checker | by fema3832 | Current hits: {str(hits)}")
    driver.quit()
    checkid()

checkid()