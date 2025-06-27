from flask import Flask, request, jsonify 
from flask_cors import CORS
from ticket_bot import simulate_ticket_task # 模擬搶票任務（核心功能）

app = Flask(__name__)
CORS(app) # 啟用 CORS，解決前後端跨域問題

@app.route("/start-task", methods=["POST"]) # 接收前端啟動任務的請求
def start_task():
    data = request.get_json() 
    print("收到任務:", data) # 
    result = simulate_ticket_task() 
    return jsonify({"status": result}) # ✅ 核心：執行搶票模擬

if __name__ == "__main__":
    app.run(debug=True) # 啟動本地伺服器（開發階段用）
