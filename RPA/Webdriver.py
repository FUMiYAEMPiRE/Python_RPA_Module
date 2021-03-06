from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from logging import getLogger

logger = getLogger(__name__)


def browser(save_dir: str, headless=False):
    # ダウンロード先指定
    prefs = {"download.default_directory": save_dir}

    # 各種オプション追加
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--lang=ja-JP')
    chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36")

    if headless == True:
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--remote-debugging-port=9222')

    return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
