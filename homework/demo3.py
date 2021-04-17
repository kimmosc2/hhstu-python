import turtle
 
def drawSnake(rad,angle,len,neckrad):

  colors = ["red","orange","yellow","green","cyan","blue","black","purple","coral"]
  for i in range(len):
    turtle.color(colors[i])
    turtle.circle(rad,angle*2)
    turtle.circle(-rad,angle)

    
  turtle.fd(rad*10)
  turtle.circle(rad,angle*2.25)
  turtle.fd(rad*10)
  
def main():
  turtle.setup(1000,1000,0,0)#宽，高，起点位置
  turtle.penup()#提起笔移动，不绘制图形，用于另起一个地方绘制
  turtle.goto(-10,10)#将画笔移动到坐标为x,y的位置
  turtle.pendown()#移动时绘制图形，缺省时也为绘制
  pythonsize = 30
  turtle.pensize(pythonsize)#设置画笔的宽度
  turtle.seth(0)
  drawSnake(40,80,9,pythonsize/2)
 

if __name__ == '__main__':
	main()
