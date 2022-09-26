# thris script will iterate through a DB connection by defined keys so not all data needs to be loaded. As similar loop can be used for training iterations of predictions.
import sys
import pandas as pd

evs = ["DKB10","DKB10"]
for x in evs:
    # Fetch some data including %s where variable needs to be chnaged in sql and [x] which is the variable name from the loop
     cur = conn.execute("select date_trunc('minute', time)\
         AS time_table, AVG(soc) AS power FROM fleet_dkb.car_log\
              WHERE fleet_id=%s GROUP BY DATE_TRUNC('minute' , time)\  
                   LIMIT 100;",[x])
    
    data = pd.DataFrame(cur)
    print(data.head())