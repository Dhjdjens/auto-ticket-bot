from selenium import webdriver
import time

def simulate_ticket_task():
    # 重要提醒：把這個路徑改成你電腦上 test_ticket.html 的實際位置
    file_path = "file:///C:/Users/lin/Desktop/拓元搶票系統/test_ticket.html"

    driver = None  # 初始化瀏覽器變數，方便後面關閉用

    try:
        driver = webdriver.Chrome()  # 開啟 Chrome 瀏覽器 (要先裝 chromedriver)
        driver.get(file_path)  # 打開模擬搶票的網頁

        for _ in range(20):  # 最多試點按鈕 20 次
            try:
                btn = driver.find_element("id", "buyButton")  # 找到按鈕元素
                if btn.is_displayed():  # 按鈕是可見狀態
                    btn.click()  # 點擊搶票按鈕
                    if driver:
                        driver.quit()  # 點成功就關掉瀏覽器
                    return "success"  # 回傳成功訊息
            except Exception:
                pass  # 按鈕找不到或點不了就繼續試
            time.sleep(1)  # 每次試間隔 1 秒

        if driver:
            driver.quit()  # 連試 20 次都不成功，還是要關瀏覽器
        return "fail (按鈕沒出現或點不到)"  # 回傳失敗狀態

    except Exception as e:
        if driver:
            driver.quit()  # 碰到其他錯誤，也要確保關掉瀏覽器
        return f"error: {str(e)}"  # 回傳錯誤訊息
