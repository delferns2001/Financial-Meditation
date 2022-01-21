import pandas as pd
from datetime import datetime
from datetime import date

# print(pd.date_range(end=datetime.today(), periods=-7).to_pydatetime().tolist())

# today = date.today()
# print(today)

# # OR

# # print(pd.date_range(start="2022-01-01", end="2023-01-01").to_pydatetime().tolist())


d1 = datetime.now()
# retuns year, week, month
print(d1.isocalendar()[1])
print('Week :', d1.isocalendar()[1])


print('\033[1m' + 'Hello')
