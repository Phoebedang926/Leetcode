class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentq = deque(students)
        sandwichq = deque(sandwiches)
        studentnums = len(students)
        lastserve = 0
        while studentnums > lastserve:
            if studentq[0] == sandwichq[0]:
                studentq.popleft()
                sandwichq.popleft()
                lastserve = 0
                studentnums -=1
            else:
                studentq.rotate(-1)
                lastserve +=1
        return studentnums
            
        