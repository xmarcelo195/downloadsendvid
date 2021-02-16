from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os


options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

links = []

for link in links:
    pos = links.index(link)
    driver.get(link)
    print('baixando video', pos)
    src = driver.find_element_by_id('video_source').get_attribute('src')
    title = driver.find_element_by_class_name('video-title').text
    title = title.replace(' ', '_')

    os.system('ffmpeg -i "{}" -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 {}.mp4'.format(src, title))
    print('baixou ', link)


