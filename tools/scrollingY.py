import time
from tools.scrapyLinks import scrapyLinks

def scrollingSearchPage(driver):
    # Получаем начальную высоту страницы
    last_height = driver.execute_script("return document.body.scrollHeight")
    number_scrolling = 0
    while True:

        number_scrolling+=1
        print(f'Scrolling: [{number_scrolling}]')

        # Скроллим до конца страницы
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5) # Немного паузы, что бы страница успела прогрузиться
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break  # Если высота страницы не меняется, это означает, что прокрутка достигла низа.
        # Обновляем высоту, если мы еще не в самом низу
        last_height = new_height


               
