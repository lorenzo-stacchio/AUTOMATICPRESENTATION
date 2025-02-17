import os


vtt = open("data\\transcript.vtt").readlines()
vtt = vtt[2:] # skip header
vtt = [line for line in vtt  if line != "\n" ]

subRip = ""

idx = 1
for index_line in range(0, len(vtt), 2): # skip header
    time_formatted = vtt[index_line].replace(".", ",").replace("\n", "")
    
    text = vtt[index_line+1]
    subRip += f"{idx}\n{time_formatted}\n{text}\n"
    # print(vtt[index_line],vtt[index_line+1])
    idx += 1
    # exit()
open("data\\transcript.srt", "w").writelines(subRip)
   
# print(vtt)