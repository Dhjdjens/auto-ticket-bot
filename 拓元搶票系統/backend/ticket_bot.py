from selenium import webdriver
import time

def simulate_ticket_task():
    # ***重要：請自行修改為本機的 test_ticket.html 路徑***
    file_path = "file:///C:/Users/lin/Desktop/拓元搶票系統/test_ticket.html"

    driver = None

    try:
        driver = webdriver.Chrome()  # 啟動 Chrome 瀏覽器（須先安裝 chromedriver）
        driver.get(file_path)  # 載入模擬搶票頁面

        for _ in range(20):  # 最多嘗試點擊按鈕 20 次
            try:
                btn = driver.find_element("id", "buyButton")  # 找按鈕
                if btn.is_displayed():
                    btn.click()  # 按鈕可見就點擊
                    if driver:
                        driver.quit()  # 成功後關閉瀏覽器
                    return "success"  # 回傳成功訊息
            except Exception:
                pass  # 找不到或無法點擊就忽略錯誤繼續嘗試
            time.sleep(1)  # 每次間隔一秒

        if driver:
            driver.quit()  # 嘗試 20 次仍失敗則關閉瀏覽器
        return "fail (按鈕沒出現或點不到)"  # 回傳失敗訊息

    except Exception as e:
        if driver:
            driver.quit()  # 發生錯誤時也要關瀏覽器
        return f"error: {str(e)}"  # 回傳錯誤訊息
