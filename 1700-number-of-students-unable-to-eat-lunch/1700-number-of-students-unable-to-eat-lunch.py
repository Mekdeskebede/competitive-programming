class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        eat = 0
        while True:
            if not students or not sandwiches:
                break
            elif students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                eat += 1
            elif sandwiches[0] not in students:
                break
            else:
                temp = students.pop(0)
                students.append(temp)
        return n - eat