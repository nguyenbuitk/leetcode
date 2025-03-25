# Medium
## 189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

```
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

# Key Idea
## Approach 1 Self
**`O(n) time, O(n) space`**
```
# Create new_nums       [1, 1, 1, 1, 2, 3, 4, 5, 6, 7]
# Revert new_nums       [5, 6, 7, 1, 2, 3, 4, 1, 1, 1]
# Cut new_nums          [5, 6, 7, 1, 2, 3, 4]
```

## Approach 2
**`O(n) time, O(n) space`**

**Explain with k = 3**
```
''' with k = 3
1, 2, 3, 4, 5, 6, 7       (nums_old)
            i
5, 6, 7, 1, 2, 3, 4       (nums_new)
j
j = i + 3 
nums_new[j] = nums_old[i]

<=> nums_new[i + 3] = num_old[i]
<=> nums_new[j] = nums_old[j-3]
```

## Approach 3
**`O(n) time, O(1) space`**

**Initial array with k = 3**\
`[1, 2, 3, 4, 5, 6, 7]`

1. Revert array
`[7, 6, 5, 4, 3, 2, 1]`

2. Revert `0 -> k` (not include)
`[5, 6, 7, 4, 3, 2, 1]`

3. Revert `k -> end`
`[5, 6, 7, 1, 2, 3, 4]`

## Apporach 4
With the explain of approach 2

**Ý tưởng của thuật toán trong code:**
- Dịch từng phần tử đến vị trí mới của nó trong mảng, lặp lại việc này cho đến khi tất cả các phần tử đều được dịch đúng vị trí.

- Sử dụng kỹ thuật "cyclic replacement" – thay thế tuần hoàn (vì một phần tử được thay thì phải giữ lại giá trị cũ để chuyển tiếp cho phần tử tiếp theo).
- Do có thể có nhiều chu kỳ (cycle), nên mỗi khi một vòng kết thúc (quay về chỉ số bắt đầu), ta tăng start để bắt đầu một chu kỳ mới.

###  Explain code
```python
int cntRotated = 0;
➡ Biến đếm số phần tử đã xoay xong.

int start = 0;
int curr = 0;
int numToBeRotated = nums[0];
➡ start là điểm bắt đầu của chu kỳ, curr là chỉ số hiện tại, numToBeRotated lưu giá trị cần xoay.

do {
    tmp = nums[(curr + k) % n];                           // Lưu giá trị tại vị trí đích
    nums[(curr + k) % n] = numToBeRotated;               // Đưa giá trị hiện tại vào vị trí đích
    numToBeRotated = tmp;                                // Cập nhật giá trị tiếp theo cần xoay
    curr = (curr + k) % n;                               // Di chuyển đến chỉ số tiếp theo trong chu kỳ
    cntRotated++;                                        // Tăng số phần tử đã xoay
} while (curr != start);                                 // Khi quay lại điểm bắt đầu thì kết thúc 1 chu kỳ

Khi một chu kỳ kết thúc:
start++;
curr = start;
numToBeRotated = nums[curr];
```

### Walk through
Khi n và k không chia hết cho nhau, sẽ có nhiều chu kỳ. `Ví dụ: n = 6, k = 2` thì không thể xoay toàn bộ trong 1 chu kỳ duy nhất. Do đó cần xử lý nhiều chu kỳ để xoay hết mảng.

#### Trường hợp 1: n chia hết cho k
```
nums = [1, 2, 3, 4, 5, 6], k = 2
n = 6, k = 2 → GCD(6,2) = 2 → sẽ có 2 chu kỳ
Kết quả mong đợi: [5, 6, 1, 2, 3, 4]
```
```
🔄 Cycle 1: start = 0
curr = 0, num = 1 → move to (0+2)%6 = 2
=> nums[2] = 1   (old 3)
curr = 2, num = 3 → move to (2+2)%6 = 4
=> nums[4] = 3   (old 5)
curr = 4, num = 5 → move to (4+2)%6 = 0
=> nums[0] = 5   (back to start)
✅ Đã hoàn thành 3 phần tử: cntRotated = 3
```

🔄 Cycle 2: start = 1
curr = 1, num = 2 → move to (1+2)%6 = 3
=> nums[3] = 2   (old 4)
curr = 3, num = 4 → move to (3+2)%6 = 5
=> nums[5] = 4   (old 6)
curr = 5, num = 6 → move to (5+2)%6 = 1
=> nums[1] = 6   (back to start)
✅ Hoàn thành tất cả 6 phần tử → DONE ✅

🔚 Final array:
[5, 6, 1, 2, 3, 4]



#### ❌ Trường hợp 2: n không chia hết cho k
```
Input:
nums = [1, 2, 3, 4, 5], k = 2
n = 5, k = 2 → GCD(5,2) = 1 → sẽ có 1 chu kỳ
Kết quả mong đợi: [4, 5, 1, 2, 3]
🔄 Cycle 1: start = 0
curr = 0, num = 1 → (0+2)%5 = 2
=> nums[2] = 1
curr = 2, num = 3 → (2+2)%5 = 4
=> nums[4] = 3
curr = 4, num = 5 → (4+2)%5 = 1
=> nums[1] = 5
curr = 1, num = 2 → (1+2)%5 = 3
=> nums[3] = 2
curr = 3, num = 4 → (3+2)%5 = 0
=> nums[0] = 4 (back to start)
✅ Đã đi qua tất cả 5 phần tử trong 1 chu kỳ
```


nếu n không chia hết cho k thì vẫn có thể cần nhiều chu kỳ (ví dụ n = 9, k = 6)

## Tóm tắt: GCD (Greatest Common Divisor) – Ước chung lớn nhất

Trường hợp	GCD(n, k)	Số chu kỳ	Mỗi chu kỳ dài
n = 6, k = 2	2	2	3
n = 5, k = 2	1	1	5
n = 8, k = 4	4	4	2
n = 7, k = 3	1	1	7

Số chu kỳ (cycle) = GCD(n, k)