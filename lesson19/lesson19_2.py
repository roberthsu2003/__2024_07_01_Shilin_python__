import os
import pandas as pd
from pandas import DataFrame

def get_path() -> list[str]:
    current_path = os.path.dirname(os.path.abspath(__name__))
    folder_path = os.path.join(current_path,'每日各站進出站人數')
    fileName_list = []
    for filename in os.listdir(folder_path):
        if '每日各站進出站人數' in filename:
            fileName_list.append(os.path.join(folder_path,filename))
    return fileName_list

def station_info() -> DataFrame:
    import os,json
    import pandas as pd
    current_path = os.path.dirname(os.path.abspath(__name__))
    folder_path = os.path.join(current_path,'每日各站進出站人數')
    stations_path = os.path.join(folder_path,'車站基本資料集.json')
    with open(stations_path,encoding='utf-8') as file:
        station_content = json.load(file)
    stations_df = pd.DataFrame(station_content)
    stations_df['stationCode'] = stations_df['stationCode'].astype(int)
    return stations_df 


def merge_dataFrame(names:list[str], station:DataFrame) -> list[DataFrame]:
    import pandas as pd
    all_frames = []
    for name in names:
        inOut_df = pd.read_csv(name)
        df1 = pd.merge(inOut_df,station,left_on='staCode',right_on='stationCode')
        df2 = df1.reindex(columns=['trnOpDate','stationName','gateInComingCnt','gateOutGoingCnt'])
        df3 = df2.rename(columns={'trnOpDate':'日期',
                    'stationName':'站名',
                    'gateInComingCnt':'進站',
                    'gateOutGoingCnt':'出站'
                    })
        df3['日期'] = pd.to_datetime(df3['日期'].astype(str))
        all_frames.append(df3)
    return all_frames

if __name__ == '__main__':
    fileName_list = get_path()
    stations_df = station_info()
    all_in_out = merge_dataFrame(fileName_list, stations_df)
    station_in_out= pd.concat(all_in_out)
    station_in_out.to_csv('進出站人數.csv')