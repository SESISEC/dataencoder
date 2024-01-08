import base64
import sys
import os
import tkinter
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter import *
import time
ext=".xecatiencodeddata"
def ef(f,delete):
        print("编码"+f)
        print("读取文件...",end="")
        with open(f,"rb") as fb:
            x=fb.read()
            fb.close()
        del fb
        print("完成")
        print("切分文件数据...",end="")
        xl=cut(x,100000)
        print("完成")
        c=0
        d=b""
        print("文件大小共"+len(x)+"字节，已切分为"+len(xl)+"段")
        for i in xl:
            c+=1
            print("编码第"+str(c)+"段文件数据...",end="")
            t1=time.time()
            ib=base64.b64encode(i)
            t2=time.time()
            t=t2-t1
            s=100000/t
            d+=ib
            print("完成。当前速度"+str(s)+"字节/秒，预计还需要"+str((len(x)-len(d))/100000*s)+"秒完成")
        print(f+"编码完成。")
        print("保存文件...",end="")
        with open(f+ext,"wb") as f:
            f.write(d)
        print("完成")
        if delete==True:
            os.unlink(f)
def cut(string, length):
    return [string[i:i+length] for i in range(0, len(string), length)]
def main():
    options=input("""请选择需要的操作。
1.编码
2.反编码
3.退出
>""")
    if options=="1":
        options=input("""已进入编码模式。请选择编码文件或者文件夹。
1.编码文件
2.编码文件夹
3.退出编码模式
>""")
        root=tkinter.Tk()
        root.withdraw()
        if options=="1":
            f=askopenfilename()
            print("编码"+f)
            print("读取文件...",end="")
            with open(f,"rb") as fb:
                x=fb.read()
                fb.close()
            del fb
            print("完成")
            print("切分文件数据...",end="")
            xl=cut(x,100000)
            print("完成")
            c=0
            d=b""
            print("文件大小共"+len(x)+"字节，已切分为"+len(xl)+"段")
            for i in xl:
                c+=1
                print("编码第"+str(c)+"段文件数据...",end="")
                t1=time.time()
                ib=base64.b64encode(i)
                t2=time.time()
                t=t2-t1
                s=100000/t
                d+=ib
                print("完成。当前速度"+str(s)+"字节/秒，预计还需要"+str((len(x)-len(d))/100000*s)+"秒完成")
            print(f+"编码完成。")
            print("保存文件...",end="")
            with open(f+ext,"wb") as f:
                f.write(d)
            print("完成")
            options=input("是否删除原始文件？(Y/n)>")
            if options=="Y":
                os.unlink(f)
            print("编码完成，编码文件已经保存至"+f+ext)
        elif options=="2":
            
    elif options=="2":
        #placeholder
    else:
        print("确认退出？请按任意键以继续退出。")
        os.system("pause")
        sys.exit()
    
