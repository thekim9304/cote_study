이진 탐색 (Binary Search)
-
- 원하는 값 k를 찾는 과정
- 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
- 변수 3개 start, end, mid를 사용해 탐색
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾음
![binary_search_exam](https://blog.penjee.com/wp-content/uploads/2015/04/binary-and-linear-search-animations.gif)
```python
# 반복문으로 구현한 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 원하는 값 찾은 경우 인덱스 반환
        if array[mid] == target:
            return mid
        # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
        elif array[mid] > target:
            end = mid - 1
        # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
        else:
            start = mid + 1

    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result is None:
    print('원소가 존재 X')
else:
    print(result + 1)
```

```python
# 재귀 함수로 구현한 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result is None:
    print('원소가 존재 X')
else:
    print(result + 1)
```
Lower Bound
-
- 원하는 값 k 이상이 처음 나오는 위치를 찾는 과정
- binary search에서 조건만 바뀜
```python
def lower_bound(nums, target):
    
    start, end = 0, len(nums)
    
    while start < end:  #left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = start + (end - start) // 2
        
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid
    
    return end
```

Upper Bound
-
- 원하는 값 k를 초과한 값이 처음 나오는 위치를 찾는 과정
```python
def upper_bound(nums, target):

    left, right = 0, len(nums)

    while left < right:  #left와 right가 만나는 지점이 target값 보다 큰 값이 처음 나오는 위치
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid 

    return right
```