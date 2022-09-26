# This script takes a event log format and iterates through it so one has a column based dataframe. It can be adabted so that it is som or count per column etc.
import pandas as pd
import numpy as np
from datetime import datetime as dt

# make example df
d = {'CreatedDate': ['1.1.2020', '2.1.2020', '3.4.2020', '5.4.2021'], 'Account': ["dfrt3545", "dfrt3544","dfrt3545","dfrt3544"], 'CaseType': ['test1', 'test1', 'test2', 'test2'], 'Id': [3, 4, 1, 2]}
data = pd.DataFrame(data=d)

def transform():
    data['CreatedDateISO'] = pd.to_datetime(data['CreatedDate'])
    aggregation_data = data.groupby([
                                    pd.Grouper(key='CreatedDateISO', freq='W'), 
                                    'Account', 
                                    'CaseType'])[['Id']].count()
    aggregation_data = aggregation_data.reset_index()
    pivoted = aggregation_data.pivot(index=["CreatedDateISO", "Account"], columns="CaseType", values="Id")
    pivoted=pivoted.replace(np.nan,0)
    for column in pivoted:
        pivoted['cum_'+column]=pivoted.groupby(['Account'])[column].cumsum(axis=0)
    pivoted=pivoted.reset_index()
    return pivoted

pivoted = transform()
print(pivoted)