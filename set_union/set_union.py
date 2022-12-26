# Enter your code here. Read input from STDIN. Print output to STDOUT

eng = int(input())
eng_stu = set(map(int,input().split()))
french = int(input())
french_stu = set(map(int,input().split()))
union = 0

for en in eng_stu:
    french_stu.add(en)

print(len(french_stu))