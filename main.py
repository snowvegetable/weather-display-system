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

        # 天氣預報畫面
        self.weather_forecast_page = ttk.Frame(self)

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
            self.home_page, text = "天氣預報 climate", command = self._show_weather_forecast,
            bootstyle = (PRIMARY, OUTLINE)
        )
        self.b1.pack(pady = 10)

    # 更新下拉表單
    def _update_location_list(self, *args):
        self.location_list["values"] = location_name[self.area_list.get()]
        print(self.area_list.get())

    # 回到首頁
    def _back_home_page(self):
        self.weather_forecast_page.pack_forget()
        self.weather_forecast_page = ttk.Frame(self)

        self.home_page.pack()

    # 顯示天氣預報畫面
    def _show_weather_forecast(self):
        # 如果沒有選擇縣市或鄉鎮就不會跳轉畫面
        if self.area_list.get() == "" or self.location_list.get() == "":
            return

        self.title_label = ttk.Label(
            self.weather_forecast_page,
            font = ("microsoft yahei", 18),
            text = f"您所選擇的區域為：{self.area_list.get()} {self.location_list.get()}",
        )
        self.title_label.pack()

        self.back_home_btn = ttk.Button(
            self.weather_forecast_page,
            text = "back",
            command = self._back_home_page
        )
        self.back_home_btn.pack()

        self.home_page.pack_forget()
        self.weather_forecast_page.pack()


if __name__ == '__main__':
    app = App(themename = "minty")
    app.mainloop()
