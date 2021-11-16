"""
yesterday.txt 파일읽어서
yesterday가 몇번 나오는지 count 해보기

open mode
r : read, w : write
rb : read binary, wb : write binary
a : append
"""

def file_read(file_name):
    with open(file_name,"r", encoding='utf-8') as file:
        lyric = file.read()
        return lyric

read = file_read("yesterday.txt")
print(read)

n_of_yesterday = read.count("yesterday")
print(f"NUMBER OF A WORD yesterday {n_of_yesterday}")

n_of_upper_yesterday = read.upper().count("YESTERDAY")
print(f"NUMBER OF A WORD UPPER YESTERDAY {n_of_upper_yesterday}")
