import time

from selenium import webdriver

# Get your Chrome version compatible driver at root of the project
DRIVER_PATH = r'./chromedriver.exe'


def get_videos_link(wd: webdriver):
    allVideosLink = wd.find_elements_by_xpath("""//*[@id="video-title"]""")

    return [video.get_attribute("href") for video in allVideosLink]


def get_videos_title(wd: webdriver):

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
                 "video_thumbnail": f"""https://i.ytimg.com/vi/{links[i].split("?v=")[1]}/maxresdefault.jpg""",
                 "video_title": titles[i]
                 }
                for i in range(0, len(links))]


if __name__ == '__main__':
    video_collection = get_channel_top_videos("SamarpanDasgupta")

    for i in range(len(video_collection)):
        print(f"""{i+1}) {video_collection[i]}""", end="\n\n")
