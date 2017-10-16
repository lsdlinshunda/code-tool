#-*- coding: utf-8 -*-
#=============================================================================
#This program creates the GUI of code tool.
#=============================================================================

import os
import encryptFunction
from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *

class GUInterface:
    def __init__(self):
        self.root=Tk()
        self.root.title('密码工具v1.0')
#--------------------------------全局变量定义-----------------------------------
        self.codeMethod=StringVar()
        self.codeMethod.set('凯撒密码')
        self.codeFlag=IntVar()
        self.codeFlag.set(1)
        self.codeKey=StringVar()
        self.codeKey.set('3')
        self.morseDot=StringVar()
        self.morseDot.set('*')
        self.morseDash=StringVar()
        self.morseDash.set('-')
        self.morseBarrier=StringVar()
        self.morseBarrier.set('/')
#----------------------------------菜单创建-------------------------------------        
        self.mainMenu=Menu(self.root)
        self.root.config(menu=self.mainMenu)

        self.fileMenu=Menu(self.mainMenu)
        self.mainMenu.add_cascade(label='文件',menu=self.fileMenu)
        self.fileMenu.add_command(label='打开',command=self.openFile)
        self.fileMenu.add_command(label='保存',command=self.saveFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='退出',command=self.exitTool)
        
        self.chooseMenu=Menu(self.mainMenu)
        self.mainMenu.add_cascade(label='选择加密方式',menu=self.chooseMenu)
        self.chooseMenu.add_radiobutton(label='凯撒密码',variable=self.codeMethod,
                                   value='凯撒密码',command=self.chooseCaesar)
        self.chooseMenu.add_radiobutton(label='维吉尼亚密码',variable=self.codeMethod,
                                   value='维吉尼亚密码',command=self.chooseVigenere)
        self.chooseMenu.add_radiobutton(label='摩斯密码',variable=self.codeMethod,
                                   value='摩斯密码',command=self.chooseMorse)
        self.chooseMenu.add_radiobutton(label='手机9键',variable=self.codeMethod,
                                   value='手机9键',command=self.chooseNinekey)
        self.chooseMenu.add_radiobutton(label='其他替代密码',variable=self.codeMethod,
                                   value='其他替代密码',command=self.chooseOther)
        self.chooseMenu.add_separator()
        self.chooseMenu.add_radiobutton(label='栅栏密码',variable=self.codeMethod,
                                   value='栅栏密码',command=self.chooseFence)
        self.chooseMenu.add_separator()
        self.chooseMenu.add_radiobutton(label='进制转换',variable=self.codeMethod,
                                   value='进制转换',command=self.chooseSysconvert)
        
        self.helpMenu=Menu(self.mainMenu)
        self.mainMenu.add_cascade(label='帮助',menu=self.helpMenu)
        self.helpMenu.add_command(label='使用说明',command=self.instructions)
        self.helpMenu.add_command(label='关于作者',command=self.aboutAuthor)
