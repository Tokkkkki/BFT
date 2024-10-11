from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')

driver = webdriver.Chrome(options=chrome_options)

def wait_and_find_element(by, value, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
    except TimeoutException:
        return None

try:
    # Проверка 1: Открытие главной страницы Pinterest
    driver.get("https://ru.pinterest.com/")
    print(f"Текущий URL: {driver.current_url}")
    print(f"Заголовок страницы: {driver.title}")
    assert "Pinterest" in driver.title, "Неожиданный заголовок страницы"
    print("Проверка 1: Успешно открыта главная страница Pinterest")

    # Проверка 2: Проверка наличия формы входа
    login_form = wait_and_find_element(By.CSS_SELECTOR, "form")
    if login_form:
        print("Проверка 2: Форма входа найдена")
    else:
        raise AssertionError("Форма входа не найдена")

    # Проверка 3: Проверка наличия логотипа Pinterest
    logo = wait_and_find_element(By.CSS_SELECTOR, "[class*='logo']")
    if logo:
        print("Проверка 3: Логотип Pinterest найден")
    else:
        raise AssertionError("Логотип Pinterest не найден")

    # Проверка 4: Проверка наличия ссылок на мобильные приложения
    app_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'store')]")
    if app_links:
        print(f"Проверка 4: Найдено {len(app_links)} ссылок на мобильные приложения")
    else:
        raise AssertionError("Ссылки на мобильные приложения не найдены")

    # Проверка 5: Проверка наличия текста о мобильных устройствах
    mobile_text = wait_and_find_element(By.XPATH, "//*[contains(text(), 'mobile') or contains(text(), 'мобил')]")
    if mobile_text:
        print("Проверка 5: Найден текст о мобильных устройствах")
    else:
        raise AssertionError("Текст о мобильных устройствах не найден")

    print("Тест успешно завершен!")

except AssertionError as e:
    print(f"Тест не пройден: {str(e)}")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")

finally:
    print(f"Финальный URL: {driver.current_url}")
    print("Структура страницы:")
    elements = driver.find_elements(By.XPATH, "//*")
    for element in elements[:10]:  # Выводятся первые 10 элементов
        print(f"Тег: {element.tag_name}, Класс: {element.get_attribute('class')}, Текст: {element.text[:30]}...")
    driver.quit()



'''
Текущий URL: https://ru.pinterest.com/
Заголовок страницы: Pinterest – Пинтерест
Проверка 1: Успешно открыта главная страница Pinterest
Проверка 2: Форма входа найдена
Проверка 3: Логотип Pinterest найден
Проверка 4: Найдено 1 ссылок на мобильные приложения
Проверка 5: Найден текст о мобильных устройствах
Тест успешно завершен!
Финальный URL: https://ru.pinterest.com/
Структура страницы:
Тег: html, Класс: ru fp-enabled, Текст: Pinterest
Просмотреть
Описание...
Тег: head, Класс: , Текст: ...
Тег: meta, Класс: , Текст: ...
Тег: meta, Класс: , Текст: ...
Тег: meta, Класс: , Текст: ...
Тег: meta, Класс: , Текст: ...
Тег: meta, Класс: , Текст: ...
Тег: script, Класс: , Текст: ...
Тег: script, Класс: , Текст: ...
Тег: script, Класс: , Текст: ...
'''