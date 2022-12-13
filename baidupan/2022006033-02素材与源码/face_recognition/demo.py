import tkinter as tk  # 使用Tkinter前需要先导入
from open_camera import *
import scipy.io as sio
import os


#第1步，实例化object，建立窗口window
window = tk.Tk()
import tkinter.messagebox
from tkinter import messagebox

# 第2步，给窗口的可视化起名字
window.title('人脸检测')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1000x618')  # 这里的乘是小x

# 第4步，在图形界面上设定标签
l = tk.Label(window, text='人  脸  检  测', bg='white', font=('Arial', 12), width=40, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
l.pack()  # Label内容content区域放置位置，自动调节尺寸

# 第一个按钮
a = tk.Label(window, text='camera', bg='green', font=('Arial', 12), width=12, height=2)
a.place(x=206, y=500)

# 在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, bg='green', height=400, width=700)  # .place(x=160,y=60)
canvas.place(x=160, y=60)
# 创建未打开摄像头图片

# 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image_file = ImageTk.PhotoImage(file='D:\\wei.gif')
image = canvas.create_image(351, 0, anchor='n', image=image_file)



# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
var = tk.StringVar()
var.set('OFF')
on_hit = False

key=1
key2=1

def hit_me():
    global on_hit
    global key
    if on_hit == False:
        key=1
        on_hit = True
        var.set('ON')
        open()

    else:

        if on_hitt == True:
            print(messagebox.showerror(title='错误', message='Face detect 未关闭！'))
        else:
            key = 0
            on_hit = False
            var.set('OFF')
            open()



def camera():
    cap = cv2.VideoCapture(0) #打开摄像头
    ret, frame = cap.read()   #返回两个参数 ret 1/0；frame三维矩阵
    h, w = frame.shape[:2]   #图像的水平，垂直，通道
    centerface = CenterFace()  #模型分析
    imageNum = 0
    while True:
        ret, frame = cap.read() #灰度处理
        imageNum = imageNum + 1
        fileName = 'image/' + 'image' + str(
            imageNum) + '.jpg'  # 存储路径
        cv2.imwrite(fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        dets, lms = centerface(frame, h, w, threshold=0.35)
        for det in dets:
            boxes, score = det[:4], det[4]
            cv2.rectangle(frame, (int(boxes[0]), int(boxes[1])), (int(boxes[2]), int(boxes[3])), (2, 255, 0), 1)#矩形框用于标记
        for lm in lms:
            for i in range(0, 5):
                cv2.circle(frame, (int(lm[i * 2]), int(lm[i * 2 + 1])), 2, (0, 0, 255), -1)
        pic = tKImage_c(frame)
        canvas.create_image(0, 0, anchor='nw', image=pic)
        window.update()
        window.after(1)
        print(0)
        if key2 == 0:
            break
        # cv2.imshow('out', frame)
        # Press Q on keyboard to stop recording

# 建立函数  如果OFF则显示图片  如果ON则打开摄像头

def open():
     cap = cv2.VideoCapture(0)
     if on_hit==True:
         while True:
             pic = tkImage()
             canvas.create_image(0, 0, anchor='nw', image=pic)
             window.update()
             window.after(1)
             if key==0:
                 break

# ，在窗口界面设置放置Button按键  第一个按钮            lambda:[hit_me,hit_mp]
b = tk.Button(window, textvariable=var, font=('Arial', 12), width=8, height=1, command=hit_me)
b.place(x=220, y=550)

c = tk.Label(window, text='Face detect', bg='green', font=('Arial', 12), width=12, height=2)
c.place(x=706, y=500)

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
har = tk.StringVar()
har.set('OFF')
on_hitt = False


def hit_m():
    global on_hitt
    global key2
    if on_hit == False:
        print(messagebox.showerror(title='错误', message='camera 未打开！'))

    else:
        if on_hitt == False:
            key2=1
            on_hitt = True
            har.set('ON')
            camera()

        else:
            on_hitt = False
            har.set('OFF')
            key2=0
            open()



# ，在窗口界面设置放置Button按键   第二个按钮

b = tk.Button(window, textvariable=har, font=('Arial', 12), width=8, height=1, command=hit_m)
b.place(x=720, y=550)

#  同时调多个函数  command=lambda:[funcA(), funcB(), funcC()]




# def hit_mq():
#  global on_hitt
#   if on_hitt == False: #关闭人脸检测
#   else:#打开人脸检测


# 第6步，主窗口循环显示
window.mainloop()
