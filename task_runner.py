from utils import get_driver_with_profile
from selenium.webdriver.common.by import By
import time

def run_task_for_profile(profile_index: int):
    driver = get_driver_with_profile(profile_index)

    try:
        # 🌐 1. Truy cập vào trang DApp
        driver.get("https://example-dapp.com")  # 🟡 THAY bằng URL thật
        print(f"[Profile {profile_index}] 🔗 Opened DApp page")
        time.sleep(3)

        # 🧩 2. Tìm và click nút "Connect Wallet"
        try:
            connect_btn = driver.find_element(By.XPATH, 'PASTE_XPATH_HERE')  # 🟡 THAY bằng XPath thật
            connect_btn.click()
            print(f"[Profile {profile_index}] ✅ Clicked 'Connect Wallet'")
        except Exception as e:
            print(f"[Profile {profile_index}] ❌ Không tìm thấy nút Connect: {e}")

        time.sleep(3)

        # ✍️ 3. (Optional) Xử lý popup MetaMask (nếu DApp bật lên)
        # 👉 Có thể xử lý bằng chuyển tab hoặc phát hiện element trên popup

        # ✅ 4. Làm task khác nếu cần (Claim / Stake / Mint ...)
        # task_btn = driver.find_element(By.XPATH, 'PASTE_TASK_XPATH')
        # task_btn.click()

        time.sleep(5)

    except Exception as e:
        print(f"[Profile {profile_index}] ❌ Lỗi trong quá trình chạy: {e}")

    finally:
        # ✅ Nếu muốn giữ tab mở thì comment dòng dưới
        # driver.quit()
        pass
