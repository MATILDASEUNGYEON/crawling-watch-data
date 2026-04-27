from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# 1. 브라우저 설정
options = webdriver.ChromeOptions()
# options.add_argument('--headless') # 창을 띄우지 않고 실행하려면 주석 해제
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    url = "https://www.gugus.co.kr/goodsList/viewCategoryGoodsList?categoryNo=300&searchTerm=%EC%8B%9C%EA%B3%84"
    driver.get(url)

    # 2. 'info-box'가 나타날 때까지 최대 10초 대기 (중요!)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "info-box")))

    # 3. 로드된 전체 페이지 소스 가져오기
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    items = soup.select('.info-box')

    print(f"찾은 상품 개수: {len(items)}")

    for item in items:
        brand = item.select_one('.brand').get_text(strip=True)
        title = item.select_one('.title').get_text(strip=True)
        print(f"[{brand}] {title}")

finally:
    time.sleep(3) # 눈으로 확인하기 위해 잠시 대기
    driver.quit()