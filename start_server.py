#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡單的腳本：顯示本地 IP 地址並啟動 HTTP 伺服器
"""

import socket
import sys
import os

def get_local_ip():
    """獲取本地網路 IP 地址"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"無法獲取本地 IP: {e}")
        return "127.0.0.1"

def main():
    # 獲取本地 IP
    local_ip = get_local_ip()
    port = 8000

    print("=" * 50)
    print("🌐 本地網路 IP 地址:", local_ip)
    print(f"🔗 存取網址: http://{local_ip}:{port}")
    print(f"🏠 本地存取: http://localhost:{port}")
    print("=" * 50)
    print("正在啟動 HTTP 伺服器...")
    print("按 Ctrl+C 停止伺服器")
    print("=" * 50)

    # 直接啟動 http.server，避免 subprocess 導致的模組衝突警告
    try:
        # 動態 import http.server 以避免警告
        import http.server
        import socketserver

        # 設定伺服器
        handler = http.server.SimpleHTTPRequestHandler

        # 允許從網路存取 (bind to 0.0.0.0)
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"伺服器運行在 http://0.0.0.0:{port}/")
            print("從網路存取請使用上述 IP 地址")
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n伺服器已停止")
    except Exception as e:
        print(f"啟動伺服器時發生錯誤: {e}")

if __name__ == "__main__":
    main()