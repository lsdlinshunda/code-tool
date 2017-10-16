# -*- coding: utf-8 -*-
#=============================================================================
#This module contains functions used in encrypting and decrypting.
#=============================================================================

from string import *

#从文件中读取生成密码表
def createKeydict(filename,flag):                         
    keyFile=open('password list/%s' % (filename),'r')
    keyList=keyFile.readlines()
    keyDict={}
    if flag==1:
      for i in range(len(keyList)):
        keyDict[keyList[i].split()[0]]=keyList[i].split()[1]
    elif flag==2:
      for i in range(len(keyList)):
        keyDict[keyList[i].split()[1]]=keyList[i].split()[0]
    keyFile.close()
    return keyDict

def caesar(s,n):
    n=int(n)
    result=''
    for i in s:
        if ord(i)>=ord('a') and ord(i)<=ord('z'):
            result=result+chr(ord('a')+(n+ord(i)-ord('a')) % 26)
        elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
            result=result+chr(ord('A')+(n+ord(i)-ord('A')) % 26)
        else:
            result=result+i
    return result

def vigenere(s,key,flag):
    key=lower(key)
    keyList=[]
    result=''
    for i in key:
        if ord(i)>=ord('a') and ord(i)<=ord('z'):
            keyList.append(int(ord(i)-ord('a')))
        elif i in '0123456789':
            keyList.append(int(i))
    j=0
    for i in range(len(s)):
        result+=caesar(s[i],flag*(keyList[j%len(keyList)]))
        if s[i].lower() in 'abcdefghijklmnopqrstuvwxyz':
            j+=1
    return result

def encryptMorse(s,dot,dash,barrier):
    morseDict=createKeydict('morse.txt',1)
    result=''
    s=lower(s)
    for i in s:
        if i in ['\n',' ']:
          result+=i
        elif i!=' ':
          result+=morseDict[i]+barrier
    newResult=''
    for i in result:
        if i=='*':
            newResult+=dot
        elif i=='-':
            newResult+=dash
        else:
            newResult+=i
    return newResult

def decryptMorse(s,dot,dash,barrier):
    morseDict=createKeydict('morse.txt',2)
    result=''
    newS=''
    for i in s:
        if i==dot:
            newS+='*'
        elif i==dash:
            newS+='-'
        elif i in ['\n',' ']:
            newS+=i+barrier
        else:
            newS+=i
    newS=newS.split(barrier)
    for i in newS:
        if i!='':
            if i in ['\n',' ']:
                result+=i
            else:
                result+=morseDict[i]
    return result

#替代密码（一个字母对应两个数字）
def encryptReplacecodeOne(s,filename):
    keyDict=createKeydict(filename,1)
    result=''
    s=lower(s)
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
          result+=keyDict[i]
        else:
          result+=i
    return result

def decryptReplacecodeOne(s,filename):
    keyDict=createKeydict(filename,2)
    result=''
    i=0
    while i<len(s):
        if filename=='vkey.txt':
          if s[i] in '0123456789-':
              result+=keyDict[s[i]+s[i+1]]
              i+=2
          else:
              result+=s[i]
              i+=1
        else:
          if s[i] in '0123456789':
              result+=keyDict[s[i]+s[i+1]]
              i+=2
          else:
              result+=s[i]
              i+=1

    return result

#替代密码（一个字母对应不同长度数字）
def encryptReplacecodeTwo(s,filename):
    keyDict=createKeydict(filename,1)
    result=''
    s=lower(s)
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
          result+=keyDict[i]+' '
        else:
          result+=i
    return result[:-1]

def decryptReplacecodeTwo(s,filename):
    keyDict=createKeydict(filename,2)
    result=''
    i=0
    key=''
    s+=' '
    while i<len(s):
      if s[i] in '0123456789':
          if key=='':
            key=s[i]
          else:
            key+=s[i]
      else:
          if key!='':
              result+=keyDict[key]
              key=''
          if s[i]!=' ':
              result+=s[i]
      i+=1
    return result

#替代密码（一个字母对应单个字母或符号）
def encryptReplacecodeThree(s,filename):
    keyDict=createKeydict(filename,1)
    keys=keyDict.keys()
    result=''
    for i in s:
        if i.lower() in keys and not i in keys:
            result+=keyDict[i.lower()].upper()
        elif i.lower() in keys and i in keys:
            result+=keyDict[i]
        else:
            result+=i
    return result

def decryptReplacecodeThree(s,filename):
    keyDict=createKeydict(filename,2)
    keys=keyDict.keys()
    result=''
    for i in s:
        if i.lower() in keys and not i in keys:
            result+=keyDict[i.lower()].upper()
        elif i.lower() in keys and i in keys:
            result+=keyDict[i]
        else:
            result+=i
    return result
      
def encryptNinekeyOne(s):
    return encryptReplacecodeOne(s,'ninekeyone.txt')

def decryptNinekeyOne(s):
    return decryptReplacecodeOne(s,'ninekeyone.txt')

def encryptNinekeyTwo(s):
    return encryptReplacecodeTwo(s,'ninekeytwo.txt')

def decryptNinekeyTwo(s):
    return decryptReplacecodeTwo(s,'ninekeytwo.txt')

def encryptAlpha(s):
    return encryptReplacecodeTwo(s,'alpha.txt')

def decryptAlpha(s):
    return decryptReplacecodeTwo(s,'alpha.txt')

def encryptVkey(s):
    return encryptReplacecodeOne(s,'vkey.txt')

def decryptVkey(s):
    return decryptReplacecodeOne(s,'vkey.txt')

def encryptQWE(s):
    return encryptReplacecodeThree(s,'qwe.txt')

def decryptQWE(s):
    return decryptReplacecodeThree(s,'qwe.txt')

def encryptFence(s,n):
    n=int(n)
    sList=['']*n
    j=0
    for i in s:
        if not i in [' ','\n']:
            sList[j]+=i
            j=(j+1) % n
    result=''
    for i in range(n):
        result+=sList[i]
    return result

def decryptFence(s,n):
    fenceList=['']*n
    lenList=len(s)/n
    lenflag=len(s)%n
    k=0
    for i in range(n):
        if lenflag!=0:
            for j in range(lenList+1):
                fenceList[i]+=s[k]
                k+=1
            lenflag-=1
        else:
            for j in range(lenList):
                fenceList[i]+=s[k]
                k+=1
    result=''
    for i in range(lenList+1):
        try:
           for j in range(n):
               result+=fenceList[j][i]
        except:
           return result

def sysConvert(s,m,n):
    if m==10:
        if n==2:
            result=bin(int(s))[2:]
        elif n==8:
            result=oct(int(s))[1:]
        elif n==16:
            result=hex(int(s))[2:]
        if result[-1]=='L':
            return result[:-1]
        else:
            return result
    elif n==10:
        return int(s,m)

def flashBack(s):
    result=''
    for i in range(len(s)-1,-1,-1):
        result+=s[i]
    return result
