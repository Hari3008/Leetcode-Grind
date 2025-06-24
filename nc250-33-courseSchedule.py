class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            preMap[course].append(preq)
        
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            
            if preMap[course] == []:
                return True
            
            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visit.remove(course)
            preMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
