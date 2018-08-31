#Q.1- Print the current day using Datetime module.
import datetime as d
print(d.date.today())

#Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
a=input("search video")
webbrowser.open_new_tab('http://youtube.com/search?q=%s'%a)

#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
import os
path ='C:\\Users\\Viney Gautam\\Desktop\\ASSIGNMENT12\\a'
files = os.listdir(path)
i = 1
for file in files:
    a=input("name of file")
    os.rename(os.path.join(path, file), os.path.join(path, a+'.jpg'))
    i = i+1
