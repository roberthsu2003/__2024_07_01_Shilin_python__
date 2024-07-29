import requests
from requests import Response
from pprint import pprint
from requests import ConnectionError,TooManyRedirects,Timeout,HTTPError
import pyinputplus as pyip

def connect_youbike() -> Response | str:
    youbike_url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000'
    try:
        response:Response = requests.get(youbike_url)
        response.raise_for_status()
    except ConnectionError:
        return "連線主機出問題"
    except TooManyRedirects:
        return "太多轉址"
    except Timeout:
        return "主機正在忙"
    except HTTPError:
        return "status_不是200"
    except:
        return "不明錯誤"
    else:
        return response
def search_area(response:Response,district:str)-> list[dict]:
    data:list[dict] = response.json()
    district_stations = [station for station in data if station['sarea'] == district]
    return district_stations  

def get_areas(response:Response) -> list[str]:
    data:list[dict] = response.json()
    sareas:set = set()
    for site in data:
        sareas.add(site['sarea'])
    return list(sareas)

def main():
        response:Response | str = connect_youbike() 
        if not isinstance(response,Response):
            print(response)
            return
        
        areas = get_areas(response)
        district:str = pyip.inputMenu(areas,"請輸入新北市行政區:\n",numbered=True)        
        district_stations = search_area(response,district)
        if district_stations:
            pprint(district_stations)
        else:
            print(f"沒有找到 {district} 行政區的站點資訊。請再輸入一次")
            

if __name__ == '__main__':
    main()