## 📋 專案結構

```
medplatform/
├── index.html          # 主要前端應用程式
├── .vscode/
│   └── settings.json   # VS Code 設定（Live Server 端口配置）
└── README.md          # 本說明文件
```


### 配置後端 API 地址

預設後端 API 地址為 `http://localhost:8000`。

**部署時修改：**
1. 開啟 `index.html`
2. 找到以下程式碼：
```javascript
const API_BASE_URL = "http://localhost:8000";
```
3. 修改為實際的後端服務地址：
```javascript
const API_BASE_URL = "https://your-backend-domain.com";
```

## 🎯 功能說明

### 1. 使用者註冊與登入

- **註冊**：新使用者可以註冊帳號
- **登入**：已註冊使用者可以登入系統
- **狀態持久化**：登入狀態會保存在瀏覽器的 `localStorage` 中

### 2. 預約掛號

- 選擇科別和醫師
- 選擇預約日期和時間
- 提交預約後會獲得預約 ID

### 3. 症狀填寫

- 填寫症狀描述
- 選擇持續時間和嚴重程度
- 選擇多個症狀選項
- 上傳正面照片（JPG 格式）用於 AI 分析
- 填寫額外備註

### 4. AI 問診

- 與 AI 進行對話式問診
- AI 會根據症狀提供初步建議
- 對話記錄會保存在瀏覽器中


### 狀態管理

前端使用 React `useState` 和 `useEffect` 管理狀態，並使用 `localStorage` 持久化以下資料：

- `currentUser`：當前登入的使用者資訊
- `isLoggedIn`：登入狀態
- `currentAppointmentId`：當前預約 ID
- `conversation`：AI 問診對話記錄
- `activeFeature`：當前啟用的功能頁面

### API 整合

前端透過以下 API 端點與後端通訊：

- `POST /api/users/register` - 註冊
- `POST /api/users/login` - 登入
- `GET /api/users/doctors` - 取得醫師列表
- `GET /api/users/departments` - 取得科別列表
- `POST /api/appointment/` - 建立預約
- `POST /api/appointment/symptoms` - 提交症狀
- `POST /api/analysis/skin-tone` - 上傳照片進行膚色分析
- `POST /api/ai/chat` - AI 問診對話