#---------------------------------界面创建---------------------------------------
        self.editBox=Text(self.root,width=44,height=8,font=("Arial Rounded MT",20))
        self.editBox.grid(row=0,columnspan=2,sticky=W+E)
        Label(self.root,textvariable=self.codeMethod,fg='red').grid(
            row=1,column=0)

        self.frameCaesar=Frame(self.root)
        Radiobutton(self.frameCaesar,variable=self.codeFlag,value=1,
                    text='位移位数（-25~25）：').grid(row=0,column=0)
        Entry(self.frameCaesar,textvariable=self.codeKey,
                    width=5).grid(row=0,column=1)
        Radiobutton(self.frameCaesar,variable=self.codeFlag,value=2,
                    text='列出所有组合').grid(row=0,column=2)

        self.frameVigenere=Frame(self.root)
        Label(self.frameVigenere,text='秘钥：').grid(row=0,column=0)
        Entry(self.frameVigenere,textvariable=self.codeKey).grid(row=0,column=2)
        
        self.frameMorse=Frame(self.root)
        Label(self.frameMorse,text='点：').grid(row=0,column=0)
        Entry(self.frameMorse,textvariable=self.morseDot,
                            width=5).grid(row=0,column=1)
        Label(self.frameMorse,text='划：').grid(row=0,column=2)
        Entry(self.frameMorse,textvariable=self.morseDash,
                            width=5).grid(row=0,column=3)
        Label(self.frameMorse,text='分割符：').grid(row=0,column=4)
        Entry(self.frameMorse,textvariable=self.morseBarrier,
                            width=5).grid(row=0,column=5)

        self.frameNinekey=Frame(self.root)
        Radiobutton(self.frameNinekey,variable=self.codeFlag,value=1,
                    text='键盘坐标对应字母（23=c）').grid(row=0,column=0)
        Radiobutton(self.frameNinekey,variable=self.codeFlag,value=2,
                    text='按键次数对应字母（222=c）').grid(row=0,column=1)

        self.frameOther=Frame(self.root)
        Radiobutton(self.frameOther,variable=self.codeFlag,value=1,
                    text='字母表数字').grid(row=0,column=0)
        Radiobutton(self.frameOther,variable=self.codeFlag,value=2,
                    text='QWE').grid(row=0,column=1)
        Radiobutton(self.frameOther,variable=self.codeFlag,value=3,
                    text='V字').grid(row=0,column=2)

        self.frameFence=Frame(self.root)
        Radiobutton(self.frameFence,variable=self.codeFlag,value=1,
                    text='栏数：').grid(row=0,column=0)
        Entry(self.frameFence,textvariable=self.codeKey,
                    width=5).grid(row=0,column=1)
        Radiobutton(self.frameFence,variable=self.codeFlag,value=2,
                    text='列举所有栏数').grid(row=0,column=2)

        self.frameSysconvert=Frame(self.root)
        Radiobutton(self.frameSysconvert,variable=self.codeFlag,value=1,
                    text='十进制转二进制').grid(row=0,column=0)
        Radiobutton(self.frameSysconvert,variable=self.codeFlag,value=2,
                    text='十进制转八进制').grid(row=0,column=1)
        Radiobutton(self.frameSysconvert,variable=self.codeFlag,value=3,
                    text='十进制转十六进制').grid(row=0,column=2)

        self.currentFrame=self.frameCaesar
        self.currentFrame.grid(row=1,column=1)

        self.frameButton=Frame(self.root)
        self.encryptButton=Button(self.frameButton,text='加密',width=12,command=self.encryptCaesar)
        self.encryptButton.grid(row=0,column=0)
        Frame(self.frameButton,width=30*1.5).grid(row=0,column=1)
        self.decryptButton=Button(self.frameButton,text='解密',width=12,command=self.decryptCaesar)
        self.decryptButton.grid(row=0,column=2)
        Frame(self.frameButton,width=30*1.5).grid(row=0,column=3)
        Button(self.frameButton,text='倒叙',width=12,command=self.flashBack).grid(
            row=0,column=4)
        Frame(self.frameButton,width=30*1.5).grid(row=0,column=5)
        Button(self.frameButton,text='清除',width=12,command=self.clearEditbox).grid(
            row=0,column=6)
        self.frameButton.grid(row=2,columnspan=2)
        
        self.root.mainloop()
#-----------------------------文件与帮助菜单功能----------------------------------- 
    def openFile(self):
        try:
          fileName=askopenfilename()
          if fileName:
              fileData=open(fileName,'r')
              s=fileData.read()
              self.editBox.delete(1.0,END)
              self.editBox.insert(1.0,s)
              fileData.close()
        except:
          showerror('错误','打开文件错误')

    def saveFile(self):
        try:
          saveName=asksaveasfilename(title='保存')
          if saveName:
            saveFile=open(saveName,'w')
            saveFile.write(self.editBox.get(1.0,END)[:-1].encode('utf-8'))
            saveFile.flush()
            saveFile.close()
            showinfo('提示','保存成功')
        except:
            showerror('错误','保存文件失败')

    def exitTool(self):
        if askyesno('消息','是否要关闭程序？'):
            self.root.quit()
            self.root.destroy()

    def instructions(self):
        os.startfile('help.txt')

    def aboutAuthor(self):
        showinfo('关于','作者: 林顺达\nGithub: lsdlinshunda\n邮箱: 923076444@qq.com')
