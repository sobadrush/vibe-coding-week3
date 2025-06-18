"""
我的第一個 App - Tkinter GUI 應用程式

這是一個簡單的 GUI 應用程式，包含基本的視窗設定。
"""

import tkinter as tk
from PIL import Image, ImageTk
import random

# 全域變數
coins = 0
click_power = 1
upgrade_cost = 10  # 初始升級費用
special_attacks_left = 3  # 大招剩餘次數
special_attack_power = 3  # 大招攻擊力（初始點擊力1的3倍）


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


def update_stats():
    """更新統計資訊顯示。"""
    global coins, click_power, coins_label, power_label, special_attacks_left, special_attack_power, special_label, special_power_label
    coins_label.config(text=f"💰 金幣: {coins}")
    power_label.config(text=f"⚡ 點擊力: {click_power}")
    special_label.config(text=f"🔥 大招: {special_attacks_left}次")
    special_power_label.config(text=f"攻擊力: {special_attack_power}")
    
    # 調試輸出
    print(f"更新統計 - 點擊力: {click_power}, 大招攻擊力: {special_attack_power}")


def update_upgrade_button():
    """更新升級按鈕文字。"""
    global upgrade_cost, upgrade_button
    upgrade_button.config(text=f"升級點擊力 (花費: {upgrade_cost} 金幣)")


def upgrade_click_power():
    """升級點擊力。"""
    global coins, click_power, upgrade_cost, upgrade_button, special_attack_power
    
    # 檢查是否有足夠的金幣
    if coins >= upgrade_cost:
        # 扣除金幣
        coins -= upgrade_cost
        
        # 增加點擊力
        click_power += 1
        
        # 更新大招攻擊力（點擊力的3倍）
        special_attack_power = click_power * 3
        
        # 計算下次升級費用（隨機增加10-30）
        upgrade_cost += random.randint(10, 30)
        
        # 更新顯示
        update_stats()
        update_upgrade_button()
        
        # 調試輸出
        print(f"升級後 - 點擊力: {click_power}, 大招攻擊力: {special_attack_power}")
        
        # 如果金幣不足，禁用按鈕
        if coins < upgrade_cost:
            upgrade_button.config(state="disabled")
    else:
        # 金幣不足，禁用按鈕
        upgrade_button.config(state="disabled")


def on_click(event):
    """滑鼠點擊事件處理函數。"""
    global image_label, hero_img, hero_click_img, coins, click_power, upgrade_button, upgrade_cost
    
    # 增加金幣
    coins += click_power
    
    # 更新統計顯示
    update_stats()
    
    # 檢查是否可以啟用升級按鈕
    if coins >= upgrade_cost:
        upgrade_button.config(state="normal")
    
    # 切換到點擊圖片
    image_label.config(image=hero_click_img)
    
    # 200毫秒後自動切換回原始圖片
    image_label.after(200, lambda: image_label.config(image=hero_img))


def on_right_click(event):
    """滑鼠右鍵點擊事件處理函數。"""
    global image_label, hero_img, hero_right_click_img, coins, click_power, upgrade_button, upgrade_cost, special_attacks_left, special_attack_power
    
    # 檢查是否還有大招次數
    if special_attacks_left > 0:
        # 減少大招次數
        special_attacks_left -= 1
        
        # 增加金幣（大招攻擊力）
        coins += special_attack_power
        
        # 更新統計顯示
        update_stats()
        
        # 檢查是否可以啟用升級按鈕
        if coins >= upgrade_cost:
            upgrade_button.config(state="normal")
        
        # 切換到右鍵點擊圖片
        image_label.config(image=hero_right_click_img)
        
        # 200毫秒後自動切換回原始圖片
        image_label.after(200, lambda: image_label.config(image=hero_img))


