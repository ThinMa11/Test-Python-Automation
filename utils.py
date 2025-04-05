import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from proxy_util import create_proxy_extension  # 👈 Import từ file proxy_util.py

def get_driver_with_profile(profile_index: int, proxy: str = None) -> webdriver.Chrome:
    chrome_options = Options()

    # 📁 Đường dẫn tới thư mục profile của Chrome
    user_data_dir = r"C:\Users\machp\AppData\Local\Google\Chrome\User Data"
    profile_dir = f"Profile {profile_index}"  # hoặc "Default" nếu là profile gốc

    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument(f"--profile-directory={profile_dir}")
    chrome_options.add_argument("--start-maximized")

    # 🧩 Nếu có proxy thì xử lý
    if proxy:
        parts = proxy.strip().split(":")
        ip, port = parts[0], parts[1]

        if len(parts) == 4:
            username, password = parts[2], parts[3]
            ext_path = f"proxy_auth_ext_{profile_index}.zip"
            create_proxy_extension(ip, port, username, password, ext_path)
            chrome_options.add_extension(ext_path)
        else:
            chrome_options.add_argument(f"--proxy-server={ip}:{port}")

    # 🔒 Tránh bị detect là bot
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # 🚀 Tạo trình duyệt
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
