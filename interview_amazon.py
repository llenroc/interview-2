# coding=utf-8
from __future__ import division
import os
import sys
import time
import copy
import json
import math
import heapq
import bisect
import random
import unittest
from collections import deque
from Queue import Queue, LifoQueue, PriorityQueue
from datetime import datetime, timedelta





class Solution(object):
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        indegree = [0]*numCourses
        edge = [[] for i in range(numCourses)]
        for pre in prerequisites:
            edge[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        queue = Queue()
        for idx, ind in enumerate(indegree):
            if ind == 0:
                queue.put(idx)

        cnt = 0
        res = []
        while not queue.empty():
            course = queue.get()
            res.append(course)
            cnt += 1
            for neighbor in edge[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.put(neighbor)

        if cnt != numCourses:
            return []
        return res
# sol = Solution()
# a=5
# b=[[1,0],[1,3],[2,3],[3,0],[4,1],[3,4],[4,2]]
# print sol.findOrder(a,b)



class Node(object):
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
    def __lt__(self, node):
        if self.d > node.d:
            return True
        elif self.d == node.d:
            if self.x > node.x:
                return True
            elif self.x == node.x:
                if self.y > node.y:
                    return True
        return False
# n1=Node(2,3,5)
# n2=Node(2,3,1)
# print n1>n2

class Solution1(object):

    def kClosetPoints1(self, points, origin, k):
        # not recommend
        if points is None or len(points) == 0:
            return []

        dist = [(-self.distance(p, origin), p) for p in points]
        heap = dist[:k]
        heapq.heapify(heap)

        for d in dist[k:]:
            if d[0] < heap[0][0]:
                continue
            elif d[0] > heap[0][0]:
                heapq.heapreplace(heap, d)
            else:
                if d[1][0] < heap[0][1][0]:
                    heapq.heapreplace(heap, d)
                elif d[1][0] == heap[0][1][0]:
                    if d[1][1] < heap[0][1][1]:
                        heapq.heapreplace(heap, d)

        # must sort finally!!!
        res = [p for _,p in heap]
        res.sort(key=lambda p:(self.distance(p,origin), p[0], p[1]))
        return res

    def distance(self, A, B):
        return (A[0] - B[0])**2 + (A[1] - B[1])**2

    def kClosetPoints2(self, points, origin, k):
        """
        :type points: [List[List[int]]]
        :type origin: [List[int]]
        :type k: int
        :rtype: [List[List[int]]]
        """
        if points is None or len(points) == 0:
            return []
        points = [Node(p[0], p[1], self.distance(p, origin)) for p in points]
        heap = points[:k]
        heapq.heapify(heap)

        for p in points[k:]:
            if p <= heap[0]:  # actually distance p is larger than heap[0]
                continue
            else:
                heapq.heapreplace(heap, p)
        res = [[n.x, n.y] for n in heapq.nsmallest(k, heap)][::-1]
        return res
# sol = Solution1()
# points=[(4,6),(4,7),(4,4),(2,5),(1,1),(2,-5)]
# origin=(0,0)
# k=5
# print sol.kClosetPoints1(points,origin,k)
# print sol.kClosetPoints2(points,origin,k)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution3(object):
    def maximumSubtree(self, root):
        # Binary Tree Maximum Path Sum??????????????????????????????????????????
        # ????????????????????????Subtree with Maximum Average???????????????????????????????????????
        #      ???????????????????????????????????????
        if root is None:
            return
        self.res = None
        self.total = -sys.maxint-1
        self.recursive(root)
        return self.res.val, self.total

    def recursive(self, node):
        if node is None:
            return 0

        left = self.recursive(node.left)
        right = self.recursive(node.right)

        current = node.val
        if left > 0:
            current += left
        if right > 0:
            current += right

        if current > self.total:
            self.total = current
            self.res = node

        return current
# node1=Node(-3)
# node2=Node(2)
# node3=Node(5)
# node4=Node(3)
# node5=Node(-1)
# node1.left=node2
# node1.right=node3
# node2.left=node4
# node2.right=node5
# sol=Solution3()
# print sol.maximumSubtree(node1)


class Solution4(object):
    def numberdecodeI(self, digit):
        digit_to_char = dict()
        for i in range(26):
            digit_to_char[str(i)] = chr(ord('a') + i)

        if len(digit) < 0:
            return []
        elif len(digit) == 1:
            return [digit_to_char[digit[0]]]

        pre_pre = [digit_to_char[digit[0]]]
        pre = [digit_to_char[digit[0]] + digit_to_char[digit[1]]]
        if digit_to_char.get(digit[:2]):
            pre.append(digit_to_char[digit[:2]])

        for i in range(2, len(digit)):
            tmp = [p+digit_to_char[digit[i]] for p in pre]
            if digit_to_char.get(digit[i-1:i+1]):
                tmp.extend([p+digit_to_char[digit[i-1:i+1]] for p in pre_pre])
            pre_pre = pre
            pre = tmp
        return pre

    def numberdecodeII(self, digit):
        # more simple
        self.result = []
        self.helper(digit, 0, '')
        return self.result

    def helper(self, digit, i, string):
        if i == len(digit):
            self.result.append(string)
            return

        char = chr(int(digit[i]) + ord('a'))
        self.helper(digit, i+1, string+char)

        if i < len(digit)-1:
            num = int(digit[i:i+2])
            if 9 < num < 26:
                char = chr(num + ord('a'))
                self.helper(digit, i+2, string+char)
# sol=Solution4()
# digit='226'
# digit='005'
# print sol.numberdecodeI(digit)
# print sol.numberdecodeII(digit)



class Solution5(object):
    def kSubString(self, string, k):
        '''
        k substring which contains k-1 distinct letters
        string (str): input string
        k (int): sub string with length of k
        '''
        if len(string) < k:
            return []
        count_map = dict()
        i, j = 0, 0
        res = []
        while j < k:
            if string[j] not in count_map:
                count_map[string[j]] = 1
            else:
                count_map[string[j]] += 1
            j += 1
        if len(count_map) == k - 1:
            res.append(string[i:j])
        for m in range(k, len(string)):
            if string[m] not in count_map:
                count_map[string[m]] = 1
            else:
                count_map[string[m]] += 1
            count_map[string[i]] -= 1
            if count_map[string[i]] == 0:
                del count_map[string[i]]
            i += 1
            j += 1
            if len(count_map) == k - 1:
                res.append(string[i:j])
        return res

    def kSubString1(self, string, k):
        # ???kSubString????????????
        if string is None or len(string) == 0:
            return []

        res = []
        char_map = dict()
        for i in range(len(string)):
            if string[i] not in char_map:
                char_map[string[i]] = 1
            else:
                char_map[string[i]] += 1

            if i-k >= 0:
                char_map[string[i-k]] -= 1
                if char_map[string[i-k]] == 0:
                    del char_map[string[i-k]]

            if i >= k-1:
                if len(char_map) == k-1:
                    res.append(string[(i-k+1):i+1])
        return res

    def longestSubstring(self, s):
        # Longest Substring Without Repeating Characters
        # ??????hashmap?????????????????????????????????????????????
        if len(s) <= 1:
            return len(s)
        char_map = dict()
        res = 0
        left = -1
        for idx, i in enumerate(s):
            if i in char_map and char_map[i] > left:
                left = char_map[i]
            char_map[i] = idx
            res = max(res, idx-left)
        return res

    def longestSubstringK(self, s, k):
        # Longest Substring with At Most K Distinct Characters
        # ????????????????????????????????????????????????????????????????????????k???
        # ??????hashmap???????????????????????????????????????
        if s is None:
            return 0
        char_map = dict()
        res = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]] = 1
            else:
                char_map[s[i]] += 1
            while len(char_map) > k:
                char_map[s[start]] -= 1
                if char_map[s[start]] == 0:
                    del char_map[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res

    def numberOfSubstringK(self, string, k):
        # count number of substrings with 
        # exactly k distinct characters
        # ????????????????????????????????????????????????k
        # ????????????????????????????????????????????????????????????????????????o(n)
        # ?????????numberOfSubstringK1???????????????o(nk)
        """
        :type string: str
        :type k: int
        "rtype": List[str]
        """
        # corner cases
        if string is None or string is '' or len(string) < k:
            return []

        # init variables
        char_map = dict()
        res = []
        start = 0
        end = 0
        count = 0

        # main loop
        while end < len(string):

            # if char is in map, add it to map; if not, set value to 1 
            # and increase count by one
            c = string[end]
            if c not in char_map:
                char_map[c] = 1
                count += 1
            else:
                char_map[c] += 1
            end += 1

            # if count is equal to k, it means the window has k distinct chars
            if count == k:
                res.append(string[start:end])

            # if the window has chars more than k, move end pointer to left by 1 
            if count > k:
                end -= 1

                # if count is larger than k, move start pointer to right
                # until the count is equal to k
                while count > k:
                    char_map[string[start]] -= 1
                    if char_map[string[start]] == 0:
                        count -= 1
                        del char_map[string[start]]
                    start += 1

                    # add to result if not deleting a char from map
                    if count > k:
                        res.append(string[start:end])

                    # add to result if deleting a char from map
                    if count == 2:
                        end += 1
                        res.append(string[start:end])
        return res

    def numberOfSubstringK1(self, string, k): 
        n = len(string) 
        res = []
 
        for i in range(0, n): 
            count = 0
            char_map = dict()
            for j in range(i, n): 
 
                if string[j] not in char_map:
                    count += 1
                    char_map[string[j]] = 1
                else:
                    char_map[string[j]] += 1

                if count == k: 
                    res.append(string[i:j+1])
                if count > k: 
                    break
        return res  

    def substringk(self, string, k):
        #Substrings of size K with K distinct chars
        #???numberOfSubstringK1???????????????subtring????????????k
        #??????????????????????????????
        if string is None or len(string) == 0:
            return []
        char_map = {}
        start = 0
        res = []
        for i,c in enumerate(string):
            if c in char_map and char_map[c] >= start:
                start = char_map[c]+1
            if i+1-start==k:
                res.append(string[start:i+1])
                start += 1
            char_map[c] = i
        return list(set(res))

# sol=Solution5()
# a='abccdad'
# b=4
# print sol.kSubString(a, b)
# print sol.kSubString1(a, b)
# a='abcabfsdcbb'
# a='abcabcbb'
# a='awaglknagawunagwkwagl'
# print sol.longestSubstring(a)
# a='abccde'
# a='pqpqs' # [???pq???, ???pqp???, ???pqpq???, ???qp???, ???qpq???, ???pq???, ???qs???] 
# print sol.numberOfSubstringK1(a, 4)
# a='abcabc'
# a='awaglknagawunagwkwagl'
# print(sol.substringk(a, 3))


# ?????????????????????????????????????????????-1
def binarySearch1(nums, target):
    left, right = 0, len(nums)
    while left + 1 < right:
        mid = left + (right - left)/2
        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            return mid
    return -1

# ????????????????????????????????????????????????
def binarySearch2(nums, target):
    left, right = 0, len(nums)-1
    while left + 1 < right:
        mid = left + (right - left)/2
        if nums[mid] <= target:
            left = mid
        elif nums[mid] > target:
            right = mid
    if nums[left] > target:
        return left
    if nums[right] <= target:
        return -1
    return right
# a=[1,2,5,5,6,8]
# b=5
# print binarySearch2(a,2)


class Solution6(object):
    def twoSumCloset1(self, nums, target):
        # two sum closet from one list
        nums.sort()
        i, j = 0, len(nums)-1
        diff = sys.maxint
        res = None
        while i < j:
            tmp = target - nums[i] - nums[j]
            if tmp > 0:
                if diff > tmp:
                    diff = tmp
                    res = nums[i], nums[j]
                i += 1
            elif tmp < 0:
                if diff > -tmp:
                    diff = -tmp
                    res = nums[i], nums[j]
                j -= 1
            else:
                diff = 0
                res = i, j
                break
        return diff, res

    def twoSumCloset2(self, forward, backward, target):
        # ??????????????????????????????
        closet_sum = -sys.maxint-1
        res = []
        for fw in forward:
            for bw in backward:
                tmp = fw[1] + bw[1]
                if tmp > target:
                    continue
                if tmp == closet_sum:
                    res.append([fw[0], bw[0]])
                elif tmp > closet_sum:
                    res = [[fw[0], bw[0]]]
                    closet_sum = tmp
        return res

    def twoSumCloset3(self, forward, backward, target):
        # ????????????????????????+??????????????????nlogn + mlogm + nlogm
        # ??????1?????????+??????
        # ??????2?????????+?????????
        # ????????????m???n???????????????????????????2??????1
        #      ???m????????????n????????????1?????????2?????????mlogm>m>>nlogm
        forward.sort(key=lambda r:r[1])
        backward.sort(key=lambda r:r[1])
        backward_dist = [i[1] for i in backward]
        closet_sum = -sys.maxint-1
        res = []
        for fw in forward:
            idx = binarySearch2(backward_dist, target-fw[1])
            if idx == -1:
                break
            tmp = fw[1] + backward_dist[idx]
            if tmp > target:
                continue
            if tmp == closet_sum:
                res.append([fw[0], backward[idx][0]])
            elif tmp > closet_sum:
                res = [[fw[0], backward[idx][0]]]
                closet_sum = tmp
        return res

    def twoSumCloset4(self, forward, backward, target):
        # ????????????????????????+?????????????????????nlogn + mlogm + n + m
        forward.sort(key=lambda r:r[1])
        backward.sort(key=lambda r:r[1])
        idx = 0
        res = []
        while idx < len(backward) and target - forward[0][1] >= backward[idx][1]:
            idx += 1
        idx -= 1

        closet_sum = -sys.maxint-1
        i = 0
        while idx >= 0 and i < len(forward):
            tmp = forward[i][1] + backward[idx][1]
            if tmp > target:
                idx -= 1
                continue
            if tmp == closet_sum:
                res.append([forward[i][0], backward[idx][0]])
            elif tmp > closet_sum:
                res = [[forward[i][0], backward[idx][0]]]
                closet_sum = tmp
            i += 1
        return res

    def threeSum(self, nums, target):
        num_map = {}
        for idx, i in enumerate(nums):
            num_map[i] = idx

        for idx, i in enumerate(nums):
            res = self.twoSum(nums, num_map, target-i, idx)
            if res is not None:
                return idx, res[0], res[1]
        return None

    def twoSum1(self, nums, num_map, target, third):
        # helper function for threesum
        i, j = 0, len(nums)-1
        for i in range(len(nums)):
            if i == third:
                continue
            t = target - nums[i]
            if t in num_map and num_map[t] != i and num_map[t] != third:
                return i, num_map[t]
        return None

    def twoSum2(self, nums, target):
        """
        ?????????leetcode???
        """
        memory = {}
        for i in range(len(nums)):
            if target - nums[i] in memory:
                return [memory[target - nums[i]], i]
            else:
                memory[nums[i]] = i


# sol=Solution6()
# a=[-1, 0, 1, 2, -1, -4]
# b=0
# print sol.twoSumCloset1(a,b)
# a=[[1, 3000],[2, 5000],[3, 7000],[4, 10000]]
# b=[[1, 2000],[2, 3000],[3, 4000],[4, 5000]]
# c=7000
# print sol.twoSumCloset2(a,b, c)
# a=[[1, 3000],[2, 5000],[3, 7000],[4, 10000]]
# b=[[1, 2000],[2, 3000],[3, 4000],[4, 5000]]
# c=7000
# print sol.twoSumCloset3(a,b, c)
# a=[[1, 3000],[2, 5000],[3, 7000],[4, 10000]]
# b=[[1, 2000],[2, 3000],[3, 4000],[4, 5000]]
# c=7000
# print sol.twoSumCloset4(a,b, c)
# a=[-1, 0, 1, 2, -1, -4]
# b=0
# print sol.threeSum(a,b)
# a=[5, 2, 8, 15]
# b=10
# print 11,sol.twoSum(a,b)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution7(object):
    def mergeTwoSortedLinkedList(self, l1, l2):
        # merge two sorted linked list
        dummy = Node(0)
        tmp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        if l1 is not None:
            tmp.next = l1
        if l2 is not None:
            tmp.next = l2
        return dummy.next

# l1=Node(1)
# l1.next = Node(3)
# l1.next.next = Node(5)
# l2=Node(2)
# l2.next = Node(3)
# sol=Solution7()
# node=sol.mergeTwoSortedLinkedList(l1, l2)
# while node:
#     print node.val
#     node=node.next

class Solution8(object):
    def minimumDistanceMaze(self, maze, start, end):
        # maze II
        m, n = len(maze), len(maze[0])
        if m == 0 or n == 0:
            return -1
        dists = [[sys.maxint]*n for i in range(m)]
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        queue = Queue()
        queue.put(start)
        dists[start[0]][start[1]] = 0
        while not queue.empty():
            pos = queue.get()
            for d in directions:
                x, y = pos[0], pos[1]
                dist = dists[x][y]
                while x < m and x >= 0 and y < n and y >= 0 and maze[x][y] != 1:
                    x += d[0]
                    y += d[1]
                    dist += 1
                x -= d[0]
                y -= d[1]
                dist -= 1
                if dists[x][y] > dist:
                    dists[x][y] = dist
                    if x != end[0] or y != end[1]:
                        queue.put([x, y])
        return -1 if dists[end[0]][end[1]] == sys.maxint else dists[end[0]][end[1]]

    def minimumDistance(self, maze, start, end):
        # ??????????????????1???????????????0?????????????????????????????????
        if maze is None or len(maze) == 0 or len(maze[0]) == 0:
            return -1
        m, n = len(maze), len(maze[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        queue = Queue()
        queue.put(start)
        queue.put(None)
        distance = 0
        visited = [[0]*n for _ in range(m)]
        visited[0][0] = 1
        while not queue.empty():
            pos = queue.get()
            if pos is not None:
                if pos[0] == end[0] and pos[1] == end[1]:
                    return distance
                for direct in directions:
                    x, y = pos[0]+direct[0], pos[1]+direct[1]
                    if x >= 0 and x < m and y >= 0 and y < n and \
                        visited[x][y] == 0 and maze[x][y] == 0:
                        queue.put([x, y])
                        visited[x][y] = 1
            else:
                if queue.empty():
                    return -1
                queue.put(None)
                distance += 1
        return -1
# maze = [[0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 0],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0]]
# a=[0,4]
# b=[4,4] # True
# b=[3,2] # False
# sol=Solution8()
# print sol.minimumDistanceMaze(maze, a, b)
# maze = [[0,0,0,0,0],
#         [0,1,0,1,0],
#         [0,1,0,0,0],
#         [0,1,1,0,1],
#         [0,0,0,0,0]]
# a=[0,0]
# b=[2,3]
# print sol.minimumDistance(maze, a, b)


class Solution9(object):
    def combinationSum1(self, nums, target):
        # combination I
        # ?????????unique int array????????????????????????????????????sum target???combination
        nums.sort()
        self.nums = nums
        self.res = []
        self.recursion1([], 0, target)
        return self.res

    def recursion1(self, current, start, target):
        if target == 0:
            current_ = copy.copy(current)
            self.res.append(current_)
        if target <= 0:
            return
        for i in range(start, len(self.nums)):
            current.append(self.nums[i])
            self.recursion1(current, i, target-self.nums[i])
            current.pop()

    def combinationSum2(self, nums, target):
        # combination II
        # ??????????????????????????????????????????????????????
        nums.sort()
        self.nums = nums
        self.res = []
        self.recursion2([], 0, target)
        return self.res

    def recursion2(self, current, start, target):
        if target == 0:
            current_ = copy.copy(current)
            self.res.append(current_)
        if target <= 0:
            return
        for i in range(start, len(self.nums)):
            # remove deduplicate combinations 
            if i > start and self.nums[i] == self.nums[i-1]:
                continue
            current.append(self.nums[i])
            self.recursion2(current, i+1, target-self.nums[i])
            current.pop()
# sol=Solution9()
# a,b=[2,3,6,7],7
# a,b=[1,2,3,10],30
# print sol.combinationSum1(a,b)
# a=[10,1,2,7,6,1,5] # [1, 1, 2, 5, 6, 7, 10]
# b=8
# print sol.combinationSum2(a,b)


def search2DMatrix(matrix, target):
    # 240. Search a 2D Matrix II
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    m, n = len(matrix), len(matrix[0])
    x, y = m-1, 0
    while x >= 0 and y < n:
        if target > matrix[x][y]:
            y += 1
        elif target < matrix[x][y]:
            x -= 1
        else:
            return True
    return False
# matrix=[[1, 4, 7, 11, 15], 
#         [2, 5, 8, 12, 19], 
#         [3, 6, 9, 16, 22], 
#         [10, 13, 14, 17, 24], 
#         [18, 21, 23, 26, 30]]
# print search2DMatrix(matrix, 5)
# print search2DMatrix(matrix, 20)


def minimumPathSum(matrix):
    # minimum path sum
    # 1. ??????????????????????????????????????????1
    # 2. ???????????????????????????????????????????????????m???????????????m*n????????????
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return -1
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                matrix[i][j] += matrix[i][j-1]
            elif j == 0:
                matrix[i][j] += matrix[i-1][j]
            else:
                matrix[i][j] += min(matrix[i][j-1], matrix[i-1][j])
    return matrix[-1][-1]
# matrix=[[5, 6, 1], 
#         [2, 7, 1], 
#         [9, 3, 5]]
# print minimumPathSum(matrix)


def findAllDuplicates(nums):
    # Find All Duplicates in an Array
    # ??????1~n?????????????????????????????????
    # ??????o(n)?????????o(1)
    if nums is None or len(nums) == 0:
        return []
    res = []
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] < 0:
            res.append(idx+1)
        nums[idx] = -nums[idx]
    print nums
    return res
# a=[1]
# a=[4,1,1,3,2,7,1,8,2,3]
# print findAllDuplicates(a)


def highHive(scores, k):
    # There are two properties in the node student??id??and??scores, 
    # to ensure that each student will have at least 5 points, 
    # find the average of 5 highest scores for each person
    if scores is None or len(scores) == 0 or k <= 0:
        return []
    res = []
    score_map = dict()
    for i, score in scores:
        if i not in score_map:
            score_map[i] = PriorityQueue()
            score_map[i].put(score)
        else:
            score_map[i].put(score)
            if score_map[i].qsize() > k:
                _ = score_map[i].get()
    for i, queue in score_map.items():
        total = 0
        while not queue.empty():
            total += queue.get()
        res.append((i, total*1.0/k))
    return res
# scores=[[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
# k=5
# print highHive(scores, k)
# scores.sort(key=lambda r:(r[0], r[1]))
# print scores


class Solution10(object):
    # 341. Flatten Nested List Iterator
    # ????????????????????????????????????
    def __init__(self, nums):
        self.nums = nums
        self.queue = Queue()
        self.helper(self.nums)

    def next(self):
        while not self.queue.empty():
            return self.queue.get()
        return None

    def helper(self, nums):
        for i in range(len(nums)):
            if isinstance(nums[i], int):
                self.queue.put(nums[i])
            elif isinstance(nums[i], list):
                self.helper(nums[i])
            else:
                raise ValueError('Element of list must be a list or int!')

    def hasNext(self):
        return not self.queue.empty()


class Solution11(object):
    # 341. Flatten Nested List Iterator
    # ?????????????????????????????????yield???????????????pythonic???????????????dfs???????????????
    def __init__(self, nums):
        self.nums = nums
        self.queue = LifoQueue()
        self.top = None
        for i in range(len(nums)-1, -1, -1):
            self.queue.put(nums[i])

    def next(self):
        return self.top

    def hasNext(self):
        while not self.queue.empty(): # ????????????????????????????????????????????????next
            element = self.queue.get()
            if isinstance(element, int):
                self.top = element
                return True
            else:
                for i in range(len(element)-1, -1, -1):
                    self.queue.put(element[i])
        return False
# a=[[1,1],2,[1,1]]
# a=[3,[2,[6]],[[5,[1]],[2,3]]]
# sol=Solution11(a)
# while sol.hasNext():
#     print sol.next()


class Solution12(object):
    def gcdArray(self, nums):
        # given a list of int, find gcd for all ints
        if len(nums) <= 1:
            return -1
        res = nums[0]
        for i in range(1, len(nums)):
            res = self.gcd(res, nums[i])
        return res

    def gcd(self, a, b):
        # 845. Greatest Common Divisor
        if a == 0 or b == 0:
            return 0
        a, b = self.swap(a, b)
        while a%b != 0:
            a = a%b
            # a, b = self.swap(a, b)
            tmp = a
            a = b
            b = tmp
        return b

    def swap(self, a, b):
        if a < b:
            tmp = a
            a = b
            b = tmp
        return a, b
# sol=Solution12()
# print sol.gcd(1,15)
# a=[2,4,6,8,10]
# a=[24,18,36]
# print sol.gcdArray(a)


# ???????????????
# ????????????+????????????+????????????
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]] or target is None:
            return False
        
        colLen = len(matrix[0])-1
        row = 0

        #checks to find where row might be 
        while True:
            if matrix[row][0] <= target <= matrix[row][colLen]:
                break
            else:
                #checks to make sure we don't go over the number of rows
                if row < len(matrix)-1:
                    row+=1
                else:
                    break

        #search through just that one row using binary search
        left = 0
        right = colLen

        while left<=right:
            mid = left+(right-left)/2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid+1
            elif matrix[row][mid]> target:
                right = mid-1
        return False

