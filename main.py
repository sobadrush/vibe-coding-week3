import tkinter as tk

def center_window(window, width=400, height=300):
    """將視窗置中顯示"""
    # 取得螢幕尺寸
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # 計算視窗位置
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    # 設定視窗位置和大小
    window.geometry(f"{width}x{height}+{x}+{y}")

# 建立主視窗
root = tk.Tk()

# 設定視窗標題
root.title("我的第一個 App")

# 將視窗置中顯示
center_window(root)

# 啟動主迴圈
root.mainloop() 