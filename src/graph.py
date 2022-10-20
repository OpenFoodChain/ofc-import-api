import json
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import requests
from itertools import groupby

def batches():
  IMPORT_PATH = 'batch/import'
  STATIC_URL = 'static/graph/batches.png'
  r = requests.get('http://0.0.0.0:8777/'+ IMPORT_PATH)
  r = json.loads(r.text)
  if len(r) < 1:
    print('No Data on Batches Import')
  def key_func(k):
      return k['created_at']
  after_sorted = sorted(r, key=key_func)
  data = []
  for key, value in groupby(after_sorted, key_func):
      data.append({
        "date": key,
        "total": len(list(value))
      })
  dates = [i['date'] for i in data]
  values = [i['total'] for i in data]

  df = pd.DataFrame({'dates':dates, 'total':values})
  df['dates']  = [pd.to_datetime(i) for i in df['dates']]

  print(df.sort_values(by='dates'))

  plt.style.use('dark_background')
  plt.yticks(np.arange(min(values), max(values)+1, 10.0))

  plt.plot(dates,values)
  plt.title('Batch Import Graph')
  plt.xlabel('Date')
  plt.ylabel('Batch Total')
  plt.savefig('./' + STATIC_URL)
  print('Graph Saved: ', '<host>/'+STATIC_URL)
  # plt.show()

if __name__ == '__main__':
  globals()[sys.argv[1]]()