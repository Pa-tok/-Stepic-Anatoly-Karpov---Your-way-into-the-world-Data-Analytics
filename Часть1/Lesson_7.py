import pandas as pd
from io import BytesIO
import requests

# url = 'e:\!Data-scientist\!!LessonPre\[Stepic] Анатолий Карпов - Твой путь в мир Data Analytics\Data\\table - Лист1.csv'
# your_link = 'https://docs.google.com/spreadsheets/d/1lWg5Z4NX0wO_o-KdhfRd-eBr7y2jvzl_EFPSrbyolYI/edit#gid=0'
your_link = 'https://docs.google.com/spreadsheets/d/1TmUeL_RTiOdRNRWJpM6dkOobE4_u-F8fcQyno1-tB3c/edit?usp=sharing'
req = requests.get(your_link)
# req
# # <Response [200]>
# type(req)
# requests.models.Response
req = requests.get(your_link)
data = req.content
# df = pd.read_csv(BytesIO(data))
df = pd.read_csv(BytesIO(data), on_bad_lines='skip')
print(df)