#-------------------------选择加密方式菜单功能-------------------------------------- 
    def chooseCaesar(self):
        self.currentFrame.grid_forget()
        self.currentFrame=self.frameCaesar
        self.codeFlag.set(1)
        self.codeKey.set('3')
        self.currentFrame.grid(row=1,column=1)
        self.encryptButton['command']=self.encryptCaesar
        self.decryptButton['command']=self.decryptCaesar

    def chooseVigenere(self):
        self.currentFrame.grid_forget()
        self.currentFrame=self.frameVigenere
        self.codeKey.set('')
        self.currentFrame.grid(row=1,column=1)
        self.encryptButton['command']=self.encryptVigenere
        self.decryptButton['command']=self.decryptVigenere

    def chooseMorse(self):
        self.currentFrame.grid_forget()
        self.currentFrame=self.frameMorse
        self.currentFrame.grid(row=1,column=1)
        self.encryptButton['command']=self.encryptMorse
        self.decryptButton['command']=self.decryptMorse

    def chooseNinekey(self):
        self.currentFrame.grid_forget()
        self.currentFrame=self.frameNinekey
        self.codeFlag.set(1)
        self.currentFrame.grid(row=1,column=1)
        self.encryptButton['command']=self.encryptNinekey
        self.decryptButton['command']=self.decryptNinekey

    def chooseOther(self):
        self.currentFrame.grid_forget()
        self.currentFrame=self.frameOther
        self.codeFlag.set(1)
        self.currentFrame.grid(row=1,column=1)
        self.encryptButton['command']=self.encryptOther
        self.decryptButton['command']=self.decryptOther

    def chooseFence(self):
        self.currentFrame.grid_forget()
        self.currentFrame=self.frameFence
        self.codeFlag.set(1)
        self.codeKey.set('2')
        self.currentFrame.grid(row=1,column=1)
        self.encryptButton['command']=self.encryptFence
        self.decryptButton['command']=self.decryptFence

    def chooseSysconvert(self):
        self.currentFrame.grid_forget()
        self.currentFrame=self.frameSysconvert
        self.codeFlag.set(1)
        self.currentFrame.grid(row=1,column=1)
        self.encryptButton['command']=self.encryptSysconvert
        self.decryptButton['command']=self.decryptSysconvert