def gray_code(a, b):
    # ????????????????????????gray code?????????????????????????????????
    c = a^b
    count = 0
    while c != 0:
        if c&1 == 1:
            count += 1
        c >>= 1
    return 1 if count == 1 else 0
# a=int('0b101011', 2)
# b=int('0b101010', 2)
# print gray_code(a, b)



def numOfArithmeticSlices(nums):
    """
    LeetCode 413. Arithmetic Slices
    :type: List[int]
    :rtype: int
    """
    # corner case
    if nums is None or len(nums) < 3:
        return 0

    # init variables
    count = 0
    add = 0

    # main loop
    for i in range(2, len(nums)):
        # if current sub array is AS
        # add to total value
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            add += 1
            count += add
        else:
            # the current sub is not AS
            # and set add to 0
            add = 0
    return count
# a=[1,2,3,4,5,6] # 10
# a=[1,3,5,6,7]
# print numOfArithmeticSlices(a)



def windowMinimum(nums, k):
    """
    window minimum????????????????????????????????????????????????4, 2, 12, 11, -5???
    ??????size???2????????????ArrayList??????2, 2, 11, -5
    ?????????????????????????????????list?????????
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if nums is None or len(nums) == 0 or len(nums) < k:
        return []

    # minimums serves as a deque, saving the number indices
    res = []
    minimums = []
    start = 0
    for i in range(len(nums)):
        # remove elments that are beyond window
        while len(minimums)-start > 0 and minimums[start] < i-k+1:
            start += 1

        # remove larger elements than current one, keeping ascending order 
        # in the window
        while len(minimums)-start > 0 and nums[minimums[-1]] > nums[i]:
            minimums.pop()

        # add current number into minimums
        minimums.append(i)
        if i-k+1 >= 0:
            res.append(nums[minimums[start]])
    return res
# a=[4,2,3,-2,7,1,12,11,-5]
# b=3
# print windowMinimum(a,b)


class UnionFind(object):
    # ?????????????????????count_map??????????????????????????????????????????
    def __init__(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = -1

    def compressed_find(self, x):
        parent = self.father[x]
        if parent != -1:
            parent = self.compressed_find(parent)
            # reduce parents
            self.father[x] = parent
        return x if parent == -1 else parent

    def union(self, x, y):
        fa_x = self.compressed_find(x)
        fa_y = self.compressed_find(y)
        if fa_x != fa_y:
            self.father[fa_x] = fa_y

def validTree(n, edges):
    # 1. ?????????????????????
    # 2. ??????????????????????????????????????????????????????????????????
    #    ?????????????????????????????????????????????????????????????????????????????????n?????????
    if len(edges) != n - 1:
        return False
    uf = UnionFind(n)
    
    for edge in edges:
        a, b = edge
        father_a = uf.compressed_find(a)
        father_b = uf.compressed_find(b)
        if father_a == father_b:
            return False
        else:
            uf.union(a, b)
    return True
# print validTree(5, [[2,3], [0,2], [0,3], [1,4]])


class UnionFindSet(object):
    # ?????????????????????count_map???????????????????????????
    def __init__(self, nums):
        self.father_map = {}
        self.count_map = {}
        for i in nums:
            self.father_map[i] = -1
            self.count_map[i] = 1

    def union(self, m, n):
        father_m = self.find_father(m)
        father_n = self.find_father(n)
        # keep balance
        if father_m != father_n:
            if self.count_map[father_m] >= self.count_map[father_n]:
                self.father_map[father_n] = father_m
                self.count_map[father_n] += self.count_map[father_m]
            else:
                self.father_map[father_m] = father_n
                self.count_map[father_m] += self.count_map[father_n]

    def find_father(self, n):
        father_n = self.father_map[n]
        if father_n != -1:
            father_n = self.find_father(father_n)
            # reduce parents
            self.father_map[n] = father_n
        return n if father_n == -1 else father_n

    def is_same_group(self, m, n):
        return self.find_father(m) == self.find_father(n)

    def find_islands(self):
        num = 0
        for i in self.father_map.values():
            if i == -1:
                num += 1
        return num
# a = [0,1,2,3,4,5,6]
# union_find_set = UnionFindSet(a)
# union_find_set.union(0,2)
# union_find_set.union(3,5)
# union_find_set.union(2,3)
# union_find_set.union(2,6)
# union_find_set.union(1,4)
# print union_find_set.is_same_group(1,5)  #True
# print union_find_set.father_map
 
# a = [0,1,2,3,4]
# union_find_set = UnionFindSet(a)
# for i in [[2,3], [2,0], [0,3], [1,4]]: union_find_set.union(*i)
# print union_find_set.father_map
# print union_find_set.find_islands()


class solution22(object):
    def numOfIslands(self, m, n, nums):
        # number of islands II, ????????????
        islands = [[0]*n for i in range(m)]
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        count = 0
        res = []
        for pos in nums:
            x, y = pos
            islands[x][y] = 1
            count += 1
            for direct in directions:
                x_, y_ = x + direct[0], y + direct[1]
                if x_ >= m or x_ < 0 or y_ >= n or y_ < 0:
                    continue
                if islands[x_][y_] == 1:
                    count -= 1
            res.append(count)
        return res
# sol=solution22()
# m,n=4,4
# nums=[[0,0], [1,0], [2,0], [2,1], [2,2], [1, 2], [0, 2], [0, 1]]
# # [[1, 1, 1, 0], 
# #  [1, 0, 1, 0], 
# #  [1, 1, 1, 0], 
# #  [0, 0, 0, 0]]
# print sol.numOfIslands(m,n,nums)


class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None
        self.random = None

class Solution21(object):
    def copyRandomPointer(self, head):
        # copy random pointer
        cur = head
        while cur is not None:
            next_node = Node(cur.val)
            next_node.next = cur.next
            cur.next = next_node
            cur = cur.next.next

        pre = head
        cur = head.next
        while pre is not None:
            cur.random = pre.random.next
            if cur.next is None:
                break
            pre = pre.next.next
            cur = cur.next.next

        pre = head
        cur = head.next
        new_head = head.next
        while pre is not None:
            if cur.next is None:
                pre.next = None
                break
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        return new_head
# root = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# root.next = node2
# root.random = node3
# node2.next = node3
# node2.random = node3
# node3.next = node4
# node3.random = node2
# node4.random = root
# sol=Solution21()
# res=sol.copyRandomPointer(root)
# while res:
#     if res.random:
#         print res.val, res.random.val
#     else:
#         print res.val
#     res = res.next


class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution19(object):
    def addTwoNumbers(self, l1, l2):
        # Add Two Numbers II
        #  ???????????????????????????????????????????????????
        q1 = LifoQueue()
        q2 = LifoQueue()

        tmp = l1
        while tmp is not None:
            q1.put(tmp.val)
            tmp = tmp.next

        tmp = l2
        while tmp is not None:
            q2.put(tmp.val)
            tmp = tmp.next

        total = 0
        node = None
        while not q1.empty() or not q2.empty():
            if not q1.empty():
                total += q1.get()
            if not q2.empty():
                total += q2.get()
            res = total%10
            head = Node(res)
            head.next = node
            node = head
            total /= 10

        if total != 0:
            head = Node(total)
            head.next = node
            node = head
        return node
# l1 = Node(7)
# l1.next = Node(2)
# l1.next.next = Node(4)
# l1.next.next.next = Node(3)
# l2 = Node(5)
# l2.next = Node(6)
# l2.next.next = Node(4)
# sol=Solution19()
# res=sol.addTwoNumbers(l1, l2)
# while res:
#     print res.val
#     res = res.next


class Solution22(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = list()
        max_area = 0

        stack.append([heights[0], 1])
        j = 1
        # while len(stack) > 0 and j < len(heights):
        while j < len(heights):
            tw = 1
            while len(stack) > 0 and heights[j] < stack[-1][0]:
                h, w = stack.pop(-1)
                max_area = max(max_area, (w+tw-1)*h)
                tw += w
            stack.append([heights[j], tw])
            j += 1
        
        tw = 0
        while len(stack) > 0:
            h, w = stack.pop(-1)
            tw += w
            max_area = max(max_area, h*tw)
        return max_area 
# sol=Solution22()
# a=[2,1,5,6,2,3] #10
# # a=[3,6,5,7,4,8,1,0] #20
# print sol.largestRectangleArea(a)


class Solution23(object):
    tmp  = []
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def quickSort(self, nums):
        self.helper1(nums, 0, len(nums)-1)
        return nums

    def helper1(self, nums, start, end):
        if start < end:
            mid = self.partition(nums, start, end)
            self.helper1(nums, start, mid)
            self.helper1(nums, mid+1, end)

    def partition(self, nums, start, end):
        i, j = start, end
        while i < j:
            while i < j and nums[i] <= nums[j]:
                j -= 1
            self.swap(nums, i, j)
            while i < j and nums[i] <= nums[j]:
                i += 1
            self.swap(nums, i, j)
        return i

    def mergeSort(self, nums):
        self.helper2(nums, 0, len(nums)-1)
        return nums

    def helper2(self, nums, start, end):
        if start < end:
            mid = start + (end - start)/2
            self.helper2(nums, start, mid)
            self.helper2(nums, mid+1, end)
            self.merge(nums, start, mid, end)

    def merge(self, nums, start, mid, end):
        i, j = start, mid+1
        idx = 0
        while i <= mid and j <= end:
            if nums[i] < nums[j]:
                self.tmp.append(nums[i])
                i += 1
            else:
                self.tmp.append(nums[j])
                j += 1
        while i <= mid:
            self.tmp.append(nums[i])
            i += 1
        while j <= end:
            self.tmp.append(nums[j])
            j += 1
        for i in range(0, end-start+1):
            nums[start+i] = self.tmp[i]
        self.tmp = []
# sol=Solution23()
# a=[2,1,5,6,2,3]
# a=[2,3,2,2,4,2]
# print sol.quickSort(a)
# print sol.mergeSort(a)



class Solution24(object):
    def wordBreakI(self, s, wordDict):
        '''Word break I, dynamic programming, time: o(n^2)
        '''
        pass

    def wordBreakII(self, s, wordDict):
        self.wordSet = set(wordDict)
        self.wordMap = dict()
        self.dfs(s)
        return self.wordMap[s]

    def dfs(self, s):
        if s in self.wordMap:
            return self.wordMap[s]
        if s is '':
            return ['']
        result = []
        for i in range(1, len(s)+1):
            subStr = s[:i]
            if subStr in self.wordSet:
                res = self.dfs(s[i:])
                for r in res:
                    result.append('{} {}'.format(subStr, r).strip())
        self.wordMap[s] = result
        return result
# sol=Solution24()
# a='leetcode'
# b=['leet', 'code']
# a='catsanddog'
# b=["cat", "cats", "and", "sand", "dog"]
# a='pineapplepenapple'
# b=["apple", "pen", "applepen", "pine", "pineapple"]
# print(sol.wordBreakII(a, b))


class Solution25(object):
    def uglyNumberII(self, n):
        '''return the nth ugly number
        ???????????????????????????????????????2???3???5?????????????????????????????????
        '''
        res = [1]
        i, j, k = 0, 0, 0
        while len(res) < n:
            p1 = res[i] * 2
            p2 = res[j] * 3
            p3 = res[k] * 5
            m = min(p1, min(p2, p3))
            if m == p1: i += 1
            elif m == p2: j += 1
            else: k += 1
            if m == res[-1]: continue
            res.append(m)
        print res
        return res[n-1]
    def nthUglyNumber(self, n, primes):
        if n == 1: return 1
        res = [1]
        indexes = [0]*len(primes)
        while True:
            min_val, min_idx = float('inf'), 0
            for idx,prime in enumerate(primes):
                val = res[indexes[idx]]*prime
                if min_val > val:
                    min_val = val
                    min_idx = idx
            indexes[min_idx] += 1
            if min_val == res[-1]: continue
            res.append(min_val)
            if len(res) == n:
                return res[-1]
    def nthUglyNumber1(self, n, primes):
        #???nthUglyNumber??????
        super_ugly_numbers = []
        heap = [1]
        heapq.heapify(heap)
        indexes = {1: [[0, p] for p in primes]}
        while len(super_ugly_numbers) < n:
            super_ugly_numbers.append(heapq.heappop(heap))
            for tup in indexes[super_ugly_numbers[-1]]:
                new_ugly = super_ugly_numbers[tup[0]] * tup[1]    
                if new_ugly in indexes:
                    indexes[new_ugly].append([tup[0] + 1, tup[1]])
                else:
                    indexes[new_ugly] = [[tup[0] + 1, tup[1]]]
                    heapq.heappush(heap, new_ugly)
            del indexes[super_ugly_numbers[-1]]
        return super_ugly_numbers[-1]
# sol=Solution25()
# a=10
# print sol.uglyNumberII(a)


class Solution26(object):
    def maxSlidingWindow(self, nums, k):
        '''max slide window, a window of length k scans an array,
        return the max element in the window in each iteration
        ???????????????????????????list??????window?????????????????????
        '''
        if nums is None or len(nums) < k:
            return []
        d = deque()
        res = []
        for i in range(len(nums)):
            # ????????????????????????????????????
            if d and d[0] == i - k:
                d.popleft()
            # ?????????????????????
            while d and nums[d[-1]] < nums[i]:
                d.pop() 
            d.append(i)
            if i >= k-1:
                res.append(nums[d[0]])
        return res
# sol=Solution26()
# a=[1,3,-1,-3,5,3,6,7]
# b=3
# print sol.maxSlidingWindow(a,b)


def findnumberofTriangles(arr): 
    # given an array, find possible three values that can form into a triangle
    n = len(arr) 
    arr.sort() 
    count = 0
    for i in range(0, n-2): 
        for j in range(i+1, n-1): 
            k = j + 1
            while k < n and arr[i] + arr[j] > arr[k]: 
                k += 1
                count += 1
    return count 
# arr = [10, 21, 22, 100, 101, 200, 300] 
# print findnumberofTriangles(arr) 


class Solution27(object):
    def largestIncreaseSequence(self, nums):
        # ????????????????????????LIS????????????
        if nums is None:
            return 0
        if len(nums) <= 1:
            return len(nums)
        stack = list()
        stack.append(nums[0])
        max_length = 0
        for i in range(1, len(nums)):
            if stack and nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                idx = self.binarySearch(stack, nums[i])
                stack[idx] = nums[i]
            if len(stack) > max_length:
                max_length = len(stack)
        return max_length

    def binarySearch(self, nums, target):
        left, right = 0, len(nums)
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        if nums[left] >= target:
            return left
        return right

    def binarySearch1(self, nums, target):
        left, right = 0, len(nums)
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return -1
        if nums[left] > target: return left
        elif nums[left] == target: return -1
        else: return right
# sol=Solution27()
# a=[5,7,7,2,8,5,9,10]
# a=[5,5,5,5]
# print sol.largestIncreaseSequence(a)


class Solution28(object):
    def validBST(self, head):
        return self.helper(head)
    def helper(self, node):
        if not node:
            return True
        left = self.helper(node.left)
        right = self.helper(node.right)
        if node.left and node.left.val >= node.val:
            return False
        if node.right and node.right.val <= node.val:
            return False
        return left and right


# build balanced BST
class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution29(object):
    def rightViewOfBT(self, root):
        # ?????????????????????????????????????????????
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            queue_next = deque()
            res.append(queue[-1].val)
            while len(queue) > 0:
                node = queue.popleft()
                if node.left: queue_next.append(node.left)
                if node.right: queue_next.append(node.right)
            queue = queue_next

    def preOrderTraverse(self, node):
        # ???????????????
        stack = LifoQueue()
        res = []
        while node is not None or not stack.empty():
            while node is not None:
                res.append(node.val)
                stack.put(node)
                node = node.left
            if not stack.empty():
                node = stack.get()
                node = node.right
        return res

    def inOrderTraverse(self, node):
        # ???????????????
        stack = LifoQueue()
        res = []
        while node is not None or not stack.empty():
            while node is not None:
                stack.put(node)
                node = node.left
            if not stack.empty():
                node = stack.get()
                res.append(node.val)
                node = node.right
        return res

    def postOrderTraverse(self, node):
        # ???????????????
        stack = LifoQueue()
        lastVisit = node
        res = []
        while node is not None or not stack.empty():
            while node is not None:
                stack.put(node)
                node = node.left
            node = stack.get()
            stack.put(node)
            if node.right is None or node.right == lastVisit:
                res.append(node.val)
                lastVisit = node
                _ = stack.get()
                node = None
            else:
                node = node.right
        return res
# sol=Solution29()
# root = Node(7) # (3 (1, 5)) 7 (10, (8))
# root.left = Node(3)
# root.right = Node(10)
# root.left.left = Node(1)
# root.left.right = Node(5)
# root.right.left = Node(8)
# print sol.preOrderTraverse(root)
# print sol.inOrderTraverse(root)
# print sol.postOrderTraverse(root)


class Solution30(object):
    def findMidNumber(self, nums):
        # ?????????????????????????????????????????????????????????
        mid = len(nums)/2
        res = self.helper(nums, 0, len(nums)-1, mid)
        if len(nums)%2 == 0:
            return (nums[res-1]+nums[res])/2.
        else:
            return nums[res]

    def helper(self, nums, start, end, mid):
        i, j = start, end
        while i < j:
            while i < j and nums[i] <= nums[j]:
                j -= 1
            self.swap(nums, i, j)
            while i < j and nums[i] <= nums[j]:
                i += 1
            self.swap(nums, i, j)
        if mid < i:
            return self.helper(nums, start, i-1, mid)
        elif mid > i:
            return self.helper(nums, i+1, end, mid)
        else:
            return i

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
# sol=Solution30()
# a=[2,4,1,6,5,8,10] # 5
# print sol.findMidNumber(a)


from copy import copy
class Solution31(object):
    def subsetI(self, nums):
        # subset I
        # ????????????????????????????????????????????????????????????????????????????????????
        nums.sort()
        res = []
        self.helper1(nums, 0, [], res)
        return res

    def helper1(self, nums, start, combine, res):
        res.append(copy(combine))
        for i in range(start, len(nums)):
            combine.append(nums[i])
            self.helper1(nums, i+1, combine, res)
            combine.pop(-1)
# sol=Solution31()
# a=[1,2,3]
# print sol.subsetI(a)


class Solution32(object):
    def maxAreaOfIsland(self, grid):
        # ??????????????????
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(gid[0])
        maxArea = 0
        for i in range(m):
            for j in range(n):
                area = self.helper(grid, i, j)
                maxArea = max(maxArea, area)
        return maxArea

    def helper(self, grid, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and \
            grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.helper(grid, i+1, j) + self.helper(grid, i-1, j) + \
                self.helper(grid, i, j+1) + self.helper(grid, i, j-1)
        return 0


# ???????????????????????????
'''
?????????1. 0-1???????????????????????????????????????????????????????????????
     2. ?????????????????????
     3. ????????????
'''
# 0. ????????????????????????
# ?????????????????????x=(ax+c)%m, x???????????????seed????????????????????????
def randint(modulus=2**31, a=1103515245, c=12345, seed=42):
    while True:
        seed = (a*seed + c)%modulus
        yield seed
# r=randint()
# print next(r)%10
# print next(r)%10
# print next(r)%10
# 1. ????????????????????????f()?????????0????????????60%?????????1????????????40%????????????????????????
def f():
    num = random.random()
    return 0 if num < 0.6 else 1
# 2. ??????f()??????????????????????????????g()???????????????0???1???????????????0.5
def g():
    while True:
        a, b = f(), f()
        if (a, b) == (0, 1):
            return 1
        elif (a, b) == (1, 0):
            return 0
# 3. ?????????????????????
def bernoulli(p):
    num = random.random()
    return 1 if num < p else 0
# 4. ??????????????????????????????????????????????????????1,2,3??????????????????0.3,0.4,0.3
def withProbRandomPick(prob_list):
    # prob_list: [(1,0.3),(2,0.4),(3,0.3)]
    num = random.random()
    p_sum = 0
    for p in prob_list:
        p_sum += p[1]
        if num < p_sum:
            return p[0]
# 5. ??????rand5()???????????????0~4???????????????????????????rand7()
def rand5():
    p = random.random()
    return int(p*5)
def rand7():
    while True:
        x = 5*rand5()+rand5()
        if x < 21:
            return x%7


class solution33(object):
    def searchRotatedSortedArray(self, nums, target):
        # search in rotated sorted array I, no duplicates
        if nums is None or len(nums) == 0:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]: right = mid-1
                else: left = mid+1
            else:
                if nums[mid] < target <= nums[right]: left = mid+1
                else: right = mid-1
        return -1

    def searchRotatedSortedArrayII(self, nums, target):
        # search in rotated sorted array I, with duplicates
        if nums is None or len(nums) == 0:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]: right = mid-1
                else: left = mid+1
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]: left = mid+1
                else: right = mid-1
            else: left += 1
        return -1

    def findMinimum(self, nums):
        # find minimum in rotated sorted array I, no duplicates
        # ?????????????????????????????????????????????????????????
        if nums is None or len(nums) == 0:
            return -1
        left, right = 0, len(nums)-1
        while left+1 < right:
            mid = left + (right - left)/2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])
# sol=solution33()
# a=[5,6,7,1,2]
# b=4
# print sol.searchRotatedSortedArray(a, b)
# a=[1,1,1,3,1]
# b=3
# print sol.searchRotatedSortedArrayII(a, b)
# a=[5,6,7,8,2,3,4]
# print sol.findMinimum(a)


class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
    def __lt__(self, node):
        return self.value > node.value

class Solution34:
    def pathWithMaxMinValue(self, matrix):
        # path with maximum minimum value, leetcode 1102, ???????????????????????????????????????
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return -1, -1
        m, n = len(matrix), len(matrix[0])
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        heap = []
        heap.append(Node(matrix[0][0], 0, 0))
        path_min = matrix[0][0]
        matrix[0][0] = -1
        while len(heap) > 0:
            node = heapq.heappop(heap)
            if path_min > node.value:
                path_min = node.value
            if node.x == m-1 and node.y == n-1:
                break
            for d in directions:
                x_ = node.x + d[0]
                y_ = node.y + d[1]
                if x_ < 0 or y_ < 0 or x_ > m-1 or y_ > n-1 or matrix[x_][y_]==-1: continue
                heap.append(Node(matrix[x_][y_], x_, y_))
                matrix[x_][y_] = -1
                heapq.heapify(heap)
        return path_min

    def pathWithMaxScore(self, matrix):
        # path with maximum score, ???????????????????????????????????????????????????????????????
        # https://leetcode.com/discuss/interview-question/383669/
        m, n = len(matrix), len(matrix[0])
        state = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    state[i][j] = sys.maxint
                elif i == m-1 and j == n-1:
                    state[i][j] = max(state[i][j-1], state[i-1][j])
                elif i == 0 and j != 0:
                    state[i][j] = min(state[i][j-1], matrix[i][j])
                elif j == 0 and i != 0:
                    state[i][j] = min(state[i-1][j], matrix[i][j])
                else:
                    state[i][j] = max(min(state[i][j-1], matrix[i][j]), \
                        min(state[i-1][j], matrix[i][j]))
        return state[m-1][n-1]
sol=Solution34()
# a=[[5,4,5],[1,2,6],[7,4,6]]#4,26
# a=[[3,4,6,3,4],
#    [0,2,1,1,7],
#    [8,8,3,2,7],
#    [3,2,4,9,8],
#    [4,1,2,0,0],
#    [4,6,5,4,3]]#3,103
# print(sol.pathWithMaxMinValue(a))
# a=[[5, 1],
#    [4, 5]]#4
# a=[[1, 2, 3],
#    [4, 5, 1]]#4
# a=[[3,4,6,3,4],
#    [0,2,1,1,7],
#    [8,8,3,2,7],
#    [3,2,4,9,8],
#    [4,1,2,0,0],
#    [4,6,5,4,3]]#2
# print(sol.pathWithMaxScore(a))


class Solution35:
    def minimumCostConnectStick(self, array):
        # minimum cost to connect sticks
        if len(array) == 0: return 0
        if len(array) == 1: return array[0]
        heapq.heapify(array)
        cost = 0
        while len(array) > 1:
            top1 = heapq.heappop(array)
            top2 = heapq.heappop(array)
            cost += top1 + top2
            heapq.heappush(array, top1+top2)
        return cost
# sol=Solution35()
# a=[2,4,3]#14
# a=[1,8,3,5]#30
# print(sol.minimumCostConnectStick(a))


class Solution36:
    def subtreeOfAnotherTree(self, source, target):
        # subtree of another tree
        if source is None or target is None:
            return False
        if self.helper(source, target):
            return True
        return self.subtreeOfAnotherTree(source.left, target) \
            or self.subtreeOfAnotherTree(source.right,  target)

    def helper(self, source, target):
        if source is None and target is None:
            return True
        if source is None or target is None:
            return False
        if source.value != target.value:
            return False
        left = self.helper(source.left, target.left)
        right = self.helper(source.right, target.right)
        return left and right


class Solution37:
    def minimumStep(self, matrix):
        # ???????????????0??????1??????1??????????????????????????????0???cell??????1
        # ???????????????????????????1??????????????????
        # https://leetcode.com/discuss/interview-question/411357/
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        queue = Queue()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m, n = len(matrix), len(matrix[0])
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    queue.put([i,j])
                    visited[i][j] = 1
        res = 0
        while queue.qsize() > 0:
            for _ in range(queue.qsize()):
                i, j = queue.get()
                for d in directions:
                    i_, j_ = i+d[0], j+d[1]
                    if i_ < 0 or j_ < 0 or i_ > m-1 or j_ > n-1 or visited[i_][j_] == 1:
                        continue
                    queue.put([i_, j_])
                    visited[i_][j_] = 1
            # print('\n'.join([' '.join([str(r) for r in row]) for row in visited]))
            # print('\n')
            res += 1
        return res - 1
# sol=Solution37()
# a=[[0,1,1,0,1],
#    [0,1,0,1,0],
#    [0,0,0,0,1],
#    [0,1,0,0,0]]#2
# a=[[0,1,0,0,0],
#    [0,0,0,0,0],
#    [0,0,0,0,1],
#    [0,0,0,0,0]]#4
# print(sol.minimumStep(a))

class Node(object):
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt
    def __lt__(self, node):
        if self.cnt == node.cnt:
            return self.word < node.word
        else:
            return self.cnt > node.cnt

class Solution38:
    def topNCompatitor(self, topNComp, competitors, reviews):
        """
        :topNComp: int, top n competitors
        :competitors: list of competitors
        :reviews: list of reviews
        :rtype: int
        https://leetcode.com/discuss/interview-question/415729/
        """
        comp_to_cnt = dict()
        for comp in competitors:
            comp_to_cnt[comp] = 0
        s = set()
        for review in reviews:
            for word in review.split(' '):
                word = word.lower()
                if word not in s and word in comp_to_cnt:
                    comp_to_cnt[word] += 1
                    s.add(word)
            s = set()
        heap = []
        for word,cnt in comp_to_cnt.items():
            heapq.heappush(heap, Node(word, cnt))
        res = [node.word for node in heapq.nsmallest(topNComp, heap)]
        return res
# top_n_comps = 2
# comps = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
# reviews = ["newshop is providing good service in the city;everyone should try newshop",
#            "best services by newshop",
#            "fashionbeats has great services in the city",
#            "Im proud to have fashionbeats",
#            "mymarket has awesome service",
#            "thank Newshop for the quick delivery"]#["newshop", "fashionbeats"]
# print(Solution38().topNCompatitor(top_n_comps, comps, reviews))
# top_n_comps = 2
# comps = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
# reviews = ["newshop is providing good service in the city;everyone should try newshop",
#            "best services by newshop",
#            "fashionbeats has great services in the city",
#            "Im proud to have fashionbeats",
#            "afshion has awesome service",
#            "thank afshion for the quick delivery"]#['afshion', 'fashionbeats']
# print(Solution38().topNCompatitor(top_n_comps, comps, reviews))


class Solution39:
    def numberOfIslands(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        self.matrix = matrix
        self.m, self.n = len(self.matrix), len(self.matrix[0])
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j] == 1:
                    self.helper(i, j)
                    res += 1
        return res

    def helper(self, i, j):
        if i >= 0 and j >= 0 and i <= self.m-1 and j <= self.n-1 and self.matrix[i][j] == 1:
            self.matrix[i][j] = 0
            self.helper(i, j-1)
            self.helper(i, j+1)
            self.helper(i+1, j)
            self.helper(i-1, j+1) 
# sol=Solution39()
# a=[[1,1,1,1,0],
#    [1,1,0,1,0],
#    [0,0,0,0,0],
#    [1,0,1,0,0]]
# print(sol.numberOfIslands(a))


class Solution40:
    def favoriteSongs(self, userSongs, songGenres):
        #https://leetcode.com/discuss/interview-question/373006/Amazon-or-OA-2019-or-Favorite-Genres
        song_to_genre = dict()
        user_to_genres = dict()
        for genre, songs in songGenres.items():
            for song in songs:
                song_to_genre[song] = genre
        for user, songs in userSongs.items():
            genre_to_cnt = dict()
            max_cnt = 0
            genres = []
            for song in songs:
                genre = song_to_genre.get(song)
                if genre is None: continue
                genre_to_cnt[genre] = genre_to_cnt.get(genre, 0)+1
                if max_cnt < genre_to_cnt[genre]:
                    max_cnt = genre_to_cnt[genre]
                    genres = [genre]
                elif max_cnt == genre_to_cnt[genre]:
                    genres.append(genre)
            user_to_genres[user] = genres
        return user_to_genres
# sol=Solution40()
# userSongs = {  
#    "David": ["song1", "song2", "song3", "song4", "song8"],
#    "Emma":  ["song5", "song6", "song7"]}
# songGenres = {  
#    "Rock":    ["song1", "song3"],
#    "Dubstep": ["song7"],
#    "Techno":  ["song2", "song4"],
#    "Pop":     ["song5", "song6"],
#    "Jazz":    ["song8", "song9"]}#{"David": ["Rock","Techno"], "Emma": ["Pop"]}
# userSongs = {  
#    "David": ["song1", "song2"],
#    "Emma":  ["song3", "song4"]}
# songGenres = {}#{'Emma': [], 'David': []}
# print(sol.favoriteSongs(userSongs, songGenres))


class Solution41:
    def minAbsDiffBetweenTwoElements(self, array):
        #https://leetcode.com/discuss/interview-question/376980
        #n*logn*log(element)
        #n??????????????????log?????????????????????log(element)?????????2??????
        if array is None or len(array) < 2:
            return -1
        heap = []
        sorted_list = []
        diff = sys.maxint
        for i in array:
            if i%2 == 1:#??????
                heapq.heappush(heap, i*2)
            else:
                heapq.heappush(heap, i)
        while len(heap) > 0:
            i = heapq.heappop(heap)
            if i == 14: print(sorted_list)
            while True:
                idx = bisect.bisect_left(sorted_list, i)
                if idx < len(sorted_list):
                    diff = min(diff, sorted_list[idx]-i)
                    if diff == 0: return 0
                if idx > 0:
                    diff = min(diff, i-sorted_list[idx-1])
                bisect.insort_left(sorted_list, i)
                if i%2 == 1: break
                i /= 2
        return diff
# sol=Solution41()
# a=[1,2]#0
# a=[10, 3, 7, 4, 15]#1
# a=[43,17]#9
# print(sol.minAbsDiffBetweenTwoElements(a))


class Solution42:
    def __init__(self):
        self.n = None
        self.access_counter = 0  #?????????????????????????????????????????????????????????
        self.graph = dict()
        self.visited = []  #???????????????
        self.parent = []  #?????????
        self.discovery_times = []  #???i???????????????i????????????????????????????????????????????????
        self.lower = []  #?????????i????????????????????????????????????????????????????????????????????????
                         #?????????????????????????????????????????????????????????????????????????????????!!!
        self.result = []

    def criticalConnections(self, n, connections):
        #????????????????????????????????????????????????????????????????????????leetcode1192
        self.n = n
        self.visited = [False]*n
        self.parent = [-1]*n
        self.discovery_times = [0]*n
        self.lower = [0]*n
        for conn in connections:
            self.graph.setdefault(conn[0], []).append(conn[1])
            self.graph.setdefault(conn[1], []).append(conn[0])

        for i in range(n):
            if not self.visited[i]:
                self.helper(i)
        return self.result

    def criticalNodes(self, n, connections):
        #???????????????????????????????????????????????????????????????????????????
        #??????????????????????????????????????????????????????????????????????????????????????????
        #????????????????????????????????????????????????????????????
        #??????????????????????????????????????????
        self.n = n
        self.visited = [False]*n
        self.parent = [-1]*n
        self.discovery_times = [0]*n
        self.lower = [0]*n
        for conn in connections:
            self.graph.setdefault(conn[0], []).append(conn[1])
            self.graph.setdefault(conn[1], []).append(conn[0])

        for i in range(n):
            if not self.visited[i]:
                self.helper1(i)
        return self.result

    def helper(self, node):
        self.visited[node] = True
        self.access_counter += 1
        self.discovery_times[node] = self.access_counter
        self.lower[node] = self.access_counter
        for child in self.graph[node]:
            if not self.visited[child]:
                self.parent[child] = node
                self.helper(child)
                self.lower[node] = min(self.lower[node], self.lower[child])
                if self.lower[child] > self.discovery_times[node]:
                    self.result.append((min(node,child), max(node,child)))
            elif child != self.parent[node]:  #????????????????????????????????????
                self.lower[node] = min(self.lower[node], self.discovery_times[child])

    def helper1(self, node):
        child_num = 0
        self.visited[node] = True
        self.access_counter += 1
        self.discovery_times[node] = self.access_counter
        self.lower[node] = self.access_counter
        for child in self.graph[node]:
            if not self.visited[child]:
                child_num += 1
                self.parent[child] = node
                self.helper1(child)
                self.lower[node] = min(self.lower[node], self.lower[child])
                #????????????????????????????????????????????????????????????-1
                if self.parent[node] == -1 and child_num > 1:  
                    self.result.append(node)
                #???????????????????????????????????????????????????>=!!!
                if self.parent[node] != -1 and \
                    self.lower[child] > self.discovery_times[node]:
                        self.result.append(node)

            elif child != self.parent[node]:  #????????????????????????????????????
                self.lower[node] = min(self.lower[node], self.discovery_times[child])
# a=5
# b=[[0, 1], [0, 2], [2, 3], [0, 3], [3, 4]]
# a=7
# b=[[0,1],[0, 2],[1, 3],[2, 3],[2, 5],[5, 6],[3,4]]
# sol1=Solution42()
# print(sol1.criticalConnections(a,b))
# sol2=Solution42()
# print(sol2.criticalNodes(a,b))


class Node(object):
    #Trie tree??????
    def __init__(self):
        self.childs = dict()
        self.queue = []  # ???????????????
class Word(object):
    #????????????????????????
    def __init__(self,word):
        self.word = word
    def __lt__(self,other):
        return self.word > other.word

class Solution43:
    def productSuggestions(self, n, repository, query):
        #https://leetcode.com/discuss/interview-question/414085/
        #??????trie tree???????????????????????????
        #????????????????????????????????????????????????????????????????????????????????????????????????
        if n == 0 or len(repository) == 0 or len(query) <= 1:
            return None

        # build trie tree
        root = Node()
        for word in repository:
            current = root
            for c in word:
                if c not in current.childs:
                    current.childs[c] = Node()
                #??????????????????????????????3??????????????????????????????????????????????????????????????????????????????????????????
                heapq.heappush(current.childs[c].queue, Word(word))
                if len(current.childs[c].queue) > 3:
                    _ = heapq.heappop(current.childs[c].queue)
                #????????????
                current = current.childs[c]

        return self.search(root, query)

    def search(self, node, word):
        results = []
        for i,c in enumerate(word):
            res = []
            if c not in node.childs:
                return results[1:]
            queue = node.childs[c].queue[:]
            res = [j.word for j in heapq.nlargest(3, queue)]
            results.append(res)
            node = node.childs[c]
        return results[1:]
# sol=Solution43()
# a=5
# b=["mobile", "mouse", "moneypot", "monitor", "mousepad"]
# c="mouse"#[["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
# a=9
# b=["ps4", "ps4 slim", "ps4 pro", "xbox", "tissue",
#    "standing table", "house", "true love", "tracking device"]
# c="ps4"#[["ps4", "ps4 pro", "ps4 slim"], ["ps4", "ps4 pro", "ps4 slim"]]
# c="tru"#[["tracking device", "true love"], ["true love"]]
# print(sol.productSuggestions(a,b,c))


class Solution44:
    def  zombieInMatrix(self, matrix):
        # Zombie in Matrix
        # https://leetcode.com/discuss/interview-question/411357/
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m, n = len(matrix), len(matrix[0])
        res = 0
        queue = Queue()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    queue.put((i,j))
        while queue.qsize() > 0:
            qsize = queue.qsize()
            for _ in range(qsize):
                i, j = queue.get()
                for d in directions:
                    i_, j_ = i+d[0], j+d[1]
                    if i_>=0 and i_<m and j_>=0 and j_<n and matrix[i_][j_]==0:
                        matrix[i_][j_] = 1
                        queue.put((i_,j_))
            res += 1
        return res-1
# sol=Solution44()
# a=[[0, 1, 1, 0, 1],
#    [0, 1, 0, 1, 0],
#    [0, 0, 0, 0, 1],
#    [0, 1, 0, 0, 0]]#2
# a=[[0,1,0,0,0],
#    [0,0,0,0,0],
#    [0,0,0,0,1],
#    [0,0,0,0,0]]#4
# print(sol.zombieInMatrix(a))


class Solution45:
    def reorderLogFiles(self, logs):
        # def f(log):
        #     id_, rest = log.split(" ", 1)
        #     return (0, rest, id_) if rest[0].isalpha() else (1,)
        # return sorted(logs, key=f)
        def fn(log):
            iden, log = log.split(' ', 1)
            return (0, log, iden) if log[0].isalpha() else (1,)
        return sorted(logs, key=fn)
# sol=Solution45()
# a=["g1 abc","a8 ab d aoo"]
# # a=["g1 act","a8 act aoo"]
# print(sol.reorderLogFiles(a))


class Solution46:
    def prisonAfterNDays(self, n, cells):
        # leetcode957, prison cells after n days
        state_to_idx = dict()
        idx_to_state = dict()
        res = []
        cells = tuple(cells)
        while n > 0:
            if cells in state_to_idx:
                n_ = state_to_idx[cells]
                n = n_ - n%(n_-n)
                return idx_to_state[n]
            state_to_idx[cells] = n
            idx_to_state[n] = cells
            new_cells = [0]*8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    new_cells[i] = 1
            new_cells = tuple(new_cells)
            n -= 1
            cells = new_cells
        return cells
# sol=Solution46()
# a=7
# b=[0,1,0,1,1,0,0,1]#[0,0,1,1,0,0,0,0]
# a=1000000000
# b=[1,0,0,1,0,0,1,0]#[0,0,1,1,1,1,1,0]
# print(sol.prisonAfterNDays(a,b))


class Solution47:
    def partitionLabels(self, string):
        # leetcode763 partition labels
        if string is None or len(string) == 0:
            return []
        char_to_last = dict()
        for i,c in enumerate(string):
            char_to_last[c] = i 
        start, end = 0, 0
        res = []
        for i in range(len(string)):
            char = string[i]
            if char_to_last[char] > end:
                end = char_to_last[char]
            if i == end:
                res.append(end-start+1)
                start = i+1
        return res
# sol=Solution47()
# a='ababcbacadefegdehijhklij'#[9,7,8]
# # a='abcded'#[1,1,1,3]
# print(sol.partitionLabels(a))


from collections import Counter
def get_largest_X(A):
    #???????????????????????????????????????0??????2^63????????????????????????????????????????????????????????????????????????
    #?????????????????????????????????
    #?????????????????????????????????bit????????????????????????bit?????????['0','0','0','1','1']???
    #????????????'0'??????????????????????????????
    res = []
    for i in range(0, 63):
        bit_list = [x&1 for x in A]
        bit_counter = Counter(bit_list)
        bit = '1' if bit_counter.get(1,0) < bit_counter.get(0,0) else '0'
        res.append(bit)
        A = [x>>1 for x in A]
    res.reverse()
    return int(''.join(res), 2)
# a=[10,12,5,7,19]#9223372036854775800
# print(get_largest_X(a))


class Solution48:
    def pointOfLattice(self, ax, ay, bx, by):
        diff_x, diff_y = bx-ax, by-ay
        rotate_x, rotate_y = diff_y, -diff_x

        gcd_num = self.gcd(rotate_x, rotate_y)
        rotate_x /= abs(gcd_num)
        rotate_y /= abs(gcd_num)
        return '{},{}'.format(bx+rotate_x, by+rotate_y)

    def gcd(self, a, b):
        return a if b==0 else self.gcd(b, a%b)
# sol=Solution48()
# ax,ay=-1,3
# bx,by=3,1
# print(sol.pointOfLattice(ax,ay,bx,by))


class Solution49:
    def optimalUtilization(self, a, b, target):
        if len(a) == 0 or len(b) == 0:
            return []
        a.sort(key=lambda x:x[1])
        b.sort(key=lambda x:x[1])
        left, right = 0, len(b)-1
        res = []
        cur_diff = float('inf')
        while left < len(a) and right >= 0:
            i, val1 = a[left]
            j, val2 = b[right]
            if target-val1-val2 == cur_diff:
                res.append((i, j))
            elif val1+val2 <= target and target-val1-val2 < cur_diff:
                res = []
                res.append((i, j))
                cur_diff = target-val1-val2
            if target > val1+val2:
                left += 1
            else:
                right -= 1
        return res
# sol=Solution49()
# a = [[1, 2], [2, 4], [3, 6]]
# b = [[1, 2]]
# target = 7#[[2,1]]
# a = [[1, 3], [2, 5], [3, 7], [4, 10]]
# b = [[1, 2], [2, 3], [3, 4], [4, 5]]
# target = 10#[[2, 4], [3, 2]]
# print(sol.optimalUtilization(a,b,target))

class Node(object):
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step

class Solution50:
    def treasureIsland(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return -1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(matrix), len(matrix[0])
        queue = Queue()
        queue.put(Node(0, 0, 0))
        while not queue.empty():
            node = queue.get()
            for d in directions:
                x_, y_, step_ = node.x+d[0], node.y+d[1], node.step+1
                if x_ > m-1 or x_ < 0 or y_ > n-1 or y_ < 0: continue
                if matrix[x_][y_] == 'X':
                    return step_
                elif matrix[x_][y_] == 'O':
                    queue.put(Node(x_, y_, step_))
                    matrix[x_][y_] = 'D'
        return -1
# sol=Solution50()
# matrix= [['O', 'O', 'O', 'O'],
#         ['D', 'O', 'D', 'O'],
#         ['O', 'O', 'O', 'O'],
#         ['X', 'D', 'D', 'O']]
# matrix=[['O', 'O', 'O', 'X'],
#         ['O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O']]
# print(sol.treasureIsland(matrix))



from collections import defaultdict
class Node(object):
    def __init__(self, num, cost):
        self.num = num
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost

class Solution51:
    def minCostForRepair(self, n, edges, edgesToRepair):
        graph = {}
        edge_set = set()
        for edge in edgesToRepair:
            graph.setdefault(edge[0], []).append((edge[1], edge[2]))
            graph.setdefault(edge[1], []).append((edge[0], edge[2]))
            edge_set.add((edge[0], edge[1]))
            edge_set.add((edge[1], edge[0]))
        for edge in edges:
            if tuple(edge) not in edge_set:
                graph.setdefault(edge[0], []).append((edge[1], 0))
                graph.setdefault(edge[1], []).append((edge[0], 0))
        res = 0
        queue = [Node(1, 0)]
        heapq.heapify(queue)
        visited = set()
        while queue:
            node = heapq.heappop(queue)
            if node.num not in visited:
                visited.add(node.num)
                res += node.cost
                for num, cost in graph[node.num]:
                    if num not in visited:
                        heapq.heappush(queue, Node(num, cost))
        return res
# sol=Solution51()
# n = 5
# edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
# edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]#20
# n = 6
# edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]]
# edgesToRepair = [[1, 6, 410], [2, 4, 800]]#410
# print(sol.minCostForRepair(n, edges, edgesToRepair))


class Solution52:
    def changeDirectory(self, absolute_path, relative_path):
        # ??????????????????????????????????????????????????????????????????`cd ????????????`????????????????????????
        queue = ['']
        for path in absolute_path.split('/'):
            if path != '':
                queue.append(path)
        for path in relative_path.split('/'):
            if path == '': continue
            if path == '..':
                if len(queue) > 1: queue.pop()
            else:
                queue.append(path)
        if len(queue) == 1: return '/'
        return '/'.join(queue)
# sol=Solution52()
# a='/bin/etc/abc'
# b='../xyz/tuv/..' #'/bin/etc/xyz'
# a='/bin/etc/abc'
# b='../../../../../' #'/'
# print(sol.changeDirectory(a,b))

def printBinaryTree(root):
    res = []
    queue = Queue()
    queue.put(root)
    while queue.qsize() > 0:
        num = queue.qsize()
        tmp = []
        flag = False
        for _ in range(num):
            node = queue.get()
            if node is None:
                tmp.append('')
                queue.put(None)
                queue.put(None)
            else:
                flag = True
                tmp.append(node.val)
                queue.put(node.left)
                queue.put(node.right)
        if flag:
            res.append(tmp)
        else:
            break
    for i in res:
        print(i)


class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.random = None
class Solution53:
    def copyBinaryTreeWithRandomPointer(self, root):
        # ????????????????????????????????????
        # ?????????????????????????????????????????????????????????????????????????????????????????????????????????
        if root is None:
            return None
        # ????????????
        self.addNode(root)
        # ??????????????????
        self.assignRandom(root)
        # ?????????????????????
        new, old = self.splitTree(root)
        return new

    def addNode(self, node):
        if node and node.right: 
            self.addNode(node.right)
        if node:
            new = Node(node.val)
            new.left = node.left
            node.left = new
            self.addNode(node.left.left)

    def assignRandom(self, node):
        if node and node.right:
            self.assignRandom(node.right)
        if node:
            if node.random:
                node.left.random = node.random.left
            self.assignRandom(node.left.left)

    def splitTree(self, node):
        if node is None:
            return None, None
        old = node
        new = node.left
        old.left = None
        if new.left is None and old.right is None:
            return new, old
        if new.left:
            new.left, old.left = self.splitTree(new.left)
        if old.right:
            new.right, old.right = self.splitTree(old.right)
        return new, old
# root = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# root.left = node2
# root.right = node3
# root.random = node5
# node2.left = node4
# node2.right = node5
# node2.random = node3
# node4.random = node3
# #    1
# #  2   3
# # 4 5
# sol=Solution53()
# node=sol.copyBinaryTreeWithRandomPointer(root)
# printBinaryTree(node)



class Solution54:
    def searchTwoSumInMatrix(self, matrix, target):
        # ??????????????????2sum????????????????????????????????????????????????????????????
        # ?????????????????????(0,0)??????????????????????????????, ??????????????????
        # ?????????????????????(0,n-1), ???????????????????????????????????????????????????????????????
        # ???????????????????????????????????????????????????
        self.matrix = matrix
        self.res = []
        self.visited = set()
        self.m, self.n = len(matrix), len(matrix[0])
        self.helper(0, 0, 0, self.n-1, target)
        return self.res

    def helper(self, x1, y1, x2, y2, target):
        # ????????????
        if x1 < 0 or x1 > self.m-1 or y1 < 0 or y1 > self.n-1 or \
            x2 < 0 or x2 > self.m-1 or y2 < 0 or y2 > self.n-1:
                return None
        # ????????????ssssss
        if (x1 == x2 and y1 == y2) or (y1 > y2): 
            return None
        # visited??????
        if (x1, y1, x2, y2) in self.visited or (x2, y2, x1, y1) in self.visited:
            return None
        self.visited.add((x1, y1, x2, y2))
        if self.matrix[x1][y1]+self.matrix[x2][y2] == target:
            self.res.append([self.matrix[x1][y1], self.matrix[x2][y2]])          
            self.helper(x1+1, y1, x2, y2-1, target)
            self.helper(x1, y1+1, x2, y2-1, target)
        elif self.matrix[x1][y1]+self.matrix[x2][y2] > target:
            self.helper(x1, y1, x2, y2-1, target)
        else:
            self.helper(x1, y1, x2+1, y2, target)
            self.helper(x1+1, y1, x2, y2, target)
            self.helper(x1, y1+1, x2, y2, target)
# a =[[1, 4, 7, 11,15],
#     [2, 5, 8, 12,19],
#     [3, 6, 9, 16,22],
#     [10,13,14,17,24],
#     [18,21,23,26,30]]
# b=9 #[[1,8],[2,7],[3,6],[4,5]],
# b=15 #[[1, 14], [2, 13], [6, 9], [3, 12], [10, 5], [7, 8], [4, 11]]
# sol=Solution54()
# print(sol.searchTwoSumInMatrix(a,b))


class Solution55:
    # ?????????????????????????????????295???
    # 1. ????????????????????????????????????????????????2
    # 2. ?????????????????????????????????????????????
    # ??????1????????????k?????????k???????????????????????????????????????????????????
    # ??????2?????????????????????????????????????????????????????????lru?????????????????????????????????+hashmap
    # ??????3??????????????????????????????k???????????????????????????????????????2
    # ??????4?????????????????????????????????k????????????????????????+hashmap???????????????????????????
    # ??????5?????????????????????????????????k??????????????????????????????????????? !!!
    #       https://stackoverflow.com/questions/21692624/design-a-system-to-keep-top-k-frequent-words-real-time
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        if len(self.min_heap) == 0:
            self.min_heap.append(num)
            return None
        if len(self.min_heap) == len(self.max_heap):
            if num >= self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                num = -heapq.heappushpop(self.max_heap, -num)
                heapq.heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                num = heapq.heappushpop(self.min_heap, num)
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.max_heap, -num)

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0]-self.max_heap[0])/2
        return self.min_heap[0]
# sol=Solution55()
# sol.addNum(6)
# print(sol.findMedian()) #6
# sol.addNum(10)
# print(sol.findMedian()) #8
# sol.addNum(2)
# print(sol.findMedian()) #6
# sol.addNum(6)
# print(sol.findMedian()) #6
# sol.addNum(5)
# print(sol.findMedian()) #6
# sol.addNum(0)
# print(sol.findMedian()) #5.5


class Solution56:
    def __init__(self, equations, values):
        self.graph = dict()
        self.visited = set()
        for e,v in zip(equations,values):
            self.graph.setdefault(e[0], []).append([e[1], v])
            self.graph.setdefault(e[1], []).append([e[0], 1/v])

    def evaluateDivision(self, queries):
        res = []
        for query in queries:
            self.visited.clear()
            ans = self.search(query)
            res.append(ans)
        return res

    def search(self, query):
        if query[0] not in self.graph or query[1] not in self.graph:
            return -1
        if query[0] == query[1]:
            return 1
        queue = Queue()
        queue.put([query[0], 1])
        while queue.qsize() > 0:
            node = queue.get()
            self.visited.add(node[0])
            for next_node in self.graph[node[0]]:
                if next_node[0] in self.visited: continue
                if next_node[0] == query[1]:
                    return node[1]*next_node[1]
                queue.put([next_node[0], node[1]*next_node[1]])
        return -1
# equations = [["a", "b"], ["b", "c"]]
# values = [2.0, 3.0]
# sol=Solution56(equations, values)
# queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
# print(sol.evaluateDivision(queries))


class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
class Solution57:
    def secondLargestElementInBST(self, node):
        # BST??????????????????
        if node is None or (node.left is None and node.right is None):
            return -1
        second, largest = float('-inf'), node.val
        tmp = node
        while tmp.right:
            second = tmp.val
            largest = tmp.right.val
            tmp = tmp.right
        if node.left:
            second = node.left.val
            tmp = node.left
            while tmp.right:
                second = tmp.right.val
                tmp = tmp.right
        return second

    def medianInBST(self, root):
        # bst??????????????????????????????k?????????
        # ????????????????????????bst?????????????????????????????????????????????
        # node = None
        node = self.BST2DLL(root, None)
        return self.findMedian(node)

    def BST2DLL(self, root, last):
        if root is None:
            return None
        if root.left:
            last = self.BST2DLL(root.left, last)
        root.left = last
        if last is not None:
            last.right = root
        last = root
        if root.right is not None:
            last = self.BST2DLL(root.right, last)
        return last

    def findMedian(self, root):
        fast = root
        slow = root
        while fast.left is not None and fast.left.left is not None:
            fast = fast.left.left
            slow = slow.left
        if fast.left is not None:
            return (slow.val+slow.left.val)/2
        else:
            return slow.val
# sol=Solution57()
# root = Node(4)
# node2 = Node(2)
# node3 = Node(5)
# node4 = Node(1)
# node5 = Node(3)
# root.left = node2
# root.right = node3
# node2.left = node4
# node2.right = node5
# node5.right = Node(6)#4.5
# print(sol.medianInBST(root))


class Solution58(object):
    def numDistinct(self, s, t):
        self.visited = {}
        return self.helper(s, t, 0, 0)

    def helper(self, s, t, s_ptr, t_ptr):
        if t_ptr == len(t): return 1
        if s_ptr >= len(s): return 0
        if (s_ptr, t_ptr) not in self.visited:
            c = 0
            for i in range(s_ptr, len(s)):
                if s[i] == t[t_ptr]:
                    c += self.helper(s, t, i + 1, t_ptr + 1)
            self.visited[(s_ptr, t_ptr)] = c
        return self.visited[(s_ptr, t_ptr)]
# sol=Solution58()
# a='rabbbit'
# b='rabbit'#3
# # a='babgbag'
# # b='bag'#5
# a="aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
# b="bddabdcae"#10582116
# print(sol.numDistinct(a,b))


class maxFrequencyStack:
    def __init__(self):
        self.element_to_cnt = dict()
        self.cnt_to_elements = dict()
        self.max_cnt = float('-inf')

    def push(self, element):
        cnt = self.element_to_cnt.get(element, 0) + 1
        if cnt > self.max_cnt:
            self.max_cnt = cnt
        self.element_to_cnt[element] = cnt
        self.cnt_to_elements.setdefault(cnt, []).append(element)

    def pop(self):
        if self.max_cnt == 0:
            return None
        element = self.cnt_to_elements[self.max_cnt].pop()
        if len(self.cnt_to_elements[self.max_cnt]) == 0:
            self.max_cnt -= 1
        self.element_to_cnt[element] = self.element_to_cnt.get(element, 0) - 1
        return element
# stack=maxFrequencyStack()
# for i in [5,7,5,7,4,5]:
#     stack.push(i)
# for i in range(6):
#     print(stack.pop())



class Solution59:
    def quickSort(self, array):
        left, right = 0, len(array)-1
        self.helper1(array, left, right)
        return array

    def helper1(self, array, left, right):
        if left < right:
            mid = self.partition(array, left, right)
            self.helper1(array, left, mid)
            self.helper1(array, mid+1, right)

    def partition(self, array, left, right):
        while left < right:
            while left < right and array[right] >= array[left]:
                right -= 1
            if left < right:
                self.swap(array, left, right)
            while left < right and array[left] <= array[right]:
                left += 1
            if left < right:
                self.swap(array, left, right)
        return left

    def swap(self, array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp


    def mergeSort(self, array):
        m, n = 0, len(array)-1
        self.helper2(array, m, n)
        return array

    def helper2(self, array, left, right):
        if left < right:
            mid = left + (right-left)//2
            self.helper2(array, left, mid)
            self.helper2(array, mid+1, right)
            self.merge(array, left, mid, right)

    def merge(self, array, left, mid, right):
        arr = [0]*(right-left+1)
        i, j = mid, right
        while i >= left or j >= mid+1:
            if i >= left and j >= mid+1:
                if array[i] > array[j]:
                    arr[i+j-left-mid] = array[i]
                    i -= 1
                else:
                    arr[i+j-left-mid] = array[j]
                    j -= 1
            elif i >= left:
                arr[i+j-left-mid] = array[i]
                i -= 1
            elif j >= mid+1:
                arr[i+j-left-mid] = array[j]
                j -= 1
        array[left:right+1] = arr
# sol=Solution59()
# a=[3,4,1,4,6,2]
# print(sol.quickSort(a))
# print(sol.mergeSort(a))


class Solution60:
    def bfs(self, root):
        if root is None:
            return []
        queue = Queue()
        queue.put(root)
        res = []
        while queue.qsize() > 0:
            num = queue.qsize()
            node = queue.get()
            res.append(node.val)
            for _ in range(num):
                if node.left: queue.put(node.left)
                if node.right: queue.put(node.right)
        return res

    def zigzagBfs(self, root):
        if root is None:
            return []
        queue = Queue()
        queue.put(root)
        queue.put(None)
        flag = 1
        res = []
        tmp = []
        while queue.qsize() > 0:
            num = queue.qsize()
            node = queue.get()
            if node is not None:
                tmp.append(node.val)
                for _ in range(num):
                    if node.left: queue.put(node.left)
                    if node.right: queue.put(node.right)
            else:
                queue.put(None)
                if flag == 0:
                    res.append(tmp[::-1])
                else:
                    res.append(tmp)
                tmp = []
                flag = 1-flag
        return res

    def preDfs(self, root):
        pass

    def midDfs(self, root):
        pass

    def postDfs(self, root):
        pass


class Solution61:
    def wordSearchI(self, board, word):
        self.board = board
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.m, self.n = len(board), len(board[0])
        self.visited = [[0]*self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    res = self.helper1(word, i, j, 0)
                    if res: return True
        return False

    def helper1(self, word, i, j, k):
        if k == len(word)-1: return True
        self.visited[i][j] = 1
        for d in self.directions:
            i_, j_ = i+d[0], j+d[1]
            if i_ < 0 or j_ < 0 or i_ > self.m-1 or j_ > self.n-1 \
                or self.visited[i_][j_] == 1:
                    continue
            if self.board[i_][j_] == word[k+1]:
                res = self.helper1(word, i_, j_, k+1)
                if res: return True
        self.visited[i][j] = 0
        return False
# sol=Solution61()
# a=[['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']]
# b='ABCCED'#True
# b='SEE'#True
# b='ABCB'#False
# print(sol.wordSearchI(a, b))


class Solution62(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        neighbors = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        for preq in prerequisites:
            neighbors[preq[1]].append(preq[0])
            indeg[preq[0]] += 1
        queue = []
        for i in range(numCourses):
            if indeg[i]==0:
                queue.append(i)
        n = 0
        while queue:
            tmp = []
            for q in queue:
                n += 1
                for nei in neighbors[q]:
                    indeg[nei] -= 1
                    if indeg[nei]==0:
                        tmp.append(nei)
            queue = tmp
        return n==numCourses
# sol=Solution62()
# a,b=3,[[0, 2],[1,0],[0,1]]
# a,b=3,[[0, 2],[1,0],[1,2]]
# print(sol.canFinish(a,b))


class TokenBucket:
    def __init__(self, rate, capacity):
        '''
        rate: num of requests per seconds
        capacity: num of tokens
        '''
        self._rate = rate
        self._capacity = capacity
        self._current_size = capacity
        self._last_timestamp = int(time.time())

    def consume(self, num):
        _ = self.get_tokens()
        if num <= self._current_size:
            self._current_size -= num
            return True
        return False

    def get_tokens(self):
        if self._current_size < self._capacity:
            delta = (int(time.time()) - self._last_timestamp)*self._rate
            self._current_size = min(self._capacity, self._current_size+delta)
            self._last_timestamp = int(time.time())
        return self._current_size



# Design elevator
'''
use cases:
1. user press floor button to get floor
2. user press lift button to target floor
3. lift move up and down, open and close door
4. lift show current floor and direction
* Direction: UP, DOWN, NONE
* Elevator: 
    - size, maxWeight
    - currentWeight(), isFull(), currentDirection(), currentFloor()
    - moveUp(), moveDown(), openDoor(), closeDoor()
* ElevatorClient:
    - numFloor,
    - requestMove(), requestOpenDoor(), requestCloseDoor() 
* Floor:
    - num, upButton, downButton, LiftDirection, liftFloor
* FloorClient:
    - requestMove(), requestLiftInfo(), setLiftDirection(), setLiftFloor()
* Manager:
    - numFloor, floors, numElevator, elevators
    - maxFloor, minFloor
    - upDirections, downDirections
    - callMove(), callDoor()
'''












'''
2???????????????
OA:
substring of size K with K-1 distinct characters.
K distinct substring: done
    input: s = ???pqpqs??? num = 2
    output: 7
    [???pq???, ???pqp???, ???pqpq???, ???qp???, ???qpq???, ???pq???, ???qs???] // ????????????????????????substring
k closest done
search 2d matrix done
    ?????????????????????????????????????????????????????????????????????????????????????????????????????????-30???????????????
    ?????????????????? O(n*n) ????????????????????????????????? Failed Test Cases??? ??????????????????
Maximum Minimum Path, done
    ??????????????????DP??????????????????????????????????????????
973, done
reverse string???follow up???in place???done
442. Find All Duplicates in an Array 52, done
???maze???????????????????????????????????????BFS???done
Substring with k dist????????????list
maximum sum path ??????, done
High Five done
K character string
max average tree???done
two sum done????????????????????????
??????close two sum, input ( int capacity, List foregroundApp, List backgroundApp). 
    capacity???maximum device ????????? List????????????Integer???????????????ID??? ????????????????????????????????????
    ???????????????List???????????????,????????????value??????capacity???????????????????????????capacity?????????pair.
?????????????????? input string ??????????????? K ???substring????????????substring??? K - 1 ??? distinct 
    ???letter????????????????????? substring ???????????? List???????????????????????????????????????16???test case???
    ?????????????????????tree???tree?????????node?????????child?????????????????????????????????????????????subtree?????????node???
    average???total sum / total count????????????leaf node ??????substree?????????????????????????????????????????????????????????
    ???3.jpeg
????????????K distinct subtree ??????pqpqs k=2??????
    7pq,pqp,pqpq,pq,pqq,pq,qs??????????????????testcase?????????????????????12??????????????????????????????????????????
    ????????????????????????testcase?????????????????????????????????????????????????????????????????????????????????????????????????????????
    ??????????????????????????????????????????????????????????????????????????????????????????????????????countstr??????????????????set???
    ????????????????????????count++???????????????????????????????????????????????????????????????????????????????????????QUQ!
    ?????????highfive ??????????????????????????????????????????
261. Graph Valid Tree
iterate nested list???done
tic tac toe ??????

LP:
?????? behavior questions ??????????????????????????????
https://www.amazon.jobs/en/principles
https://kraftshala.com/how-to-raise-the-bar-in-the-amazon-interview/
https://www.thebalancecareers.com/top-behavioral-interview-questions-2059618
https://www.1point3acres.com/bbs/thread-307462-1-1.html
https://wdxtub.com/interview/14520850399861.html
https://www.1point3acres.com/bbs/forum.php?mod=collection&action=view&ctid=228603
S - Situation - Describe the situation
T - Task - Describe the goal you are working toward, or the challenge that needs to be done
A - Elaborate the steps you took to address the situation/challenge
R - Describe the outcome of your actions or your learnings 
????????????????????????????????????????????????????????????????????????????????????????????????(earn trust)
??????????????????????????????????????????(invent and simplify)
????????? exceed expectations ?????????(high standard)
????????????????????????????????????????????????????????????????????????????????????????????????????????????(deliver results)
??????????????????????????????????????????????????????????????????
   ???it depends on what type of conflict is, deadline, priority(earn trust)
?????????????????????????????????????????????(deliver results)
???????????????????????????????????????????????????(deliver results)
???????????????????????????????????????(deliver results)
?????????????????????????????????(learn and be curious)
?????????????????????????????????????????????????????????(earn trust)
???????????????(deliver results)
??????customer??????????????????customer???feedback????????????????????????(customer)
??????????????????????????????????????????????????????(are right, a lot)
?????????????????????????????????(costomer)
????????????????????????????????????Feedback(costomer)
?????????????????????????????????????????????????????????????????????????????????(costomer)

System desgin:
????????????????????????????????????Cache
design a real time voting system. ?????????????????????msg??????????????????????????????????????????????????????
    ???failure ???????????????????????????????????????
design LRU
???????????????????????????
OOD???????????????????????????52???????????????????????????????????????????????????????????????????????????????????????
???????????????????????????????????????????????????scale????????????db??????
OOD???????????????????????????????????????Cache



10???????????????
OA???
Question 1: 2D matrix question: multiple starting points, multiple end points. 
Find the shortest distance from any starting point to any end point. (some blocks were 
not accessible.)
Question 2: 2 sum modification, but had a long story behind it.
More: Explain the approach. (15 minutes given for this)
    Some work styled survey. (All MCQs.)
https://leetcode.com/problems/minimum-cost-to-connect-sticks/
Given a 2D matrix, start point and end point, find the shortest path from 
    start to end point. 1 signifies obstacles and 0 signifies cell can be 
    travelled through. (BFS preferably, can also be solved through DFS)
Given a 2D array, find the maximum out of the minimum of every possible path. Don???t 
    include the first or final entry. You can only move down or right.
    Example:
    [[1,2,3]
    [4,5,1]]
    1-> 2 -> 3 -> 1
    1-> 2 -> 5 -> 1
    1-> 4 -> 5 -> 1
    So min of all the paths = [2, 2, 4]
    Return the max of that, so 4 
Given number of points, number of links, and list of links, return list 
    articulation points. Amazon call points ???Routers??? in questions.
Searching in a 2D matrix
Critical connections
??????????????????????????????
Path With Maximum Score??
https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/
LC142
sum two pointers, time O(m+n), m is num of rows, n in num of cols???sorted matrix: 
    each row and column sorted???lc240
copy pointer with random
2 sum unique pair

???????????????
https://www.amazon.jobs/en/principles 
https://1o24bbs.com/t/topic/7041
https://1o24bbs.com/t/topic/6669
https://medium.com/@scarletinked/are-you-the-leader-were-looking-for-interviewing-at-amazon-8301d787815d.
https://1o24bbs.com/t/topic/17495 ????????????
https://interviewgenie.com/blog-1/category/Amazon+interviews ????????????

LP: Make at least 2 stories for each LP values
Time when you didn???t meet a deadline
Time when you needed help from somebody !!!
Tell me about yourself !!!
Ever worked on tight deadline(deliver result)
took help from senior(learn and be curious)
tell me about a time when you got struck on something and did you deliver on time
Tell me about a situation where you had a conflict with someone on your team. 
    What was it about? What did you do? What was the outcome(earn trust)
Give an example of when you saw a peer struggling and decided to step in and help.
    What was the situation and what actions did you take(hire and develop the best)
Tell me about a time you committed a mistake(earn trust)
Tell me about a time when your earned your teammate???s trust(earn trust)
Tell me about a time when your teammate didn???t agree with you(are right, a lot)
Tell me about a time when you invented something(invent and simplify)
Tell me about a time when you took important decision without any data(bias for action)
Tell me about a time when you helped one of your teammate(hire and develop the best)
?????????????????????????????????????????????????????????(deliver results)
???????????????????????????????????????????????????(earn trush)
?????????????????????????????????????????????(deliver results)
????????????????????????????????????????????????????????????????????? !!!(think big)
????????????????????????????????????????????????????????????????????????????????? !!!(are right, a lot)
????????????????????????????????????????????????????????????(costomer)
???????????????????????????????????????????????????(invent and simplify)
Have you ever gone out of your way to help a peer? (ownership)
Have you ever had to make a tough decision without consulting anybody?(bias for action)
tell about handling a tight deadline, second is setbacks on projects
a time when you faced a setback initially but still achieved the goal(deliver results)
Tell me about a time when you did something out of your comfort zone !!!
??????????????????????????????????????????(?????????ownership, costomer or frugality)
Describe a difficult time on your current role !!!



onsite:
All numbers appear 3 times except 1, get that number. Extend it to 
    all numbers appearing k times except 1 todo ?????????k???????????????k????????????k??????????????????????????????0
    https://blog.csdn.net/qq_34342154/article/details/77888442
https://leetcode.com/problems/maximum-frequency-stack/ done
https://leetcode.com/problems/cheapest-flights-within-k-stops/
    Dijkstra
Basic Calculator II done
House Robber II. done
Minimum Spanning Tree Question done
https://leetcode.com/problems/convert-bst-to-greater-tree/ !!! done
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/ !!! done
https://leetcode.com/problems/valid-sudoku/ !!! done ??????hashmap???????????????????????????????????????
https://leetcode.com/problems/remove-k-digits/ !!! done
https://leetcode.com/problems/word-break-ii/ !!! done
https://leetcode.com/problems/last-stone-weight/ !!! done
    How would you do it in linear time?
https://leetcode.com/problems/insert-delete-getrandom-o1/ !!! done 
https://leetcode.com/problems/decode-string/ !!! done
https://leetcode.com/problems/time-based-key-value-store/  done
    ?????????essentially using a tree based map !!!
Given start date and end date, return number of months and days in between
    Example: 10/01/2019 - 11/02/2020. Output: 13 months, 2 days !!!
Given a list of co-ordinates, return the center of the circle such that 
    maximum points from the list lie on the circumference of the circle
    Interviewer helped to recall the property that only 1 circle can pass through 
    any set of 3 points
    Further simplified by providing an already available method which returns 
    center of the circle when 3 points are passed as input.
    Could come up with O(n^3) answer which he agreed was the best we could do !!! done
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
https://leetcode.com/problems/super-ugly-number/ !!! done, ????????????????????????
https://leetcode.com/problems/merge-k-sorted-lists/ done
https://leetcode.com/problems/trapping-rain-water/ done ???????????????????????????
Median of BST done
3Sum
Two sum and k nearest point using Euclidean Distance done
Binary level order traversal , Zig Zag traversal done
Tested sorting knowledge on particular given inputs, (counting and merge sort)
Word Search
https://leetcode.com/problems/distinct-subsequences/ !!! done
reversing a linked list done
finding the next largest element in a BST !!! done
https://leetcode.com/problems/two-city-scheduling/ !!! done
https://leetcode.com/problems/reorder-data-in-log-files/ !!! done
https://leetcode.com/problems/employee-importance/ !!! done
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ !!!
    Time - O(n) , Memory O(1) done
https://leetcode.com/problems/search-a-2d-matrix-ii/ done
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
????????????????????????n???????????????????????? done
??????????????? ?????? done
Leetcode ???????????? 1240???
    ??????????????????????????????MIN????????????????????????overlap?????????????????????
??????Rearrange Array????????????Ele??????????????? ??????
TreeMap: ???????????????????????????????????????????????????O(logn) done
https://leetcode.com/problems/product-of-array-except-self/ !!! done??????????????????????????????
https://leetcode.com/problems/contains-duplicate/ !!! done
https://leetcode.com/problems/validate-binary-search-tree/ !!! done
implementing fizz-buzz done
Trapping Rain water
    what if now water is not coming from sky , instead we choose an 
    index to pour x unit of water , what is the amount of water we can trap now
    eg. [2,0,0,4,0,1] , if we pour 4 unit at index 2 , 
    max it can trap 4 unit of water done?????????????????????
https://leetcode.com/problems/valid-parentheses/ done
https://leetcode.com/problems/reverse-words-in-a-string/ done
Given streaming data, find the median in the K Largest Top Elements
    eg. K =. 3
    [. 1] ->. 1
    [1,2] -> for 1.5
    [l, 2,3] -> 2
    [1,2,3,1] -> 2
    [1,2,3,1,10] -> 3 #treemap(??????data???????????????????????????)+linkedlist(??????data?????????)
??????LC240. Search a 2D Matrix II, all row and col direction are sorted, 
    find all two sum pairs in matrix such that two sum equal to target.
    [[1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]]
    given target=9, return [[1,8],[2,7],[3,6],[4,5]],
    order does not matter, [3,6] are same as [6,3],do not include duplicate pair.
    my idea is use hashmap, which cost O(mn) time.
    follow-up: can you do better than O(mn) done
graph problem, -1 is obstacle,1 is tree need to cut, 0 is empty place 
    you can walk through, after cut, tree can be walk through, you can start at 
    any point and you can cut in any order, return minimum distance you have 
    to walk to cut all the tree, if you cannot do that, return -1.
    eg:
    [[1,1,1],
    [-1,-1,1],
    [1,1,1]]
    return 6
    [[-1,1,-1],
    [1,1,1],
    [-1,1,-1]]
    return 6 

copy a binary tree with random pointers, node 2 has a random pointer 
    to node 3 , and we will retain such structure in our copied result
      1           1
    2   3       2 -> 3
    O(1) done
Write a method which accepts a linked list of words and a 2-d array 
    of characters and returns a linked list of the words found in the 
    array with their (x,y) co-ordinated and direction.
    When further asked, the word can be searched in 8 directions 
    (right,left,top,down,top right,top left,bottom right bottom left).
Given P papers of varying lengths, each of which take a proportionate 
    time to process and given k graders.
    Distribute papers among the graders to minimize total time to grade all papers.
    It is similar with divide chocolate minimize maximum, but in this case, 
    can be any order.
    eg: papers=[10,13,12,18,10],k=2
    result is 32 =>min_sum([10,10,12] , [13,18])
    but not 35=>min_sum([10,13,12],[18,10])??????????????????????????????????????????
Given 2nd and 3rd term of a Geometric Progression find the nth 
    term of it and round it off upto 3 decimal places.
    char* nthTerm(double input1, double input2, int input3) {
        //your code here
    }
    input1 = 2nd term and input2 = 3rd term and both are between -2 to 2.
    input3 = nth term to be find and can be upto 100.
    e.g input1 = 1, input2 = 2, input3 = 4
          output = 4.0 done
Find two numbers in an array whose sum is equal to a given number. 
    We had to return the indices of the numbers, in an another array which 
    form the final pair. If there are multiple pairs, then return the indices 
    of the pair which contained the largest number.
    Eg: arr = [100,100,20,120,180] and sum=200 -> Possible answers are [0,1] 
    or [2,4] we should return [2,4] since arr[4] = 180 is the largest. done
Given two unsorted lists of integers find a pair of numbers closest to a 
    given number. Return all the possible pairs which are closest to the number.
    Eg: list1 = [20,10,30,20] & list2 = [20,30,40], target = 70
    Ans: [20,40],[30,30],[20,40]. 
    Note each number in the pair must be from each list done
Given a infinite stream of intergers, construct the list of pairs where 
    each pair represents all the integer elements between the range of two 
    elements. Maintain the updated List of pairs. Print/Output the updated 
    list after each encounter of an integer in the stream
    Stream till now : 7,10,15,9,8,3,2,5,???
    Output of list till now :
    [[7,10],[15,15],[2,5]]
    say there is integer 6 in coming as next element in the stream:
    Updated List of pairs or Array of pairs would be:
    [[2,10],[15,15]]
    Note: If a pair is [1,4] then you have all the integers [1,2,3,4] from 
    the stream, [9,13] represents [9,10,11,12,13] etc, else you have to add 
    a self element pair into the list like [x,x] if number x doesn???t fall 
    under a range in contructed pairs of your existing list. Update and output 
    the list of pairs as you read the stream of integers. !!!
Input is in <productId, timeStamp> format. So assume you have a list of 
    productIDs and their timestamps which they were accessed:
    [<product1, timestamp1>, <product2, timestamp2>, <product3, timestamp3>, ???]
    Find the top K products purchased in the last one hour.
Given a list of employees and their IDs as follows and the manager id is 0 for the CEO.
    eg.
    Jeff, 0
    John, 1
    Lisa, 1
    Jacob, 2
    Jason, 2
    David, 3
    Then ask to print the following form according to the class relationship:
    Jeff
         John
             Jacob
             Jason
         Lisa
             David #??????????????????????????????????????????
implementation of amazon prime video pause functionality.
    When we click pause button while watching prime video, it displays the list 
    of actors present at that particluar time.
    was given list of actors who appear at particular time range, and was asked 
    to implement a function when queried at particular time would list all the actor names.
    Jason - {2,9},{15,20}
    Jasica - {7,10}
    getActorNames(8) ??? > Jason,Jasica
    getActorNames(10) -->Jasica # ?????????Person???????????????name?????????????????????????????????????????????
                                # ?????????????????????????????????merge??????????????????????????????????????????
First Unique Number in Data Stream
    I used an ordered set and map to provide the answer. The set will store the 
    numbers which are added to the stream for the first time and map will store 
    the count.When a number comes the corresponding count of it in the map is updated. 
    When a number comes for the first time, I add it to the ordered set.
    When a number comes for the second time I remove it from the ordered set.
    The first elem from the set will be the number.I told this solution to the 
    interviewer to which he agreed and asked the time and space complexity.
    I answered both of them correctly. Then he started asking me what if you 
    didn???t have the ordered set. And that was like 5 minutes remaining.
    He expected me to answer a DLL instead of an ordered set, but what about 
    the solution I provided # ??????lru??????????????????????????????unique???????????????map???????????????????????????(??????????????????)
                            # ????????????????????????????????????map????????????????????????????????????map?????????????????????1???????????????????????????
                            # ??????+1?????????????????????1?????????
Given an absolute file path and a relative file path as inputs, write a 
    function to determine the working directory after performing a cd command 
    with the relative path as its argument.
    e.g.
    inputs:
    absolute path: ???/bin/etc/abc???
    relative path: ???/???/xyz/tuv/???/???
    output:
    ???/bin/etc/xyz??? done

OOD
Design a DMV office, implement an algorithm that places a customer at the best window
System Design Tic-Tac-Toe
Design Amazon Retail Website
LRU Cache
design an Elevator system
design locker system
shorten URL, Discussed : DB, WebServer, sharding
    focus on databses to be used
????????????????????????HashMap??? hashMap??????????????????????????????
design a hashMap for me with get/put functions and writing all test cases.
    Lint code Hash Fucntion ??? ????????????hash?????????
    what makes a good hash function !!!
???????????????????????????datastructure????????????????????????????????????????????????????????????????????????overlap
    ???????????????????????????meeting room?????????
????????????????????????rangelock?????????range????????????integer??????free????????????????????????wait
    ????????????????????????release lock
?????????????????????DFS???BFS !!!
??????data lake??????????????????
?????????????????????????????????????????????????????????????????????????????? !!!
system design????????? load balancer, cache???sharding !!!
??????debug??? ?????????????????????????????????????????? ????????????????????? ??????????????? !!!
design the DVR (settop box) feature to record a show
???????????????
????????????????????????https://1o24bbs.com/t/topic/17552
??????????????????API???????????????????????????????????????<word, defination>???????????????
    1. void add(word, def) 
    2. void remove(word)
    3. void update(word, def)
    4. String lookup(word) return defition
    5. printOut() ?????????????????? <word, def> pair ????????????word?????????
     add???remove???update???lookup??????O(1), printOut??????O(n) 
     bucket sort
     ??????word??????????????????????????????word.length() < 1000????????????Trie????????????
     add???remove???update???lookup????????????????????????????????????????????????????????????????????????
     ???????????????????????????????????????alphabetical?????????????????????
design a table reservation system for a restaurant which would be used 
    from a tablet interface by people coming to the front desk. I gave my 
    solution using a hash table for different table sizes, 2, 4, 6, 8 
    which would make use of priority queue to order them as FIFO. I think 
    I started well by asking some good questions and initial design of 
    the class and functions but kind of fumbled in the end to come up 
    with a solid design for function of AddGroup() which would add a 
    party to the waitlist. Ultimately got a reject from within few days. 
    Overall I felt I did good on LP questions but not so much on the above 
    design question.
You are given a logfile with multiple requests in the following form:-
    Timestamp Customer_ID Page_ID
    Assume that the logfile is sorted on timestamp. Find a way of generating the 
    most common 3 page sequence. A 3 page sequence is a sequence of pages 
    such that a user visits these 3 pages one after each other.
    eg.
    T1 C1 P1
    T2 C2 P2
    T3 C1 P2
    T4 C2 P1
    T5 C1 P1
    Here, the most frequent 3 page sequence is P1->P2->P1. C2 here is 
    a corner-case because C2 only visits 2 pages, asked about this and was 
    told to discard such sequences.
https://leetcode.com/problems/min-stack/
4-5 questions about linked list/stack/queue fundamentals
There is already defined Twitch video stream and chat box with a viewer count
    There is a User Service that requires User_id and provides User???s Age and Gender.
    Need to add Analytics dashboard of all viewers based on Gender, Age 
    distribuution graphs below the video stream.
    I had a WebSocket approach where the user devices provide heartbeat 
    checks to server and Server produces data analytics on active users.
techincal conecpt of OOPS
?????????????????????nosql ???sql?????????
?????????????????????lookup service. ??????????????????10 billion???key-value pair, 
    ????????????????????????????????????key??????????????????value???????????????key???size???0.1kB???
    ??????value???size???1kB???????????????qps >= 5000???latency < 200ms.
    server????????????:
    commodity server
    8X CPU cores on each server
    32G memory
    6T disk
    ?????????????????????server???????????????service
Design Instagram
OOD a system which has multiple warehouses connected by a transport system
    Further expanded the question by including different ways
    Only class-inheritance structure and major methods required !!!
Design an Amazon locker
    The interviewer asked me to OOD a locker system and also write working code for the same
    Follow up questions included expanding the design to accomodate various 
    different types of lockers like regular, freezing, hot, etc. !!!
Design Kubernetes
Propose a data structure to represent arithmetic expressions, write expression 
    evaluation function
Implement word suggestions + autocompletion given input as an ???old-style Nokia phone??? 
    string of digits
Design a system for Weather App (temperature only) given a data stream of 
    temperature readings from multiple sensors across the country !!!


LP:
Customer Obsession:
??? how do u show customer obession!!!
??? tell me about a time when you were not able to meet a time commitment
    what prevented you from meeting it? what was the outcome and what 
    do u learn from it!!! ????????????????????????????????????????????????????????????????????????????????????????????????
    have many projects, data platform, rule match, ????????????????????????????????????????????????
    ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
    ????????????????????????????????????????????????????????????????????????????????????????????????
??? Who was your most difficult customer?
??? Give me an example of a time when you did not meet a client???s expectation. 
    What happened, and how did you attempt to rectify the situation?
??? When you???re working with a large number of customers, it???s tricky to 
    deliver excellent service to them all. How do you go about prioritizing 
    your customers??? needs?
??? Tell the story of the last time you had to apologize to someone
??? Amazon always based on customer experience, do you have this experience?

Ownership:
??? give me an example of a time you faced a conflict while working on 
    a team? how did you handle that!!! dont sacrifice long team value
    ????????????????????????????????????????????????????????????????????????????????????

Invent and Simplify:
??? Tell me about a time when you gave a simple solution to a complex problem
    --> ???????????????back translation
??? Tell about the situation where u found a creative way to overcome 
    a problem!!! --> ???????????????back translation

Are Right, A Lot:!!!!!!!!!!!!!!!!!
??? tell a abot a time u stepped in to a leadership role!!! 
    --> ????????????????????????????????????
??? Tell me about a time when you were wrong --> solr index 
??? Tell me about a time when you had to work with incomplete data or information
    --> cmb chatbot

Learn and Be Curious:
??? an example of a time u faced a conflict while working on a team!!!
    --> solr index
??? a time when u missed an obvious solution to a problem!!! 
    --> solr index??????????????????????????????????????????????????????lucene?????????docker
??? Tell me about a time when you influenced a change by only asking questions
    --> 
??? Tell me about a time when you solved a problem through just superior 
    knowledge or observation

Hire and Develop The Best:
??? what did u do when u needed to motivate a group of individuals!!!
    --> ??????????????????????????????????????????????????????
??? Tell me about a time when you mentored someone 
    --> ???PM??????????????????????????????????????????

Insist on the Highest Standards:
??? do u collaborate with others well!!! --> ?????????????????????????????????push??????
??? a time u wish u'd handled a situation differently
??? Tell me about a time when you couldn???t meet your own expectations 
    on a project
??? Tell me about a time when a team member didn???t meet your expectations 
    on a project --> ??????data extraction????????????????????????????????????????????????
    no comments???????????????????????????????????????????????????????????????????????????code standard

Think Big:
??? a time when u faced a problem that had multiple solutions!!!
    --> nlp????????????, data generation techniques??????????????????
    back translation, add noise, random permution
??? tell me about a time when u had to choose between technologies
    for a project -->
??? Tell me about your proudest professional achievement 
    --> two weeks implementing a asycronous system
??? Tell me about a time when you went way beyond the scope of 
    the project and delivered -->

Bias for Action:!!!!!!!!!!!!!!!!!
??? Describe a time when you saw some problem and took the initiative to 
    correct it rather than waiting for someone else to do it --> 
??? Tell me about a time when you took a calculated risk --> 
??? Tell me about a time you needed to get information from someone who 
    wasn???t very responsive. What did you do -->

Frugality:
??? Tell me about a time when you had to work with limited time or resources!!!
    --> icredit????????????????????????????????????????????????????????????????????????scalable

Earn Trust:
??? a time when u received negative feedback from ur manager?
    how did u respond!!! --> ???????????????????????????????????????????????????????????????
    ???????????????????????????????????????????????????
    ???????????????????????????proactive???take more responsibility in design models
    ???????????????????????????
??? Tell me about a time when you had to tell someone a hard truth
    --> 

Dive Deep:!!!!!!!!!!!!!!!!!
??? Give me two examples of when you did more than what was required 
    in any job experience -->

Have Backbone; Disagree and Commit:
??? we all have to work with people that dont like us. how to u deal
    with someone that doesnt like u!!! --> ?????????????????????????????????????????????
    ??????????????????????????????????????????????????????dont have patience, easily lose temper
    ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????
    work quite well
??? Tell me about a time when you did not accept the status quo.
??? Tell me about a time when you had to step up and disagree with a team 
    members approach
??? If your direct manager was instructing you to do something you 
    disagreed with, how would you handle it? --> zhongyidong poc

Deliver Results:
??? an example of a time when u set a difficult goal and were able 
    to meet it --> ?????????????????????spa?????????navigation bar?????????????????????????????????
    ????????????????????????????????????????????????scalable???????????????????????????????????????worker???
    ??????dashboard???two weeks

??? By providing an example, tell me when you have had to handle a 
    variety of assignments. Describe the results 
    --> data platform, rule match and costomer requirements
??? What is the most difficult situation you have ever faced in your 
    life? How did you handle it? --> cmb chatbot, improve accuracy

mistake, tightddl, beyond expectation
How to persuade your coworkers to implement your suggestions?
What???s the most challenge thing in your work?
how to improve your system?
What do you learn from your work?




Duplicate a graph not clear
Given a grid of islands surrounded by 1s and 0s, find A route 
    from one point to another point. How do you count the number of islands done
Bahavioral ONLY.
Implement a traffic stop (one-way). Implement a traffic intersection.
Implement a Concurrency Service to check if a video stream is playing.
    How would you scale this?

Design and implement a class to support certain functions.
Straightforward LC Medium.

LC question which involves trie implementation, regarding versioning in trie
Dan Croitor on youtube ?????????????????????LP????????? !!!

Design a system for an api rate limiter
https://leetcode.com/problems/course-schedule/ done
https://leetcode.com/problems/course-schedule-ii/
https://leetcode.com/problems/search-in-rotated-sorted-array/ done
https://leetcode.com/problems/roman-to-integer/ done

lc819 done
lc277 done ????????????

Design a system where a seller puts an item for sale in the local 
    currency/ currency of his choice and the buyer can buy it from 
    anywhere by placing bids. If the bid reaches the max price or 
    the list price, need to mark the item as sold. There should be 
    some way to convert the currency.
    Answer: I started to answer the question and tried to get 
    everything I could get out of him. He seemed a little off to me. 
    At the end I came up with an idea that would help in extending 
    the solution and he kept saying that was not the question. 
    REALLY FRUSTRATING done
Given an List of String [???abcd???, ???efgh???, ???abcd???], find the string 
    that occurs odd number of times trie?????????hashset
Answer : I coded a solution using a HashMap in 5 minutes by maintaining 
    a count of eachh string. The interviewer wanted a solution that would 
    not use space. We kept discussing on it and he kept suggesting that 
    when I iterate through the array the first time I would encounter 
    any string would be a odd number. This was the hint and it was 
    confusing. At the end he suggested a solution using a HashSet 
    instead of Map so I asked him what is the difference as Set will 
    also use space. So then he said you wont have to iterate through 
    the List again as you can keep calculating the odd String on the 
    fly in one Pass. It didnt seem to be a possibility.
Design a Recommendation System(Customers who bought this also bought)
Answer : I nailed this round. The interviewer was really happy with 
    the Solution. He also asked to write the code for the API and 
    seemed really satisfied.
The interviewer drew a diagram of a system that had LB, Web Servers 
    and DB and asked me how I would scale it when there is slowness
Answer : I had read all the System Design jargons eg. Cache, NoSQL 
    DB etc etc. I redesigned the whole system by including a lot of 
    those technologies. It was satisfying to me but couldnt get a 
    read on the interviewer. He seemed satisfied though

Given tuples of (worker_id, num_hours_worked) find the top K workers 
    ranked by number o hours worked.
    Eg: Given
    (1, 30), (2, 20), (1, 40), (3, 10) k = 2
    Result = [1, 2] done
Design a HashSet with Expiry time. and methods to be implemented
    boolean contains(int key)
    boolean add(key)
    boolean removeExpiredKeys()
    Came up with simple HashMap solution first. Was asked to optimixxe 
    for removeExpiredKeys. Then came up with a solution using both 
    HashMap and PriorityQueue
Design an EventManager class and Subscriber class.
    Subscriber class can subscribe to a specific event with event Id.
    Rough outline of my solution
    class EventManager() {
        HashMap<integer, List<Subscriber> subscriber ;
        subscribe(Subscriber subscriber, int eventId) {
            // add this to the hashmap
        }
        unsubscribe(Subscriber subscriber, int eventId) {
            // remove this from the hashmap
        }
        createEvent(int eventId) {
        // create the event and call Subscriber. action() method for all 
        // its subscribers
        }
    }
    interface Subscriber {
        action() {
        }
    }
    I had to ask a lot of clarifying questions because his question was very vague.
    And he followed up with a few questions on concurrency issues etc.
Given a log of (customer_id, page_visited). Find the most visited 3-page sequence.
    Eg:
    Given log
    [1, 30]
    [1, 31]
    [1, 32]
    [1, 33]
    [2, 40]
    [2, 41]
    [2, 42]
    [3, 30]
    [3, 31]
    [3, 32]
    [1, 45]
    [2, 43]
    Answer: [30, 31, 32] done
Full on LP questions with Hiring manager - I think this is a very crucial 
    round. I was asked a lot of LP questions with a lot of follow up questions.
    All the interviews were on Whiteboard.

Count the number of black shapes in a 2-D bit map containing 0s and 1s 
Design a network of vending machines where customers can collected their 
    food items ordered on Amazon.com. Follow-up was to extend this system 
    to enable suppliers to stock the vending machines. Focus was placed 
    on high-level design, scalability, and details of the back-end 
    system design. Also, each design decision had to be justified
Design a queue using an array. Queue should be dynamically resizable
Design a game-controller to administer two games: Tic-Tac-Toe (traditional 
    3x3 board and a more generic mxn board) and Connect-4 (a generic 
    mxn board). Focus was more on object-oriented design and the use 
    of appropriate design patterns. The interviewer wanted to see 
    various classes and their relationships, and some basic APIs to 
    manage these games

Tell me a time where you had to make a decision without having enought data
Technical:
Given a set of words, how would you validate that user???s input is a valid word
    My solution: Binary search for word in set of words
Follow up Question: Users are complaining that this takes too long, 
    what can be used to improve it?
    My solution: If set of words were stored in a Trie, search 
    for word in Trie done
Follow up on follow up: How to improve so that as user writes word, 
    it suggest words with similar prefixes
    https://leetcode.com/problems/design-search-autocomplete-system/



'''