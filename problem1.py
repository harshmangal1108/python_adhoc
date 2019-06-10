
#!/usr/bin/python3
import datetime

name = str(input("Enter your name :"))
age=int(input("Enter your age :"))
d=datetime.datetime.now()


print("IN {},{} you will turn 95 ".format((95-age)+d.year,name) )
