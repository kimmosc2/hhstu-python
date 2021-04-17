# Circle.py -- 使用turtle绘制圆形

import turtle
# 设置画布
turtle.setup(500, 500, 300, 300)
# 调整起笔位置
turtle.penup()
turtle.seth(90)
turtle.fd(100)
turtle.pendown()
# 设置画笔大小
turtle.pensize(1)
# 设置绘制方向
turtle.seth(180)
# 画圆
turtle.circle(100, 360)

