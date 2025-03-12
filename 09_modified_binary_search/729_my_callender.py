class MyCalender:
    def __init__(self):
        self.callender = []
    def book(self, startTime: int, endTime: int) -> bool:
        i, n = 0, len(self.callender)
        if not self.callender:
            self.callender.append([startTime, endTime])
            return True
        # step 1: check intervals before endTime
        while i < n and self.callender[i][1] <= startTime:
            i += 1
        # what happend when i = 0

        # first book is (10, 20)
        # second book is (15,25) or (0,10) are return i = 0

        # if i == n, it don't overlap with any element
        if i == n:
            self.callender.append([startTime, endTime])
            return True

        # step 2: check whether it have interval after 
        if i < n:
            after_book = self.callender[i]
            if endTime <= after_book[0]:  # can book
                self.callender.insert(i, [startTime, endTime])
                return True
            else: return False

        # self.callender.append([startTime, endTime])

    def print(self):
        print(self.callender)
        
myCalender = MyCalender()
print(myCalender.book(10,20))
print(myCalender.book(15,25))
print(myCalender.book(20,30))
myCalender.print()
