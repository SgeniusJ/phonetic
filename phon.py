import json
from random import randint

with open("t.json","r",encoding="utf-8") as file:
    data=json.load(file)

parsed=[]
correct=0
for i in range(26):
    random_index=randint(0,25)
    while(random_index in parsed):
        random_index=randint(0,25)
    parsed.append(random_index)
    print(f"----------------------------------------------------------------------")
    print(f"What's the corresponding nato phonetic alphabet word for the letter: {list(data)[random_index]}")
    resp=input()
    if(resp==list(data.values())[random_index]):
        print(f"Correct\nRemaining:{26-len(parsed)}/26")
        correct+=1
    else:
        print(f"False\nRemaining:{26-len(parsed)}/26")

print(f"You have {correct} out of 26 \nScore:{round(correct/26*100)}%")
