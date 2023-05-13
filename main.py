"""
GUI 的資訊連結與 API 還有詳細說明：

    先幫我下載這個（不然看不到視窗喔）：
    pip install ttkbootstrap

    API 模組：
    https://ttkbootstrap.readthedocs.io/en/latest/api/

    初學使用指南：
    https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/tutorial/#the-traditional-approach

    主題一般預設為 Litera 如果想使用其他主題，可以輸入其他內置主題的名字
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def climate_event():
    """
    按鈕一處理事件

    """
    child_window = ttk.Toplevel(root)
    child_window.title("氣候資訊")
    child_window.geometry("320x100")

    # 在子視窗中建立 Label
    label = ttk.Label(child_window, text="你點進來了", font=("microsoft cache", 16))
    label.pack(pady=20)

def forecast_event():
    """
    按鈕二處理事件

    """
    child_window = ttk.Toplevel(root)
    child_window.title("預報資訊")
    child_window.geometry("320x100")

    # 在子視窗中建立 Label
    label = ttk.Label(child_window, text="你點進來了", font=("microsoft cache", 16))
    label.pack(pady=20)

def observation_event():
    """
    按鈕三處理事件

    """
    child_window = ttk.Toplevel(root)
    child_window.title("觀測資訊")
    child_window.geometry("320x100")

    # 在子視窗中建立 Label
    label = ttk.Label(child_window, text="你點進來了", font=("microsoft cache", 16))
    label.pack(pady=20)


def astronomical_event():
    """
    按鈕四處理事件

    """
    child_window = ttk.Toplevel(root)
    child_window.title("天文資訊")
    child_window.geometry("320x100")

    # 在子視窗中建立 Label
    label = ttk.Label(child_window, text="你點進來了", font=("microsoft cache", 16))
    label.pack(pady=20)


def weatherAlert_event():
    """
    按鈕五處理事件

    """
    child_window = ttk.Toplevel(root)
    child_window.title("天氣警特報資訊")
    child_window.geometry("320x100")

    # 在子視窗中建立 Label
    label = ttk.Label(child_window, text="你點進來了", font=("microsoft cache", 16))
    label.pack(pady=20)

def numericalForecast_event():
    """
    按鈕六處理事件

    """
    child_window = ttk.Toplevel(root)
    child_window.title("數值預報資訊")
    child_window.geometry("320x100")

    # 在子視窗中建立 Label
    label = ttk.Label(child_window, text="你點進來了", font=("microsoft cache", 16))
    label.pack(pady=20)

def earthquakeAndTsunami_event():
    """
    按鈕七處理事件

    """
    child_window = ttk.Toplevel(root)
    child_window.title("地震與海嘯資訊")
    child_window.geometry("320x100")

    # 在子視窗中建立 Label
    label = ttk.Label(child_window, text="你點進來了", font=("microsoft yahei", 16))
    label.pack(pady=20)


root = ttk.Window(themename="minty")
root.title("天氣顯示系統 Weather Display System")
root.geometry("640x650")

# 標題
label = ttk.Label(root, text="天氣顯示系統 Weather Display System", font=("microsoft yahei", 18))
label.pack(pady=50)

# 下拉式選單
options = ["台北市", "新北市", "基隆市", "桃園市", "新竹市", "台中市", "彰化縣", "台南市", "高雄市", "屏東縣", "宜蘭縣", "花蓮縣", "台東縣", "澎湖縣", "金門縣", "連江縣"]
cb = ttk.Combobox(root, bootstyle="secondary", values=options)
cb.pack(pady=10)

# 按鈕們
b1 = ttk.Button(root, text="氣候 climate", command=climate_event, bootstyle=(PRIMARY,OUTLINE))
b1.pack(pady=10)

b2 = ttk.Button(root, text="預報 forecast", command=forecast_event, bootstyle=(SECONDARY,OUTLINE))
b2.pack(pady=10)

b3 = ttk.Button(root, text="觀測 observation", command=observation_event, bootstyle=(SUCCESS,OUTLINE))
b3.pack(pady=10)

b4 = ttk.Button(root, text="天文 astronomical", command=astronomical_event, bootstyle=(INFO,OUTLINE))
b4.pack(pady=10)

b5 = ttk.Button(root, text="天氣警特報 weather alert", command=weatherAlert_event, bootstyle=(WARNING,OUTLINE))
b5.pack(pady=10)

b6 = ttk.Button(root, text="數值預報 numerical forecast", command=numericalForecast_event, bootstyle=(DANGER,OUTLINE))
b6.pack(pady=10)

b7 = ttk.Button(root, text="地震與海嘯 earthquake & tsunami", command=earthquakeAndTsunami_event, bootstyle=(DARK,OUTLINE))
b7.pack(pady=10)

root.mainloop()