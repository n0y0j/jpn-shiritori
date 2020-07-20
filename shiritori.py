import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup


def shiritori(start_word: str, text: str, answer: bool) -> bool:
    check_text = ""

    if (start_word == text[0]):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        options.add_argument('disable-gpu')
        driver = webdriver.Chrome(
            '/usr/bin/chromedriver', chrome_options=options)
        driver.get('https://ja.dict.naver.com/#/search?query=' + text)

        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")

        hotKeys = soup.select(
            "div.component_keyword.has-saving-function div.row div.origin a.link strong.highlight")

        for key in hotKeys:
            check_text = key.get_text()

            if (text == check_text):
                mean_Keys = soup.select(
                    "div.component_keyword.has-saving-function div.row ul.mean_list li.mean_item p.mean")

                for mKey in mean_Keys:
                    print(mKey.get_text())
                return True
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    with open('hiragana.txt') as file:
        dump = file.readline()
        all_hira = dump.split()

    score = 0
    curr_res = []
    start_word = random.choice(all_hira)
    answer = True

    while True:
        print("시작 단어: " + start_word)
        text = input("단어를 입력하세요: ")

        check = shiritori(start_word, text, answer)

        if check == True:
            score += 1
            start_word = text[-1]

            if len(curr_res) < 5:
                curr_res.append(text)
            else:
                del curr_res[0]
                curr_res.append(text)
            print(curr_res)
        else:
            print(score)
            break
