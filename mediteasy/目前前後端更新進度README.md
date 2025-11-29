

## 📋 專案結構

```
mediteasy/
├── app/
│   ├── analysis/
│   │   └── skin_tone.py          # 膚色分析模組
│   ├── routers/                  # API 路由
│   │   ├── __init__.py
│   │   ├── user.py              # 使用者管理 API
│   │   ├── appointment.py       # 預約管理 API
│   │   ├── ai.py                # AI 問診 API
│   │   └── analysis.py          # 分析功能 API
│   ├── database.py              # 資料庫設定
│   ├── main.py                  # FastAPI 主程式
│   ├── models.py                # 資料模型定義
│   └── utils.py                 # 工具函數
├── .env                         # 環境變數（需自行建立，不包含在版本控制中）
├── pyproject.toml              # 專案依賴配置
├── seed_data.py                # 測試資料生成腳本
└── README.md                    # 本說明文件
```



#### 1. 環境設定

在專案根目錄建立 `.env` 檔案，並填入您的 Google Gemini API Key：

```bash
GOOGLE_API_KEY=your_api_key_here
```

**取得 API Key：**
- 前往 [Google AI Studio](https://makersuite.google.com/app/apikey)
- 登入 Google 帳號
- 建立新的 API Key
- 將 API Key 複製到 `.env` 檔案中

**注意**：`.env` 檔案已加入 `.gitignore`，不會被提交到版本控制系統。

#### 2. 初始化資料庫

```bash
uv run python seed_data.py
```

這會建立測試資料，包括：
- 3 位醫師
- 3 位病患
- 5 筆預約資料
- 1 筆分析紀錄

#### 3. 啟動後端服務

```bash
uv run uvicorn app.main:app --reload
```

服務將在 `http://localhost:8000` 啟動。

#### 4. 查看 API 文檔

在瀏覽器中開啟：http://localhost:8000/docs

## 📡 API 端點

### 使用者管理 (`/api/users`)

- `POST /api/users/register` - 註冊新使用者
- `POST /api/users/login` - 使用者登入
- `GET /api/users/doctors` - 取得所有醫師列表
- `GET /api/users/departments` - 取得所有科別列表
- `DELETE /api/users/{user_id}` - 刪除使用者

### 預約系統 (`/api/appointment`)

- `POST /api/appointment/` - 建立新預約
- `GET /api/appointment/` - 取得所有預約
- `GET /api/appointment/{appointment_id}` - 取得特定預約
- `PATCH /api/appointment/{appointment_id}` - 更新預約
- `DELETE /api/appointment/{appointment_id}` - 刪除預約
- `POST /api/appointment/symptoms` - 提交症狀資訊

### AI 問診 (`/api/ai`)

- `POST /api/ai/chat` - 與 AI 進行問診對話

### 分析功能 (`/api/analysis`)

- `POST /api/analysis/skin-tone` - 膚色分析
- `GET /api/analysis/records` - 取得所有分析紀錄
- `GET /api/analysis/records/{record_id}` - 取得特定分析紀錄




### 資料庫

`med-it-easy.db`


## 🔗 前端整合

本後端服務已與前端（`medplatform`）完整整合：

- **前端位置**：`medplatform/index.html`
- **API 基礎 URL**：`http://localhost:8000`（開發環境）
