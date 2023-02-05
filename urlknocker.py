import winsound
import requests
import sys
import time
import datetime

now = datetime.datetime.now()
filename = 'urlknock_' + now.strftime('%Y%m%d_%H%M%S') + '.log'

def log(text):
  with open(filename, mode='a') as f:
    time_log = datetime.datetime.now()
    f.write(f'[{time_log.strftime("%Y%m%d_%H:%M:%S")}]\n')
    f.write(text+'\n\n')
    print(f'[{time_log.strftime("%Y%m%d_%H:%M:%S")}]')
    print(text+'\r\n\r\n')

args = sys.argv

if len(args) < 2:
  print('python urlknocker.py http://example.com/test 200')
  exit(0)

url = args[1]
status_code = str(int(args[2]))
minutes = 1
terminate = False


while not terminate:
  print(f'Start knocking!\r\n{url}')
  first_time_request = True
  while True:
    try:
      response = requests.get(url)
    except requests.exceptions.ConnectionError:
      try:
        while True:
          print('Connection Error Occured')
          winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
          time.sleep(5)
      except KeyboardInterrupt:
        print('終了しますか?\r\n')
        answer = input()
        if 'y' in answer:
          terminate = True
        break
    if first_time_request:
      first_time_request = False
      log(response.text)
    log(str(response.status_code))
    if not str(int(response.status_code)) == status_code:
      try:
        while True:
          print('status code_changed')
          winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
          time.sleep(5)
      except KeyboardInterrupt:
        print('終了しますか?\r\n')
        answer = input()
        if 'y' in answer:
          terminate = True
        break
    time.sleep(60 * minutes)