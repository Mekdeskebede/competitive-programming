# Enter your code here. Read input from STDIN. Print output to STDOUT

eng = int(input())
eng_stu = set(map(int,input().split()))
french = int(input())
french_stu = set(map(int,input().split()))
only_eng = 0

for en in eng_stu:
    if en not in french_stu:
        only_eng += 1

print(only_eng)