import infred
import time
mydegree = 90
status = 1

while True:
    mydegree = infred.checkLeftright(mydegree)
    print 'my:',mydegree
    status = infred.checkUpdown(status)
    time.sleep(0.5)