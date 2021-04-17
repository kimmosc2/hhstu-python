import time
import math
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
    x = (i / scale)
    # 下面表达式任选一个即可,也可参考书上92页的公式自行设计
    # express = math.pow(x + (1 - x) / 2, 8)
    # express = 1 + math.pow((1-x),3) * -1
    # express = x + math.sin(x*math.pi*20)/80
    express = x + math.sin(x*math.pi*5)/20
    a = '*' * int(scale * express)
    b = '.' * int(scale * (1 - express))
    c = express * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, '-'))
