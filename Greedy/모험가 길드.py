n = int(input())
fear = list(map(int, input().split()))

fear.sort()

groupCnt = 0        # 총 그룹의 수
cnt = 0             # 해당 그룹의 인원 수
for i in fear:
  cnt += 1      
  if cnt >= i:
    groupCnt += 1
    cnt = 0

print(groupCnt)
