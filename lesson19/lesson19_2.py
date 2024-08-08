from tools import get_path,station_info,merge_dataFrame
import pandas as pd

if __name__ == '__main__':
    fileName_list = get_path()
    stations_df = station_info()
    all_in_out = merge_dataFrame(fileName_list, stations_df)
    station_in_out= pd.concat(all_in_out)
    print(station_in_out)