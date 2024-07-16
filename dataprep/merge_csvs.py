# Load libraries
import pandas as pd
from pathlib import Path

#/storage/research/cinn_comp/ThalSR/zan/scripts/fthp_metrics.csv

# reading two csv files 
data1 = pd.read_csv('/storage/research/cinn_comp/ThalSR/zan/scripts/fthp_metrics.csv') 
data2 = pd.read_csv('/storage/research/cinn_comp/ThalSR/zan/scripts/fthp_hardware.csv')
# using merge function by setting how='inner' 
output1 = pd.merge(data1, data2,  
                   on='scanID',  
                   how='inner') 
  
output1.to_csv('fthp_results.csv')