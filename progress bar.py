import time, sys

def process(num, total):
    rate = num / total
    ratenum = int(round(rate, 2) * 100)
    bar = '\r%s%% [%s%s]' %(ratenum, '#'*ratenum, ' '*(100 - ratenum))
    sys.stdout.write(bar)
    sys.stdout.flush()

n = 80
for i in range(1, n+1):
    time.sleep(0.1)
    process(i, n)
