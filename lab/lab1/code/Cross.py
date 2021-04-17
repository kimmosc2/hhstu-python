# Cross.py -- 使用turtle绘制叉

import turtle
# 设置画布
turtle.setup(400, 400, 300, 300)
# 抬笔
turtle.penup()
# 调整落笔位置
turtle.seth(45)
turtle.fd(200)
turtle.seth(180)
turtle.fd(300)
turtle.pendown()
# 画笔大小
turtle.pensize(5)
# 绘制方向
turtle.seth(-45)
turtle.fd(400)

# 另一部分
turtle.penup()
turtle.seth(90)
turtle.fd(280)
turtle.pendown()
turtle.seth(-135)
turtle.fd(400)

