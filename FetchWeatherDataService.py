import requests


class FetchWeatherDataService:
    def __init__(self, authorization: str):
        self.authorization = authorization

    # 取得天氣日報
    def get_weather_forecast_data(self, location_id: str, location_name: str):
        url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-093"
        params = {
            "Authorization": self.authorization,
            "format": "JSON",
            "locationId": location_id,  # 縣市編號
            "locationName": location_name  # 鄉鎮名稱
        }
        response = requests.get(url, params)
        return response.json()["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"]

# if __name__ == '__main__':
#     token = "CWB-1926AAC3-EDEB-47C2-985A-1EE9120A0E55"
#     url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-093"
#     params = {
#         "Authorization": token,
#         "format": "JSON",
#         "locationId": "F-D0047-067",  # 縣市編號
#         "locationName": "三民區"  # 鄉鎮名稱
#     }
#     response = requests.get(url, params)
#     f = response.json()
#     print(f)
