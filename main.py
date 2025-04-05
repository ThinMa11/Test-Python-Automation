import concurrent.futures
from task_runner import run_task_for_profile
from proxy_util import test_proxy_connectivity, validate_proxy_format

# ======================
# ⚙️ Cấu hình chính
# ======================

# 💡 Số profile chạy song song cùng lúc (điều chỉnh tùy máy)
MAX_CONCURRENCY = 5

# 🧩 Danh sách proxy - dạng IP:PORT hoặc IP:PORT:USER:PASS
proxy_list = [
    "103.180.142.26:48812:huynhlong1320:agzFnzCN",
    "123.45.67.89:8000:user:pass",
    "127.0.0.1:8888",
    # ... tiếp tục thêm
]

# ======================
# ✅ Kiểm tra proxy trước khi chạy
# ======================

validated_proxy_list = []
for i, proxy in enumerate(proxy_list):
    print(f"🔍 Kiểm tra proxy {i}: {proxy}")

    if not validate_proxy_format(proxy):
        print(f"❌ Proxy {i} sai định dạng → Bỏ qua\n")
        continue

    if not test_proxy_connectivity(proxy):
        print(f"⚠️ Proxy {i} không hoạt động → Bỏ qua\n")
        continue

    print(f"✅ Proxy {i} OK → Sử dụng\n")
    validated_proxy_list.append(proxy)

NUM_PROFILES = len(validated_proxy_list)
print(f"\n🚀 Tổng số proxy hợp lệ: {NUM_PROFILES}\n")

if NUM_PROFILES == 0:
    print("🛑 Không có proxy nào dùng được. Dừng chương trình.")
    exit()

# ======================
# 🚀 Chạy các task song song (tối đa MAX_CONCURRENCY cùng lúc)
# ======================

with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as executor:
    futures = []
    for i in range(NUM_PROFILES):
        proxy = validated_proxy_list[i]
        futures.append(executor.submit(run_task_for_profile, i, proxy))

    for future in concurrent.futures.as_completed(futures):
        try:
            future.result()
        except Exception as e:
            print("❌ Lỗi trong một profile:", e)
