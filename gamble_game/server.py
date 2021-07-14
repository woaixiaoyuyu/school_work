#  我真诚地保证：
#  我自己独立地完成了整个程序从分析、设计到编码的所有工作。
#  如果在上述过程中，我遇到了什么困难而求教于人，那么，我将在程序实习报告中
#  详细地列举我所遇到的问题，以及别人给我的提示。
#  在此，我感谢 , …, XXX对我的启发和帮助。下面的报告中，我还会具体地提到
#  他们在各个方法对我的帮助。
#  我的程序里中凡是引用到其他程序或文档之处，
#  例如教材、课堂笔记、网上的源代码以及其他参考书上的代码段,
#  我都已经在程序的注释里很清楚地注明了引用的出处。

#  我从未没抄袭过别人的程序，也没有盗用别人的程序，
#  不管是修改式的抄袭还是原封不动的抄袭。
#  我编写这个程序，从来没有想过要去破坏或妨碍其他计算机系统的正常运转。 
#  <xiaoyuyu>


#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#encoding:utf-8

from socket import *
from time import ctime
import random
import time
import threading
#random.seed ( [x] )

list_k=["""
           ┌────┐ ┌─────┐
           │●　 │ │　   │
	   │ 　 │ │　●　│ 
           │ 　 │ │　　 │
	   └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
           │●　●│ │　   │
	   │ 　 │ │　●　│
	   │ 　 │ │　　 │
	   └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
           │●　●│ │　   │
           │●　 │ │　●　│
           │ 　 │ │　　 │
	   └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
           │●　●│ │　   │
	   │●　●│ │　●　│
           │ 　 │ │　　 │
	   └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
           │●　●│ │　●　│
	   │●　 │ │　　 │
	   └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
           │●　●│ │　   │
	   │●　●│ │　●　│
	   │●　●│ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　 │ │　●  │
	   │ 　 │ │　●　│
	   │ 　 │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　●  │
	   │ 　 │ │　●　│
	   │ 　 │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　 │ │　●● │
	   │    │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　●│ │　●● │
	   │    │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　●│ │　●● │
	   │●　 │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　●│ │　●● │
	   │●　●│ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　 │ │　   │
	   │    │ │　●●●│
	   │    │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │    │ │　●●●│
	   │    │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　 │ │　●●●│
	   │    │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　●│ │　●●●│
	   │    │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　●│ │　●●●│
	   │●　 │ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　●│ │　●●●│
	   │●　●│ │　　 │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
 	   │●　 │ │　   │
	   │    │ │　●● │
	   │    │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │    │ │　●● │
	   │    │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　 │ │　●● │
	   │    │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　●│ │　●● │
	   │    │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　●│ │　●● │
 	   │●　 │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　   │
	   │●　●│ │　●● │
	   │●　●│ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　 │ │　●● │
	   │    │ │　●● │
	   │    │ │　●　│
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　●● │
	   │    │ │  ●● │
	   │    │ │　●　│
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　●● │
	   │●　 │ │　●● │
	   │    │ │　●　│
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　●● │
	   │●　●│ │　●● │
	   │    │ │　●　│
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　●● │
	   │●　●│ │　●● │
	   │●　 │ │　●　│
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　●● │
	   │●　●│ │　●● │
	   │●　●│ │　●　│
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　 │ │　●● │
	   │    │ │　●● │
	   │    │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●　●│ │　●● │
	   │    │ │　●● │
	   │    │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●●　│ │　●● │
	   │●   │ │　●● │
	   │    │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●●　│ │　●● │
	   │●●  │ │　●● │
	   │    │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●●　│ │　●● │
	   │●●  │ │　●● │
	   │●   │ │　●● │
           └────┘ └─────┘""",
        """
           ┌────┐ ┌─────┐
	   │●●  │ │　●● │
	   │●●  │ │　●● │
	   │●●  │ │　●● │
           └────┘ └─────┘""",]


list_k2=["""
            ┌────┐
            │  　│
            │ ●　│
            │　  │
            └────┘""",
         """ 
            ┌────┐
            │●　●│
            │ 　 │
            │ 　 │
            └────┘""",
         """
            ┌────┐
            │●　 │
            │ ●　│
            │ 　●│
            └────┘""",
         """
            ┌────┐
            │●　●│
            │  　│
            │●　●│
            └────┘""",
         """
            ┌────┐
            │●　●│
            │ ●　│
            │●　●│
            └────┘""",
         """
            ┌────┐
       	    │●　●│
  	    │●  ●│
            │●　●│
	    └────┘"""]

host = '127.0.0.1'
port = 9998
buffsize = 2048
ADDR = (host,port)
tctime = socket(AF_INET,SOCK_STREAM)
tctime.bind(ADDR)
tctime.listen(3)                          #监听，允许的连接数


