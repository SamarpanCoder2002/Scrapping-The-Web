import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


def get_video_total_likes(wd: webdriver):
    try:
        element = wd.find_element_by_css_selector(
            """a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer 
            #text.style-scope.ytd-toggle-button-renderer.style-text""")

        return element.text
    except:
        return ''


def get_video_publish_date(wd: webdriver):
    try:
        elements = wd.find_elements_by_css_selector(
            """#description-inline-expander span.style-scope.yt-formatted-string.bold""")

        if len(elements) >= 3:
            return elements[2].text
        else:
            return ''

    except:
        return ''


def get_video_description(wd: webdriver):
    try:
        elements = wd.find_elements_by_css_selector(
            """div#description yt-formatted-string""")

        description: str = ''

        for element in elements:
            if len(element.text) > 0:
                description += f"{element.text}\n"

        return description
    except:
        return ''


def get_comments(wd: webdriver):
    elements = wd.find_elements_by_css_selector("#comment #content-text")

    comments_collection: str = ''

    for i in range(len(elements)):
        comments_collection += f'{i+1}) {elements[i].text}\n'

    return comments_collection


def get_video_data(videoId):
    formattedUrl = f"https://www.youtube.com/watch?v={videoId}"

    chrome_driver_path = r'./chromedriver.exe'

    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # For scrapping without opening browser

    with webdriver.Chrome(executable_path=chrome_driver_path, options=option) as wd:
        wd.get(url=formattedUrl)
        wait = WebDriverWait(wd, 5)

        for item in range(3):  # by increasing the highest range you can get more content
            wait.until(EC.visibility_of_element_located(
                (By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(0.5)

        [total_likes, publish_date, description, all_comments] = [
            get_video_total_likes(wd),
            get_video_publish_date(wd),
            get_video_description(wd),
            get_comments(wd)]

        print(f'\n\nLikes: {total_likes}')
        print(f'\n\nPublish Date: {publish_date}')
        print(f'\n\nDescription: {description}')
        print(f'\n\nComments: {all_comments}')


if __name__ == '__main__':
    get_video_data("LXHhwvuBTfw")
