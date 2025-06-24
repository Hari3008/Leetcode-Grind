class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c:[] for c in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        # a course can have like 3 states
        # visited : course has been added to the output
        # visiting : course is not added to the output but is added in the cycle
        # unvisited : course is not added to the output or the cycle

        visit, cycle = set(), set()
        output = []

        def dfs(course):
            if course in cycle:
                return False # Cycle Detected!
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre): # Cycle detected
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output

