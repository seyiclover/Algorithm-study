array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):        # 삽입정렬에서 가장왼쪽은 정렬이 완료된 데이터이기 때문에 비교하지 않는다. 
    for j in range(i, 0, -1):         # 오른쪽에서 왼쪽으로 이동하면서 비교 정렬 
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
