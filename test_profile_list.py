import os

# Thay bằng đúng đường dẫn máy bạn
user_data_dir = r"C:\Users\machp\AppData\Local\Google\Chrome\User Data"

# Lấy danh sách các folder có tên bắt đầu bằng "Profile" hoặc là "Default"
profiles = [d for d in os.listdir(user_data_dir) if d.startswith("Profile") or d == "Default"]

print("🧩 Danh sách profile Chrome bạn đang có:")
for p in profiles:
    print(" -", p)

print(f"\n🔢 Tổng cộng: {len(profiles)} profile")
