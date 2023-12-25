# Turtleグラフィックスのライブラリをインポート
import turtle
from turtle import *

turtle.setup(1000,700,None,0) #スクリーンサイズ、表示位置設定
window = turtle.Screen()
window.title("ウマノアシガタ")  
window.bgcolor("white")

#亀2つをt1,t2にいれる
t1 = turtle.Turtle()
t2 = turtle.Turtle()



#アイコン亀にする
t1.shape("turtle")
t2.shape("turtle")


t1.pencolor('blue') #t1線の色
t2.color("Red", "gray") #t2線の色,中の色


#t1の初期位置移動
t1.penup() #ペン上げる
t1.right(20) #右に向く
t1.forward(280) #前に進む
t1.pendown() #ペン降ろす


#t2の初期位置移動
t2.right(180) #t2線の向き変える
t2.penup() #ペン上げる
t2.left(30) #左に向く
t2.forward(210) #前に進む
t2.pendown() #ペン降ろす



#バラ書く
t1.speed("fastest") #スピード早める
t1.begin_fill()
for i in range(35):
    t1.forward(100 + i * 5)
    t1.right(360 / 4 + 10)
t1.end_fill()

#星書く
t2.pensize(5)
t2.begin_fill()
for i in range(5):
	t2.forward(100)
	t2.right(144)
t2.end_fill()

#円の定義
def draw_shape(t3, coordinates, radius, color):
    for (x, y) in coordinates:
        t3.penup()
        t3.goto(x, y)
        t3.pendown()
        t3.fillcolor(color)
        t3.begin_fill()
        t3.circle(radius)
        t3.end_fill()

#眉毛の定義       
def draw_eyebrows(t3, x, y,  color):
    t3.penup()
    t3.goto(x, y)
    t3.pendown()
    t3.color("black")
    
    
    for i in range(35):
        t3.forward(5) #
        t3.left(6) #

#口の定義        
def draw_mouth(t3, x, y, color):
    t3.penup()
    t3.goto(x, y)
    t3.pendown()
    t3.color("black")
    
    for i in range(35):
        t3.forward(4)
        t3.left(2)
        
#四角定義       
def draw_square(t3, x, y, color):
    t3.penup()
    t3.goto(x, y)
    t3.pendown()
    t3.color("white")
    
    
    for i in range(4):
        t3.right(90)
        t3.forward(20)
    
    
#アンパンマンを描く
def draw_turtle():
    #カメのカーソルの設定
    t3 = turtle.Turtle()
    t3.speed(6) #スピード変更
    t3.shape("turtle") #アイコン亀にする
    t3.pencolor("black") #ペンの色
    t3.pensize("10") #ペンサイズ変更
    
    #アンパンマンの頭、ほっぺ、鼻、目
    t3.shapes = [((0, 0), 160, "#f4a460"),    # 頭
              ((-100, 80), 50, "#ff6633"),  # 左ほっぺ
              ((105, 95), 50, "#ff6633"),   # 右ほっぺ
              ((5, 90), 50, "#ff3333"),     # 鼻
              ((-60, 200), 20, "black"),  # 左目
              ((50, 210), 20, "black")]   # 右目
           
    for shape in t3.shapes:
        draw_shape(t3, [shape[0]], shape[1], shape[2])
 
    t3.pensize(5) #ペンサイズ変更
    t3.left(75) #右眉毛
    draw_eyebrows(t3, 100, 225, "black")
    t3.left(155) #左眉毛
    draw_eyebrows(t3, -20, 225, "black")
    
    
    t3.left(40)
    draw_mouth(t3, -60, 60, "black")
    
    t3.pensize(3) #ペンサイズ変更
    t3.squarese = [(-80, 150, "white"), #左四角
                   (0, 155, "white"),   #真ん中四角
                   (80, 160, "white")]  #右四角
    
    for square in t3.squarese:
        draw_square(t3, square[0], square[1], square[2])
        
draw_turtle()



done()