#------------------------底部按钮功能----------------------------------------
    def clearEditbox(self):
        self.editBox.delete(1.0,END)
        
    def showResult(self,result):
        self.editBox.delete(1.0,END)
        self.editBox.insert(1.0,result)

    def flashBack(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          result=encryptFunction.flashBack(s)
          self.showResult(result)
        except:
          showerror('错误','倒叙出错')

    def encryptCaesar(self):
        try:
          result=''
          s=self.editBox.get(1.0,END)[:-1]
          if self.codeFlag.get()==1:
              result=encryptFunction.caesar(s,int(self.codeKey.get()))
          elif self.codeFlag.get()==2:
              for i in range(26):
                result=result+encryptFunction.caesar(s,i)+'\n'
          self.showResult(result)
        except:
          showerror('错误','加密出错')
                  
    def decryptCaesar(self):
        try:
          result=''
          s=self.editBox.get(1.0,END)[:-1]
          if self.codeFlag.get()==1:
              result=encryptFunction.caesar(s,-int(self.codeKey.get()))
          elif self.codeFlag.get()==2:
              for i in range(26):
                result=result+encryptFunction.caesar(s,-i)+'\n'
          self.showResult(result)
        except:
          showerror('错误','解密出错')

    def encryptVigenere(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          result=encryptFunction.vigenere(s,self.codeKey.get(),1)
          self.showResult(result)
        except:
          showerror('错误','加密出错')

    def decryptVigenere(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          result=encryptFunction.vigenere(s,self.codeKey.get(),-1)
          self.showResult(result)
        except:
          showerror('错误','解密出错')
          
    def encryptMorse(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          result=encryptFunction.encryptMorse(s,
               self.morseDot.get(),self.morseDash.get(),self.morseBarrier.get())
          self.showResult(result)
        except:
          showerror('错误','加密出错')

    def decryptMorse(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          result=encryptFunction.decryptMorse(s,
               self.morseDot.get(),self.morseDash.get(),self.morseBarrier.get())
          self.showResult(result)
        except:
          showerror('错误','解密出错')

    def encryptNinekey(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          if self.codeFlag.get()==1:
              result=encryptFunction.encryptNinekeyOne(s)
          elif self.codeFlag.get()==2:
              result=encryptFunction.encryptNinekeyTwo(s)
          self.showResult(result)
        except:
          showerror('错误','加密出错')

    def decryptNinekey(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          if self.codeFlag.get()==1:
              result=encryptFunction.decryptNinekeyOne(s)
          elif self.codeFlag.get()==2:
              result=encryptFunction.decryptNinekeyTwo(s)    
          self.showResult(result)
        except:
          showerror('错误','解密出错')   

    def encryptOther(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          if self.codeFlag.get()==1:
              result=encryptFunction.encryptAlpha(s)
          elif self.codeFlag.get()==2:
              result=encryptFunction.encryptQWE(s)
          elif self.codeFlag.get()==3:
              result=encryptFunction.encryptVkey(s)
          self.showResult(result)
        except:
          showerror('错误','加密出错')

    def decryptOther(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          if self.codeFlag.get()==1:
              result=encryptFunction.decryptAlpha(s)
          elif self.codeFlag.get()==2:
              result=encryptFunction.decryptQWE(s)
          elif self.codeFlag.get()==3:
              result=encryptFunction.decryptVkey(s)
          self.showResult(result)
        except:
          showerror('错误','解密出错')

    def encryptFence(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          l=len(s)
          n=int(self.codeKey.get())
          if self.codeFlag.get()==1:
              result=encryptFunction.encryptFence(s,n)
          elif self.codeFlag.get()==2:
              result=s
              for i in range(2,(l+1)/2+1):
                  result+=u'\n%d栏：\n' % (i)
                  result+=encryptFunction.encryptFence(s,i)
          self.showResult(result)
        except:
          showerror('错误','解密出错')

    def decryptFence(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          s=s.replace(' ','')
          s=s.replace('\n','')
          l=len(s)
          n=int(self.codeKey.get())
          if self.codeFlag.get()==1:
              result=encryptFunction.decryptFence(s,n)
          elif self.codeFlag.get()==2:
              result=s
              for i in range(2,(l+1)/2+1):
                  result+=u'\n%d栏：\n' % (i)
                  result+=encryptFunction.decryptFence(s,i)
          self.showResult(result)
        except:
          showerror('错误','解密出错')

    def encryptSysconvert(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          if s:
            if self.codeFlag.get()==1:
               result=encryptFunction.sysConvert(s,10,2)
            elif self.codeFlag.get()==2:
               result=encryptFunction.sysConvert(s,10,8)
            elif self.codeFlag.get()==3:
               result=encryptFunction.sysConvert(s,10,16)
            self.showResult(result)
        except:
          showerror('错误','加密出错')
              
    def decryptSysconvert(self):
        try:
          s=self.editBox.get(1.0,END)[:-1]
          if s:
            if self.codeFlag.get()==1:
               result=encryptFunction.sysConvert(s,2,10)
            elif self.codeFlag.get()==2:
               result=encryptFunction.sysConvert(s,8,10)
            elif self.codeFlag.get()==3:
               result=encryptFunction.sysConvert(s,16,10)
            self.showResult(result)
        except:
          showerror('错误','解密出错')


        
        
