import collections


class Solution(object):
    # BFS
    def findOrder1(self, numCourses, prerequisites):
        # key是要上的课，value是上key课的前置条件
        pre = {i: set() for i in range(numCourses)}
        # key是前置条件课，value是后置课
        next = collections.defaultdict(set)
        for i, j in prerequisites:
            pre[i].add(j)
            next[j].add(i)
        queue = collections.deque(i for i in range(numCourses) if not pre[i])
        count, result = 0, []
        while queue:
            finished = queue.popleft()
            result.append(finished)
            count += 1
            for i in next[finished]:
                pre[i].remove(finished)
                if not pre[i]:
                    queue.append(i)
        return result if count == numCourses else []

    # DFS
    def findOrder(self, numCourses, prerequisites):
        # key是要上的课，value是上key课的前置条件
        pre = {i: set() for i in range(numCourses)}
        # key是前置条件课，value是后置课
        next = collections.defaultdict(set)
        for i, j in prerequisites:
            pre[i].add(j)
            next[j].add(i)
        stack = [i for i in range(numCourses) if not pre[i]]
        result = []
        while stack:
            finished = stack.pop()
            result.append(finished)
            for i in next[finished]:
                pre[i].remove(finished)
                if not pre[i]:
                    stack.append(i)
            pre.pop(finished)
        return result if not pre else []


if __name__ == "__main__":
    solution = Solution()
    solution.findOrder(3, [[1, 2]])
