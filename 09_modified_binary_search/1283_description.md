# Medium
## 1283. Find the Smallest Divisor Given a Threshold
Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer `divisor`, divide all the array by it, and sum the division's result. Find the smallest `divisor` such that the result mentioned above is less than or equal to threshold.
Each result of the division is rounded to the nearest integer greater than or equal to that element. `(For example: 7/3 = 3 and 10/2 = 5).`
The test cases are generated so that there will be an answer

Example 1:
Input: nums =`[1,2,5,9]`, threshold = `6`\
Output: 5\
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.\
If the `divisor` is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).\

# Key Idea
**Note**
- The smaller divisor, the larger sum, but `sum <= threshold`
    - for example:
        - `divisor = 100` -> `sum = 4 < threshold` --> `100` is possible result and we can decrease the divisor to get the smallest divisor with `sum < threshold`
        - `divisor = 1` -> `sum = 17 > threshold` --> we must increase the divisor to satisfy the requirment
- If `sum > threshold` -> increase `divisor` to reduce sum 
- If `sum <= threshold` -> decrease `divisor` to increase sum.


# Medium
## 729. My Calendar I
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Example 1:\
Input\
["MyCalendar", "book", "book", "book"]\
[[], [10, 20], [15, 25], [20, 30]]\
Output\
[null, true, false, true]\

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

