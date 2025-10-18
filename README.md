# 棧板儲位配對掃描 App (Pallet Location Pairing Scanner)

一個用於實時配對和追蹤棧板與儲位的行動掃描應用程式。

## 🎯 功能摘要

- **即時條碼掃描**：支援 QR Code 和 CODE_128 條碼掃描
- **棧板與儲位配對**：輕鬆掃描並記錄棧板 ID 和儲位 ID 的配對關係
- **實時資料同步**：使用 Firebase Firestore 即時同步資料，支援多用戶協作
- **紀錄管理**：查看所有配對紀錄，支援刪除錯誤紀錄
- **資料匯出**：一鍵匯出所有配對紀錄為 CSV 格式
- **行動友好**：完全響應式設計，適配手機和平板

## 🚀 快速開始

### 本地開發

1. **複製倉庫**
   ```bash
   git clone https://github.com/kennyyytu0328/PalletLocationPairing.git
   cd PalletLocationPairing
   ```

2. **啟動本地伺服器**
   ```bash
   python start_server.py
   ```
   或使用 Python 預設 HTTP 伺服器：
   ```bash
   python -m http.server 8000
   ```

3. **存取應用程式**
   - 本地：`http://localhost:8000`
   - 網路：`http://<your-local-ip>:8000`
   - GitHub Pages：`https://your-github-account.github.io/PalletLocationPairing/`

### 登入方式

應用程式使用簡單的密碼認證機制：

1. 打開應用程式時會顯示登入介面
2. 輸入共享密碼：測試環境直接寫死於HTML
3. 輸入您的使用者名稱（可選，用於記錄操作者）
4. 點擊「進入應用程式」按鈕

> **安全提示**：此密碼僅用於本地開發和演示。生產環境應實施更安全的認證方案。

## ⚙️ 使用限制

### 外部資源依賴

| 資源 | 用途 | 依賴 | 備註 |
|------|------|------|------|
| **Firebase** | 資料存儲與同步 | 需要網路連線 | 使用 Firestore 即時資料庫 |
| **Tailwind CSS** | UI 樣式框架 | CDN 載入 | 需要網路連線 |
| **Lucide Icons** | 圖示庫 | CDN 載入 | 需要網路連線 |
| **ZXing Library** | 條碼掃描 | CDN 載入 | 需要網路連線 |

### 功能限制

#### 相機存取
- ✅ **支援環境**
  - HTTPS 連線
  - `http://localhost:*` (本地 HTTP)
  - Android Chrome（需啟用相機權限）

- ❌ **不支援環境**
  - `file://` 協議（本地檔案打開）
  - 非 HTTPS 的遠端 HTTP（例如 `http://192.168.1.x`）
  - iOS Safari（需特殊設定）

> **解決方案**：如需在非 localhost 的 HTTP 環境中使用相機，建議使用 HTTPS 或 ngrok 建立安全通道。

#### 瀏覽器支援
- ✅ Chrome/Edge（推薦）
- ✅ Firefox
- ⚠️ Safari（iOS 需要額外設定）

#### 儲存空間
- 紀錄存儲於 Firebase Firestore
- 無本地儲存限制

## 📋 系統需求

### 客戶端
- 現代瀏覽器（Chrome、Firefox、Safari）
- 相機裝置（用於條碼掃描）
- 網路連線（Firebase 同步）

### 伺服器（開發環境）
- Python 3.6+
- 無額外依賴（使用 Python 內建 `http.server`）

## 🔧 技術棧

- **前端框架**：Vanilla JavaScript（無框架依賴）
- **樣式**：Tailwind CSS
- **圖示**：Lucide Icons
- **條碼掃描**：ZXing Library
- **後端**：Firebase (Firestore + Authentication)
- **部署**：GitHub Pages

## 📁 檔案結構

```
PalletLocationPairing/
├── index.html                          # 首頁（重導向到主應用程式）
├── pallet_pairing_scanner_mobile.html  # 主應用程式
├── start_server.py                     # 本地開發伺服器啟動腳本
└── README.md                           # 本文件
```

## 🔐 Firebase 設定

應用程式已配置 Firebase Firestore 資料庫。若要使用自己的 Firebase 專案：

1. 建立 Firebase 專案（https://console.firebase.google.com）
2. 啟用 Firestore Database 和 Anonymous Authentication
3. 在 `pallet_pairing_scanner_mobile.html` 中修改 `firebaseConfig` 物件

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

## 🐛 偵錯

- **Debug 資訊區**：頁面左下角的浮動視窗會顯示實時日誌
- **瀏覽器 Console**：按 F12 開啟開發者工具查看詳細日誌
- **常見錯誤**
  - `相機列表錯誤`：檢查瀏覽器相機權限或使用 HTTPS/localhost, 使用相機功能, 請務必建立HTTPS
  - `Firebase 未載入`：檢查網路連線
  - `Firestore 連線失敗`：確認 Firebase 專案配置正確

## 📱 行動應用建議

在 Android 手機上最佳使用體驗：
1. 使用 Chrome 瀏覽器
2. 透過 HTTPS 或 localhost 存取
3. 允許相機權限
4. 考慮將網站新增至主螢幕（快捷方式）

## 📝 使用範例

### 基本工作流程

1. **登入**：輸入使用者與密碼進入應用程式
2. **掃描棧板**：點擊棧板 ID 旁的相機圖示，掃描或手動輸入
3. **掃描儲位**：點擊儲位 ID 旁的相機圖示，掃描或手動輸入
4. **儲存配對**：點擊「儲存配對」按鈕
5. **檢視紀錄**：查看下方的配對紀錄表
6. **匯出資料**：點擊「匯出 CSV」下載紀錄

## 📞 支援與反饋

如有問題或建議，請在 GitHub Issues 中提報。

## 📄 授權

此專案為內部使用專案。

---

**最後更新**：2025 年 10 月 18 日
