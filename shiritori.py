import sys
import random
import requests
from bs4 import BeautifulSoup


def shiritori(start_word: str, text: str, answer: bool) -> bool:
    check_text = ""

    if (start_word == text[0]):
        source = requests.get(
            "https://dic.daum.net/search.do?q=" + text)
        soup = BeautifulSoup(source.content, "lxml")
        hotKeys = soup.select(
            "div.search_cont div.card_word div.search_box div.cleanword_type.kujk_type div.search_cleanword strong.tit_cleansch a.txt_cleansch span.txt_emph1")

        for key in hotKeys:
            check_text = key.get_text()

        if (text == check_text):
            mean_Keys = soup.select(
                "div.search_cont div.card_word div.search_box div.cleanword_type.kujk_type ul.list_search li span.txt_search")

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
    # curr_res = []
    start_word = random.choice(all_hira)
    answer = True

    while True:
        print("시작 단어: " + start_word)
        text = input("단어를 입력하세요: ")

        check = shiritori(start_word, text, answer)

        if check == True:
            score += 1
            start_word = text[-1]
        else:
            print(score)
            break
