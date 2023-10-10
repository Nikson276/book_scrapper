from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_book_link():
    chrome_options = Options()
    # опции, если пытаться скачать через selenium
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "/downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    })

    # user-agent
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

    # for ChromeDriver version 79.0.3945.16 or over
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # headless mode
    chrome_options.add_argument("--headless")

    # Инициализация веб-драйвера
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 2.Переход на сайт
        driver.get("https://baza-knig.ink/")

        # Пример JavaScript функции для получения данных
        # Используйте JavaScript для получения данных JSON с сервера
        # json_data = driver.execute_script("return getJSONData();")

        # # Парсинг JSON и получение значения hittoken
        # parsed_data = json.loads(json_data)
        # hittoken_value = parsed_data["hittoken"]
        # print(f"hittoken: {hittoken_value}")

        # 3.Поиск элемента по классу и клик по ссылке
        short_title_link = driver.find_element(By.CLASS_NAME, "short-title")
        short_title_link.click()

        # Ожидание загрузки страницы с книгой
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tabs"))
            )

        # 4.Клик по блоку внутри вкладки
        tabs_block = driver.find_element(By.CLASS_NAME, "tabs")
        tabs_block.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "create_archive"))
            )

        # 5.ищем class=create_archive, и кликает по нему
        block_to_click = tabs_block.find_element(By.XPATH, ".//button[@class='create_archive']")
        block_to_click.click()

        # 6.Ожидание загрузки блока для скачивания
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ui-dialog-buttonset"))
            )

        # открыли окошко с кнопкой Да
        button_line = driver.find_element(By.CLASS_NAME, "ui-dialog-buttonset")
        # читаем кнопку да и нажимаем
        yes_button = button_line.find_element(By.TAG_NAME, "button")
        yes_button.click()

        # 7.1.Ожидание загрузки окна скачивания
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "info-win")))

        # 7.2.Нахождение ссылки внутри окна и скачивание файла
        link_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#info-win > a"))
            )

        # 7.3. получаем ссылку
        link_href = link_element.get_attribute('href')
        print(f'Ссылка получена: {link_href}')

        # Тут должна идти скачка, с передачей данных сеанса браузера (hittoken)

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    # link = get_book_link()
    get_book_link()

    # не рабочее решение, возвращает код 401
    # response = requests.get(link, stream=True)

    # # Проверить, успешно ли выполнен запрос (код ответа 200)
    # print(response.status_code)
    # if response.status_code == 200:
    #     # Получить имя файла из заголовков ответа (если доступно)
    #     content_disposition = response.headers.get('content-disposition')
    #     if content_disposition:
    #         filename = content_disposition.split("filename=")[1]
    #     else:
    #         # Если имя файла не доступно в заголовках, использовать имя по умолчанию
    #         filename = 'file.txt'
        
    #     # Сохранить файл в локальной папке
    #     with open(filename, 'wb') as f:
    #         for chunk in response.iter_content(chunk_size=8192):
    #             f.write(chunk)
