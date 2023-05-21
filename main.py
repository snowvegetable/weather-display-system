'''
GUI 的資訊連結與 API 還有詳細說明：

    先幫我下載這個：
    pip install ttkbootstrap

    API 模組：
    https://ttkbootstrap.readthedocs.io/en/latest/api/

    初學使用指南：
    https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/tutorial/#the-traditional-approach

    主題一般預設為 Litera 如果想使用其他主題，可以輸入其他內置主題的名字

    使用 python 版本：3.10.7
'''

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def show_selected_option():
    '''
    顯示下拉式選單所選的選項

    '''
    selected_option_c = cb.get()
    selected_option_d = district_cb.get()
    label.config(text="您所選擇的區域為："+str(selected_option_c)+str(selected_option_d))
    label.pack(pady=50)
    back_button.pack(pady=10)
    hide_homepage()



def go_back():
    '''
    回到原本的主畫面

    '''
    label.pack_forget()
    back_button.pack_forget()
    show_homepage()


# 隱藏首頁的元件
def hide_homepage():
    title_label.pack_forget()
    cb.pack_forget()
    district_cb.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    b5.pack_forget()
    b6.pack_forget()
    b7.pack_forget()


# 顯示首頁的元件
def show_homepage():
    title_label.pack(pady=50)
    cb.pack(pady=10)
    district_cb.pack(pady=10)
    b1.pack(pady=10)
    b2.pack(pady=10)
    b3.pack(pady=10)
    b4.pack(pady=10)
    b5.pack(pady=10)
    b6.pack(pady=10)
    b7.pack(pady=10)
    back_button.pack_forget()

# 根據其他縣市的選項，新增對應的行政區、鄉、鎮的資料
def update_district_options(*args):
    selected_city = cb.get()
    if selected_city == "台北市":
        district_options = ["中正區", "大同區", "中山區", "松山區", "大安區", "萬華區", "信義區", "士林區", "北投區", "內湖區", "南港區", "文山區"]

    elif selected_city == "新北市":
        district_options = ["板橋區", "三重區", "中和區", "永和區", "新莊區", "新店區", "樹林區", "鶯歌區", "三峽區", "淡水區", "汐止區", "瑞芳區","石門區","三芝區","金山區","萬里區","八里區","汐止區","林口區","五股區","蘆洲區","雙溪區","貢寮區","平溪區","泰山區","石碇區","深坑區","土城區","坪林區","烏來區"]

    elif selected_city == "基隆市":
        district_options = ["安樂區", "中山區", "中正區", "七堵區", "信義區", "仁愛區", "暖暖區"]

    elif selected_city == "桃園市":
        district_options = ["大園區", "蘆竹區", "觀音區", "龜山區", "桃園區", "中壢區", "新屋區", "八德區", "平鎮區", "楊梅區", "大溪區", "龍潭區", "復興區"]

    elif selected_city == "新竹市":
        district_options = ["北區", "香山區", "東區"]

    elif selected_city == "新竹縣":
        district_options = ["新豐鄉", "湖口鄉", "新埔鎮", "竹北市", "關西鎮", "芎林鄉", "竹東鎮","寶山鄉","尖石鄉","橫山鄉","北埔鄉","峨眉鄉","五峰鄉"]

    elif selected_city == "苗栗縣":
        district_options = ["竹南鎮", "頭份市", "三灣鄉", "造橋鄉", "後龍鎮", "南庄鄉", "頭屋鄉","獅潭鄉","苗栗市","西湖鄉","通霄鎮","公館鄉","銅鑼鄉","泰安鄉","苑裡鎮","大湖鄉","三義區","卓蘭鎮"]

    elif selected_city == "台中市":
        district_options = ["北屯區", "西屯區", "南屯區", "北區", "南區", "東區", "中區","西區","和平區","大甲區","大安區","外埔區","后里區","清水區","東勢區","神岡區","龍井區","石岡區","豐原區","梧棲區","新社區","沙鹿區","大雅區","潭子區","大肚區","太平區","烏日區","大里區","霧峰區"]

    elif selected_city == "彰化縣":
        district_options = ["伸港鄉", "和美鎮", "線西鄉", "鹿港鎮", "彰化市", "秀水鄉", "福興鄉","花壇鄉","芬園鄉","芳苑鄉","埔鹽鄉","大村鄉","二林鎮","員林市","溪湖鎮","埔心鄉","永靖鄉","社頭鄉","埤頭鄉","田尾鄉","大城鄉","田中鎮","北斗鎮","竹塘鄉","溪州鄉","二水鄉"]

    elif selected_city == "南投縣":
        district_options = ["仁愛鄉", "國姓鄉", "埔里鎮", "草屯鎮", "中寮鄉", "南投市", "魚池鄉", "水里鄉", "名間鄉", "信義鄉", "集集鎮", "竹山鎮", "鹿谷鄉"]

    elif selected_city == "雲林縣":
        district_options = ["麥寮鄉","二崙鄉","崙背鄉","西螺鎮","莿桐鄉","林內鄉","臺西鄉","土庫鎮","虎尾鎮","褒忠鄉","東勢鄉","斗南鎮","四湖鄉","古坑鄉","元長鄉","大埤鄉","口湖鄉","北港鎮","水林鄉","斗六市"]

    elif selected_city == "嘉義縣":
        district_options = ["大林鎮","溪口鄉","阿里山鄉","梅山鄉","新港鄉","民雄鄉","六腳鄉","竹崎鄉","東石鄉","太保市","番路鄉","朴子市","水上鄉","中埔鄉","布袋鎮","鹿草鄉","義竹鄉","大埔鄉"]

    elif selected_city == "嘉義市":
        district_options = ["西區","東區"]

    elif selected_city == "台南市":
        district_options = ["安南區","中西區","安平區","東區","南區","北區","白河區","後壁區","鹽水區","新營區","東山區","北門區","柳營區","學甲區","下營區","六甲區","南化區","將軍區","楠西區","麻豆區","官田區","佳里區","大內區","七股區","玉井區","善化區","西港區","山上區","安定區","新市區","左鎮區","新化區","永康區","歸仁區","關廟區","龍崎區","仁德區"]

    elif selected_city == "高雄市":
        district_options = ["楠梓區","左營區","三民區","鼓山區","苓雅區","新興區","前金區","鹽埕區","前鎮區","旗津區","小港區","那瑪夏區","甲仙區","六龜區","杉林區","內門區","茂林區","美濃區","旗山區","田寮區","湖內區","茄萣區","阿蓮區","路竹區","永安區","岡山區","燕巢區","彌陀區","橋頭區","大樹區","梓官區","大社區","仁武區","鳥松區","大寮區","鳳山區","林園區","桃源區"]

    elif selected_city == "屏東縣":
        district_options = ["高樹鄉","三地門鄉","霧臺鄉","里港鄉","鹽埔鄉","九如鄉","長治鄉","瑪家鄉","屏東市","內埔鄉","麟洛鄉","泰武鄉","萬巒鄉","竹田鄉","萬丹鄉","來義鄉","潮州鎮","新園鄉","崁頂鄉","新埤鄉","南州鄉","東港鎮","林邊鄉","佳冬鄉","春日鄉","獅子鄉","琉球鄉","枋山鄉","牡丹鄉","滿州鄉","車城鄉","恆春鎮","枋寮鄉"]

    elif selected_city == "宜蘭縣":
        district_options = ["頭城鎮","礁溪鄉","壯圍鄉","員山鄉","宜蘭市","大同鄉","五結鄉","三星鄉","羅東鎮","冬山鄉","南澳鄉","蘇澳鎮"]

    elif selected_city == "花蓮縣":
        district_options = ["秀林鄉","新城鄉","花蓮市","吉安鄉","壽豐鄉","萬榮鄉","鳳林鎮","豐濱鄉","光復鄉","卓溪鄉","瑞穗鄉","玉里鎮","富里鄉"]

    elif selected_city == "台東縣":
        district_options = ["長濱鄉","海端鄉","池上鄉","成功鎮","關山鎮","東河鄉","鹿野鄉","延平鄉","卑南鄉","臺東市","太麻里鄉","綠島鄉","達仁鄉","大武鄉","蘭嶼鄉","金峰鄉"]

    elif selected_city == "澎湖縣":
        district_options = ["白沙鄉","西嶼鄉","湖西鄉","馬公市","望安鄉","七美鄉"]

    elif selected_city == "金門縣":
        district_options = ["金城鎮","金湖鎮","金沙鎮","金寧鄉","烈嶼鄉","烏坵鄉"]

    elif selected_city == "連江縣":
        district_options = ["南竿鄉","北竿鄉","莒光鄉","東引鄉"]

    district_cb['values'] = district_options


