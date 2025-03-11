# Medium
## 875. Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = `[3,6,7,11]`, h = `8`
Output: `4`

Example 2:
Input: piles = `[30,11,23,4,20]`, h = `5`
Output: `30`

# Key Idea
- If Koko eats at speed `k`, the time needed to finished pile `piles[i]` is:
`hours = sum(pile[i] + k - 1 // k)` 
- If using brute force, we must check all `k` value from `1` to `max(piles)` to find `k`, this will inefficient
- Eating speed of Koko: `low = 1` and `high = max(piles)` make we think of `binary search` to find minimum `k`

## Approach
1. Compute `mid = (low + high) // 2` (test eating speed at `k=mid`)
2. If `sum(pile[i] + k - 1 // k)` > `h` => we must increase speed => move `low = mid + 1`
3. If `sum(pile[i] + k - 1 // k)` <= `h` => we have adopt the requirement, this could be potential result => we could decrease speed => move `high = mid`