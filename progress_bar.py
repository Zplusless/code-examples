import time, sys

'''
实现进度条的关键是：
1. 不换行
2. 利用\r将光标返回行首，后续输出就会覆盖前面的输出
'''


def process(num, total):
    rate = num / total
    ratenum = int(round(rate, 2) * 100)
    bar = '\r%s%% [%s%s]' %(ratenum, '#'*ratenum, ' '*(100 - ratenum)) # \r保证光标始终在这一行的最开头
    sys.stdout.write(bar) # 标准输出，print()相当于sys.stdout.write(obj+'\n')
    sys.stdout.flush()  # 刷新标准输出的缓冲区，保证输出内容实时出现在屏幕上

n = 80
for i in range(1, n+1):
    time.sleep(0.1)
    process(i, n)


# 使用print实现
for i in range(30):
    print('\r'+str(i)+'-'*i, end='',flush=True)
    time.sleep(0.2)

# 证明\r后会有新输出的地方覆盖，没有新输出的地方会保留
for i in range(5):
    print('-------------', end='')
    time.sleep(0.5)
    print('\r',end='')
    print('****', end='')
    time.sleep(0.5)
    print('\r',end='')