root = ttk.Window(themename="minty")
root.title("天氣顯示系統 Weather Display System")
root.geometry("640x680")

# 標題
title_label = ttk.Label(root, text="天氣顯示系統 Weather Display System", font=("microsoft yahei", 18))
title_label.pack(pady=50)


# 縣市下拉式選單
city_options = ["台北市", "新北市", "基隆市", "桃園市", "新竹市","新竹縣","苗栗縣", "台中市", "彰化縣","南投縣","雲林縣","嘉義縣","嘉義市", "台南市", "高雄市", "屏東縣", "宜蘭縣", "花蓮縣", "台東縣", "澎湖縣", "金門縣", "連江縣"]
cb = ttk.Combobox(root, bootstyle="secondary", values=city_options)
cb.pack(pady=10)
cb.bind("<<ComboboxSelected>>", update_district_options)


# 行政區、鄉、鎮下拉式選單
district_cb = ttk.Combobox(root, bootstyle="secondary")
district_cb.pack(pady=10)


# 按鈕
b1 = ttk.Button(root, text="氣候 climate", command=show_selected_option, bootstyle=(PRIMARY,OUTLINE))
b1.pack(pady=10)

b2 = ttk.Button(root, text="預報 forecast", command=show_selected_option, bootstyle=(SECONDARY,OUTLINE))
b2.pack(pady=10)

b3 = ttk.Button(root, text="觀測 observation", command=show_selected_option, bootstyle=(SUCCESS,OUTLINE))
b3.pack(pady=10)

b4 = ttk.Button(root, text="天文 astronomical", command=show_selected_option, bootstyle=(INFO,OUTLINE))
b4.pack(pady=10)

b5 = ttk.Button(root, text="天氣警特報 weather alert", command=show_selected_option, bootstyle=(WARNING,OUTLINE))
b5.pack(pady=10)

b6 = ttk.Button(root, text="數值預報 numerical forecast", command=show_selected_option, bootstyle=(DANGER,OUTLINE))
b6.pack(pady=10)

b7 = ttk.Button(root, text="地震與海嘯 earthquake & tsunami", command=show_selected_option, bootstyle=(DARK,OUTLINE))
b7.pack(pady=10)

back_button = ttk.Button(root, text="回首頁", command=go_back, bootstyle=DARK)
back_button.pack(pady=10)

label = ttk.Label(root, font=("microsoft yahei", 18))

show_homepage()

root.mainloop()