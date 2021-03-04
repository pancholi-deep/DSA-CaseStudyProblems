import time
import random

class Queue:
    def __init__(self):
        self.items = []
 
    def enqueue(self, data):
        self.items.append(data)
        
    def dequeue(self):
        return self.items.pop(0)

    def first(self):
        return self.items[0]

l = 1
print(f"FollowMe Game Instructions:")
print("Numbers will be shown in a sequence as per your level.")
print("Level 1 will show 1 number, Level 2 will show 2 numbers, etc...")
print("To progress to next level, you need to score full points in a level.")
overall_scores = []

while True:
    input(f"Press Enter to start level {l}...")
    time.sleep(2)
    print(f"Level {l}")
    res = [random.randrange(10, 100, 1) for i in range(l)]
    q = Queue()
    for i in res:
        q.enqueue(i)
    
    for r in res:
        print(r)
        time.sleep(2)
        print("\033[A \033[A")

    print("Enter the list elements in order as you remember: ")
    score = 0
    for i in range(len(res)):
        temp = int(input())
        if temp == q.first():
            score += 1
            q.dequeue()

    overall_scores.append(score)
    print(f"you scored {score}/{l} points in level {l}")
    if score != l:
        print(f"Incorrect!!!\nCorrect sequence was {res}")
        break
    else:
        l += 1
    
print(f"Your cumulative Score is: {sum(overall_scores)}")