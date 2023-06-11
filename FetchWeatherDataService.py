import requests


class FetchWeatherDataService:
    def __init__(self, token: str):
        self.token = token


if __name__ == '__main__':
    token = "CWB-1926AAC3-EDEB-47C2-985A-1EE9120A0E55"
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": token,
        "format": "JSON",
        "locationName": "高雄市"
    }
    response = requests.get(url, params)
    print(response.json())
