# 学习能力
power = 1.0
# 学习flag
study = True
# 不学习flag
unstudy = False
# 连续学习天数(7天一周期,到7天归零)
serialDay = 0
# 当前学习状态
state = study
for i in range(0, 365):
    # 前三天能力值不变
    if state == study and (serialDay in [0, 1, 2]):
        # 计算能力
        power *= 1
        # 计算周期
        serialDay = (serialDay + 1) % 7
    # 后四天能力值每天增加1%
    elif state == study and (serialDay in [3, 4, 5, 6]):
        # 计算能力
        power *= 1.01
        # 计算周期
        serialDay = (serialDay + 1) % 7
    # 如果没在学习,连续学习天数归零
    elif state == unstudy:
        serialDay = 0
    else:
        pass
print("连续学习365天后能力值为{:.2f}".format(power))