def main():
    """主程式函數。"""
    global image_label, hero_img, hero_click_img, hero_right_click_img, coins_label, power_label, upgrade_button, special_label, special_power_label
    
    # 建立主視窗
    root = tk.Tk()
    
    # 設定視窗標題
    root.title("點擊英雄")
    
    # 將視窗置中顯示
    center_window(root, 500, 550)
    
    # 建立遊戲標題標籤
    title_label = tk.Label(
        root,
        text="🎮 點擊英雄 🎮",
        font=("Arial", 24, "bold"),
        fg="darkblue",
        bg="lightgray"
    )
    title_label.pack(pady=(50, 20))
    
    # 建立統計資訊框架（真正的圓角區塊）
    # 使用 Canvas 創建圓角矩形
    canvas = tk.Canvas(
        root,
        width=350,
        height=80,
        bg="white",  # 背景設為白色，之後會被圓角矩形覆蓋
        highlightthickness=0  # 移除邊框
    )
    canvas.pack(pady=10)
    
    # 在 Canvas 上繪製圓角矩形
    canvas.create_rounded_rectangle = lambda x1, y1, x2, y2, radius, **kwargs: canvas.create_polygon(
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1,
        smooth=True,
        **kwargs
    )
    
    # 繪製深灰色圓角矩形背景
    canvas.create_rounded_rectangle(0, 0, 350, 80, 15, fill="#404040", outline="#404040")
    
    # 建立金幣標籤
    coins_label = tk.Label(
        canvas,
        text="💰 金幣: 0",
        font=("Arial", 12, "bold"),
        fg="gold",
        bg="#404040",  # 深灰色背景
        padx=10,
        pady=5
    )
    canvas.create_window(70, 25, window=coins_label)
    
    # 建立點擊力標籤
    power_label = tk.Label(
        canvas,
        text="⚡ 點擊力: 1",
        font=("Arial", 12, "bold"),
        fg="orange",
        bg="#404040",  # 深灰色背景
        padx=10,
        pady=5
    )
    canvas.create_window(70, 55, window=power_label)
    
    # 建立分隔線
    separator = tk.Frame(
        canvas,
        bg="#666666",  # 較淺的灰色
        width=2,
        height=50
    )
    canvas.create_window(175, 40, window=separator)
    
    # 建立大招標籤
    special_label = tk.Label(
        canvas,
        text="🔥 大招: 3次",
        font=("Arial", 12, "bold"),
        fg="red",
        bg="#404040",  # 深灰色背景
        padx=10,
        pady=5
    )
    canvas.create_window(280, 25, window=special_label)
    
    # 建立大招攻擊力標籤
    special_power_label = tk.Label(
        canvas,
        text="攻擊力: 3",
        font=("Arial", 12, "bold"),
        fg="red",
        bg="#404040",  # 深灰色背景
        padx=10,
        pady=5
    )
    canvas.create_window(280, 55, window=special_power_label)
    
    # 載入圖片
    try:
        # 載入原始圖片
        hero_image = Image.open("hero.png")
        # 獲取原始尺寸
        hero_width, hero_height = hero_image.size
        # 計算合適的顯示尺寸（保持比例）
        display_size = 200
        if hero_width > hero_height:
            # 寬度較大，以寬度為基準
            new_width = display_size
            new_height = int(hero_height * display_size / hero_width)
        else:
            # 高度較大，以高度為基準
            new_height = display_size
            new_width = int(hero_width * display_size / hero_height)
        
        # 調整 hero.png
        hero_image = hero_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        hero_img = ImageTk.PhotoImage(hero_image)
        
        # 載入點擊圖片並調整為相同尺寸
        hero_click_image = Image.open("hero_click.png")
        hero_click_image = hero_click_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        hero_click_img = ImageTk.PhotoImage(hero_click_image)
        
        # 載入右鍵點擊圖片並調整為相同尺寸
        hero_right_click_image = Image.open("hero_right_click.png")
        hero_right_click_image = hero_right_click_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        hero_right_click_img = ImageTk.PhotoImage(hero_right_click_image)
        
        # 建立圖片標籤
        image_label = tk.Label(root, image=hero_img)
        image_label.pack(pady=20)
        
        # 綁定滑鼠左鍵點擊事件
        image_label.bind("<Button-1>", on_click)
        
        # 綁定滑鼠右鍵點擊事件
        image_label.bind("<Button-3>", on_right_click)
        
    except Exception as e:
        # 如果圖片載入失敗，顯示錯誤訊息
        error_label = tk.Label(
            root,
            text=f"圖片載入失敗: {e}",
            font=("Arial", 12),
            fg="red"
        )
        error_label.pack(pady=20)
    
    # 建立升級按鈕
    upgrade_button = tk.Button(
        root,
        text="升級點擊力 (花費: 10 金幣)",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="#4CAF50",  # 綠色背景
        activebackground="#45a049",  # 按下時的顏色
        activeforeground="white",
        relief="raised",  # 凸起效果
        bd=3,  # 邊框寬度
        padx=35,
        pady=15,
        command=upgrade_click_power,
        state="disabled",  # 初始狀態為禁用
        cursor="hand2"  # 滑鼠懸停時顯示手型游標
    )
    upgrade_button.pack(pady=20)
    
    # 啟動主迴圈
    root.mainloop()


if __name__ == "__main__":
    main() 