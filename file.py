import time

start_time = time.time()

filename = "pg30.txt"

with open(filename) as kjv:
    bible = kjv.read()

sub_string = input("What word do you want to find in the Bible? ")

count = bible.count(sub_string)
cap_love = bible.count("Love")
print(count)
