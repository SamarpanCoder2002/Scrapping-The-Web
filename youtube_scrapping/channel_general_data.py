from selenium import webdriver
import time


def get_channel_name(wd: webdriver):
    element = wd.find_element_by_xpath("""/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[
    3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[
    1]/ytd-channel-name/div/div/yt-formatted-string""")
    return element.text


def get_channel_subscribers(wd: webdriver):
    element = wd.find_element_by_xpath(
        """//*[@id="subscriber-count"]""")
    return element.text


def get_channel_avatar(wd: webdriver):
    elements = wd.find_elements_by_xpath("""//*[@id="img"]""")
    return elements[1].get_attribute("src")


def get_channel_id(wd: webdriver):
    priceValue = wd.find_element_by_xpath("//meta[@itemprop='channelId']")

    return priceValue.get_attribute("content")


def get_channel_about(wd: webdriver):
    element = wd.find_element_by_xpath(
        """/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[
        1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[
        1]/div[1]/yt-formatted-string[2]""")
    return element.text


def yt_channel_general_data(channelName):
    baseUrl = "https://www.youtube.com/c"

    chrome_driver_path = r'./chromedriver.exe'

    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # For scrapping without opening browser

    with webdriver.Chrome(executable_path=chrome_driver_path, options=option) as wd:
        wd.get(url=f"{baseUrl}/{channelName}")
        time.sleep(0.5)

        [channel_name, total_subscribers, channel_avatar, channel_id] = [get_channel_name(wd),
                                                                         get_channel_subscribers(
                                                                             wd),
                                                                         get_channel_avatar(wd), get_channel_id(wd)]

        wd.get(url=f"{baseUrl}/{channelName}/about")
        time.sleep(0.5)

        channel_about_data = get_channel_about(wd)

        channel_general_data = {'channel_id': channel_id, 'channel_name': channel_name,
                                'channel_total_subscribers': total_subscribers, 'channel_avatar': channel_avatar,
                                'channel_about': channel_about_data}

        print(f'Channel general data: {channel_general_data}')


if __name__ == '__main__':
    yt_channel_general_data("""SamarpanDasgupta""")
