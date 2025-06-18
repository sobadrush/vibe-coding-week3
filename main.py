"""
我的第一個 App - Tkinter GUI 應用程式

這是一個簡單的 GUI 應用程式，包含輸入框、按鈕和標籤。
使用者可以在輸入框中輸入文字，點擊按鈕後會將文字顯示在標籤中。
"""

import tkinter as tk

# 全域變數
entry = None
label = None


def center_window(window, width=400, height=300):
    """將視窗置中顯示。
    
    Args:
        window: Tkinter 視窗物件
        width: 視窗寬度，預設 400
        height: 視窗高度，預設 300
    """
    # 取得螢幕尺寸
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # 計算視窗位置
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    # 設定視窗位置和大小
    window.geometry(f"{width}x{height}+{x}+{y}")


def update_label():
    """更新標籤文字為輸入框中的內容。"""
    global entry, label
    input_text = entry.get()
    label.config(text=input_text, fg="blue")


def main():
    """主程式函數。"""
    global entry, label
    
    # 建立主視窗
    root = tk.Tk()
    
    # 設定視窗標題
    root.title("我的第一個 App")
    
    # 將視窗置中顯示
    center_window(root, 500, 400)
    
    # 建立輸入框
    entry = tk.Entry(
        root,
        font=("Arial", 12),
        width=20
    )
    entry.insert(0, "唐納川普")  # 預設填入 "唐納川普"
    entry.pack(pady=20)
    
    # 建立按鈕
    button = tk.Button(
        root,
        text="顯示文字",
        command=update_label,
        font=("Arial", 12),
        bg="lightblue",
        fg="black"
    )
    button.pack(pady=10)
    
    # 建立標籤
    label = tk.Label(
        root,
        text="你好，世界!",
        font=("Arial", 14),
        fg="blue"
    )
    label.pack(pady=20)
    
    # 啟動主迴圈
    root.mainloop()


if __name__ == "__main__":
    main() 