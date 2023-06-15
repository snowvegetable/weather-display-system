"""
GUI 的資訊連結與 API 還有詳細說明：

    先幫我下載這個：
    pip install ttkbootstrap

    API 模組：
    https://ttkbootstrap.readthedocs.io/en/latest/api/

    初學使用指南：
    https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/tutorial/#the-traditional-approach

    主題一般預設為 Litera 如果想使用其他主題，可以輸入其他內置主題的名字

    使用 python 版本：3.10.7
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from FetchWeatherDataService import FetchWeatherDataService
from area import area_name, location_name, area_name_conversion_id_table


class App(ttk.Window):
    def __init__(self, themename):
        super().__init__(themename = themename)
        self.geometry("640x680")

        self.authorization = "CWB-1926AAC3-EDEB-47C2-985A-1EE9120A0E55"
        self.fetch_weather_data_service = FetchWeatherDataService(self.authorization)

        # 主頁面
        self.home_page = ttk.Frame(self)
        self.home_page.pack()
        self._set_home_page()

    # 設定主畫面布局
    def _set_home_page(self):
        # 首頁標題
        self.title_label = ttk.Label(
            self.home_page, text = "天氣顯示系統 Weather Display System", font = ("microsoft yahei", 18)
        )
        self.title_label.pack(pady = 50)

        # 下拉選單
        self.area_list = ttk.Combobox(
            self.home_page, bootstyle = "secondary", values = area_name
        )
        self.area_list.pack(pady = 10)
        self.area_list.bind("<<ComboboxSelected>>", self._update_location_list)

        self.location_list = ttk.Combobox(
            self.home_page, bootstyle = "secondary"
        )
        self.location_list.pack(pady = 10)

        # 按鈕
        self.b1 = ttk.Button(
            self.home_page, text = "氣候 climate", bootstyle = (PRIMARY, OUTLINE)
        )
        self.b1.pack(pady = 10)

        self.b2 = ttk.Button(
            self.home_page, text = "預報 forecast", bootstyle = (SECONDARY, OUTLINE)
        )
        self.b2.pack(pady = 10)

        self.b3 = ttk.Button(
            self.home_page, text = "觀測 observation", bootstyle = (SUCCESS, OUTLINE)
        )
        self.b3.pack(pady = 10)

        self.b4 = ttk.Button(
            self.home_page, text = "天文 astronomical", bootstyle = (INFO, OUTLINE)
        )
        self.b4.pack(pady = 10)

        self.b5 = ttk.Button(
            self.home_page, text = "天氣警特報 weather alert", bootstyle = (WARNING, OUTLINE)
        )
        self.b5.pack(pady = 10)

        self.b6 = ttk.Button(
            self.home_page, text = "數值預報 numerical forecast", bootstyle = (DANGER, OUTLINE)
        )
        self.b6.pack(pady = 10)

        self.b7 = ttk.Button(
            self.home_page, text = "地震與海嘯 earthquake & tsunami", bootstyle = (DARK, OUTLINE)
        )
        self.b7.pack(pady = 10)

    # 更新下拉表單
    def _update_location_list(self, *args):
        self.location_list["values"] = location_name[self.area_list.get()]
        print(self.area_list.get())

    # 回到首頁
    def _back_home_home(self):
        self.home_page.pack()


app = App(themename = "minty")
app.mainloop()
