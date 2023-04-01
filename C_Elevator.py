test = int(input())

for _ in range(test):
    wf, et, ef = map(int,input().split()) 
   
    optimal = min(wf*ef, 2*(ef*et)) + min(wf*(4-ef),et*(4-ef))
    print(optimal)