import time

from selenium import webdriver

DRIVER_PATH = r'./chromedriver.exe'  # Get your Chrome version compatible driver at root of the project


def get_videos_link(wd: webdriver):
    # allVideosLink = wd.find_elements_by_css_selector(
    #     """#items.style-scope.ytd-grid-renderer ytd-grid-video-renderer.style-scope.ytd-grid-renderer
    #     #dismissible.style-scope.ytd-grid-video-renderer ytd-thumbnail.style-scope.ytd-grid-video-renderer
    #     a.yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail""")

    allVideosLink = wd.find_elements_by_xpath("""//*[@id="video-title"]""")

    return [video.get_attribute("href") for video in allVideosLink]


def get_videos_title(wd: webdriver):
    # allVideosTitle = wd.find_elements_by_css_selector(
    #     """#items.style-scope.ytd-grid-renderer ytd-grid-video-renderer.style-scope.ytd-grid-renderer
    #     #dismissible.style-scope.ytd-grid-video-renderer #details.style-scope.ytd-grid-video-renderer
    #     #meta.style-scope.ytd-grid-video-renderer h3.style-scope.ytd-grid-video-renderer
    #     a.yt-simple-endpoint.style-scope.ytd-grid-video-renderer""")

    allVideosTitle = wd.find_elements_by_xpath("""//*[@id="video-title"]""")

    return [video.text for video in allVideosTitle]


def get_channel_top_videos(channelName):
    baseUrl = "https://www.youtube.com/c"
    videosSection = "videos"

    chrome_driver_path = r'./chromedriver.exe'

    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # For scrapping without opening browser

    with webdriver.Chrome(executable_path=chrome_driver_path, options=option) as wd:
        wd.get(url=f"{baseUrl}/{channelName}/{videosSection}")
        time.sleep(0.5)

        [links, titles] = [get_videos_link(wd), get_videos_title(wd)]

        return [{"video_id": links[i].split("?v=")[1],
                 "video_link": links[i],
                 "video_thumbnail": f"""https://i.ytimg.com/vi/{links[i].split("?v=")[1]}/hqdefault.jpg""",
                 "video_title": titles[i]
                 }
                for i in range(0, len(links))]


if __name__ == '__main__':
    final_data = get_channel_top_videos("SamarpanDasgupta")  # Replace this with targetted channelname

    print(final_data)
    print(len(final_data))
