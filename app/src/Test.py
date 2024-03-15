import time
import traceback

from Driver import get_driver

from selenium.webdriver.common.by import By



def check_proxy(driver):
    driver.get('http://www.whatismyproxy.com/')
    proxy_check = driver.find_element(By.XPATH, '//div[@class="information"]')
    print(proxy_check.json)



def main():

    driver = get_driver()

    try:
        proxyText = check_proxy(driver)
        print(proxyText)

    except Exception:
        print(traceback.format_exc())

    finally:
        driver.close()
        driver.quit()



if __name__ == "__main__":
    main()