from time import sleep
from datetime import datetime
DELAY = 1  # In minutes

while True:
    with open("log.txt", "w") as f:
        print(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        f.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    sleep(60 * DELAY)
