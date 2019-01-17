import sys
from collections import deque


class Solution:
    stack = []
    queue = deque([])

    def pushCharacter(self, c):
        self.stack.append(c)

    def popCharacter(self):
        return self.stack.pop()

    def enqueueCharacter(self, c):
        self.queue.append(c)

    def dequeueCharacter(self):
        return self.queue.popleft()
