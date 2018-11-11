# https://developers.google.com/web/updates/2017/04/headless-chrome?hl=ja
# https://github.com/ebidel/lighthouse-ci/blob/master/builder/Dockerfile
# これ chrome の headless 関係なく webdriver 使ってるっていう話なんじゃ..
# sudo apt-get install chromium-chromedriver
# $ sudo ln -s  /usr/bin/chromedriver
from splinter import Browser

browser = Browser('chrome',
                  executable_path="/usr/lib/chromium-browser/chromedriver",
                  headless=True)

browser.visit('http://www.yahoo.co.jp/')
# browser.html
print(browser.find_by_tag("form").first)