def ZZC(tctimeClient):
    #tctimeClient,addr = tctime.accept()   #建立连接，等待客户端
    while True:
        #print('Wait for connection ...')
        #tctimeClient,addr = tctime.accept()   #建立连接，等待客户端
        #print("Connection from :",addr)
        data=''
        data1 = tctimeClient.recv(buffsize).decode()
        if '$' not in data1:
            data+=data1
            continue
        elif '$' in data1:
            data+=data1[:data1.find('$')]
            print(data)

            #exit
            if data=='exit':
                yaoyao="客官，再来玩几把呗\n"
                tctimeClient.send(('%s' % yaoyao).encode())
                #time.sleep(2)
                break

            key=random.randint(0,35)    #35中情况
            tc1=key%6
            if(0<=key<=5):
                tc2=1
            if(6<=key<=11):
                tc2=2
            if(12<=key<=17):
                tc2=3
            if(18<=key<=23):
                tc2=4
            if(24<=key<=29):
                tc2=5
            if(30<=key<=35):
                tc2=6
        
            yaoyao="\n性感ZZC，在线发牌"
            yaoyao+="新开盘！预叫头彩！\n"
            yaoyao+=list_k[key]
            yaoyao+='\n'
            yaoyao+="输入你压的值:"
            #data = tctimeClient.recv(buffsize).decode()
            #tctimeClient.send(('[%s] %s' % (ctime(),data)).encode())
            tctimeClient.send(('%s' % yaoyao).encode('utf-8'))

        #二次甩筛子
            key=random.randint(0,5)
            tc3=key
            key=random.randint(0,5)
            tc4=key

            while True:
                data1 = tctimeClient.recv(buffsize).decode()
                if '$' not in data1:
                    data+=data1
                    continue
                elif '$' in data1:
                    data+=data1[:data1.find('$')]
                    print(data)
                    list_a=data.split()  #etc.['ya', 'tc', '10', 'gold']
                    yaoyao="ZZC开奖啦"
                    yaoyao+="\n"
                    yaoyao+="庄家将两枚玉骰扔进两个金盅，一手持一盅摇将起来"
                    #tctimeClient.send(('%s' % yaoyao).encode())
                    #time.sleep(2)
                    yaoyao+="庄家将左手的金盅倒扣在银盘上，玉骰滚了出来\n"
                    yaoyao+=list_k2[tc3]
                    yaoyao+='\n'
                    #tctimeClient.send(('%s' % yaoyao).encode())
                    #time.sleep(2)
                    yaoyao+="庄家将右手的金盅倒扣在银盘上，玉骰滚了出来\n"
                    yaoyao+=list_k2[tc4]
                    yaoyao+='\n'
                    #tctimeClient.send(('%s' % yaoyao).encode())

        #tc
                    if(list_a[1]=='tc'):
                        if(tc1==tc3 and tc2==tc4):
                            money=int(list_a[2])*35
                            yaoyao+="你赢了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
                        elif(tc1!=tc3 or tc2!=tc4):
                            money=int(list_a[2])*35
                            yaoyao+="你输了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
       #dc        
                    if(list_a[1]=='dc'):
                        if(tc1==tc4 and tc2==tc3):
                            money=int(list_a[2])*17
                            yaoyao+="你赢了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
                        elif(tc1!=tc4 or tc2!=tc3):
                            money=int(list_a[2])*17
                            yaoyao+="你输了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
       #kp
                    if(list_a[1]=='kp'):
                        if(tc3!=tc4 and tc3%2==0 and tc4%4==0):
                            money=int(list_a[2])*5
                            yaoyao+="你赢了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
                        elif(tc3==tc4 or tc3%2!=0 or tc4%4!=0):
                            money=int(list_a[2])*5
                            yaoyao+="你输了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
       #qx
                    if(list_a[1]=='qx'):
                        if((tc3+tc4)==7):
                            money=int(list_a[2])*5
                            yaoyao+="你赢了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
                        elif((tc3+tc4)!=7):
                            money=int(list_a[2])*5
                            yaoyao+="你输了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
       #dd
                    if(list_a[1]=='dd'):
                        if(tc3%2!=0 and tc4%2!=0):
                            money=int(list_a[2])*3
                            yaoyao+="你赢了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
                        elif(tc3%2==0 and tc4%2==0):
                            money=int(list_a[2])*3
                            yaoyao+="你输了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
       #sx
                    if(list_a[1]=='sx'):
                        if((tc3+tc4)==3 and (tc3+tc4)==5 and (tc3+tc4)==9 and (tc3+tc4)==11):
                            money=int(list_a[2])*2
                            yaoyao+="你赢了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
                        elif((tc3+tc4)!=3 and (tc3+tc4)!=5 and (tc3+tc4)!=9 and (tc3+tc4)!=11):
                            money=int(list_a[2])*2
                            yaoyao+="你输了"+str(money)+" "+list_a[3]
                            tctimeClient.send(('%s' % yaoyao).encode())
                            break
    tctimeClient.close()

while True:
    tctimeClient,addr=tctime.accept()
    print("Connection from :",addr)
    serve = threading.Thread(target=ZZC,args=(tctimeClient,))
    serve.start()   #启动线程

