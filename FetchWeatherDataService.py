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

    # 取得天氣警特報資料
    def get_weather_alert_data(self, location_name: str):
        return_data = []

        url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/W-C0033-001"

        for phenomena in ["濃霧", "大雨", "豪雨", "大豪雨", "超大豪雨", "陸上颱風"]:
            params = {
                "Authorization": self.authorization,
                "format": "JSON",
                "locationName": location_name,  # 縣市編號
                "phenomena": phenomena
            }
            response = requests.get(url, params)

            if not response.json()["records"]["location"][0]["hazardConditions"]["hazards"]:
                return_data.append("無")
            else:
                return_data.append(
                    response.json()["records"]["location"][0]["hazardConditions"]["hazards"][0]["info"]["significance"])

        return {
            "濃霧": return_data[0],
            "大雨": return_data[1],
            "豪雨": return_data[2],
            "大豪雨": return_data[3],
            "超大豪雨": return_data[4],
            "陸上颱風": return_data[5]
        }


if __name__ == '__main__':
    fetchWeatherDataService = FetchWeatherDataService("CWB-1926AAC3-EDEB-47C2-985A-1EE9120A0E55")

    data = fetchWeatherDataService.get_weather_alert_data("高雄市")

    print(data)
