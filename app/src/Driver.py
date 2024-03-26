import Tools

from selenium import webdriver


# from fp.fp import FreeProxy
# from fake_headers import Headers

# def get_headers():
#     header = Headers(
#         browser="chrome",  # Generate only Chrome UA
#         os="linux",  # Generate only Windows platform
#         headers=False # generate misc headers
#     )
#     return header.generate()['User-Agent']

def get_driver(proxy=False, fakeShape=False):

    options=webdriver.ChromeOptions()
    options.page_load_strategy='eager'
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    

    if fakeShape:
        options.add_argument(f"user-agent={Tools.getShape()}")

    # if proxy:
    #     options.add_argument(
    #         '--proxy-server=%s' % FreeProxy(country_id=['BR']).get().split('//')[-1]
    #     )

    driver = webdriver.Remote(
        command_executor='http://10.5.0.2:4444/wd/hub',
        options=options
    )

    return driver