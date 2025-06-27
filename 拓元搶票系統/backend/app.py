from flask import Flask, request, jsonify 
from flask_cors import CORS
from ticket_bot import simulate_ticket_task  # 這是搶票的核心模擬函式

app = Flask(__name__)
CORS(app)  # 啟用跨域資源分享，前後端才能順利溝通

@app.route("/start-task", methods=["POST"])  # 監聽前端發來啟動搶票任務的請求
def start_task():
    data = request.get_json()  # 取得前端送來的 JSON 資料
    print("收到任務:", data)  # 在終端機印出收到的任務資訊，好追蹤
    result = simulate_ticket_task()  # 呼叫搶票模擬核心，執行搶票動作
    return jsonify({"status": result})  # 回傳搶票結果，讓前端知道成功或失敗

if __name__ == "__main__":
    app.run(debug=True)  # 以除錯模式啟動 Flask，本地測試用
