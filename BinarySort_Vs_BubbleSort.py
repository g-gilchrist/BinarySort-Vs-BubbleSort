#================================================================================================================
#    Author: Grant Gilchrist
#    Problem: Make a list, check it twice make sure if the runtime on each sort is naughty or nice.
#================================================================================================================

import time
import random

# ---------------------------------------------------------           
# "Random" Hexidecimal Generator
# ---------------------------------------------------------


def RandomNum(length):
    print("\n""- GENERATING LIST -")
    for i in range(length):
        x = random.random()
        List.append(x)
        
        
# ---------------------------------------------------------           
# TREE SORT
# ---------------------------------------------------------        
# This is a simple Binary Tree that sorts the random List


class Groot:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def seperateList(self,List):
        for data in List:
            G.add(data)

    def add(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Groot(data)
            else:
                self.left.add(data)
        elif data > self.data:
            if self.right is None:
                self.right = Groot(data)
            else:
                self.right.add(data)       
                
    def reorder(self):
        if self.left:
            self.left.reorder()
        List2.append(self.data)
        if self.right:
            self.right.reorder()
            
            
# ---------------------------------------------------------           
# BUBBLE SORT
# ---------------------------------------------------------            


class BbblSrt():
    def __init__(self,List3):
        self.length = length

    def bubbleSort(self):  
        print("\n""please be patient, I'm preforming a Bubble Sort...""\n")               
        for index1 in range(self.length):
            for index2 in range(self.length-1):             
                self.swapElement(index1,index2)
            
    def swapElement(self,x,y):
        if List3[x] < List3[y]:
            List3[x], List3[y] = List3[y], List3[x]


# ---------------------------------------------------------           
# MAIN
# ---------------------------------------------------------

List=[]
length=10000
start = time.time()     
RandomNum(length)
end = time.time()     
print("\n""- LIST GENERATED - ")

# ---------------------------------------------------------

List2 = []
start1 = time.time()          
G = Groot(.45)
G.seperateList(List)
G.reorder()
end1 = time.time()
print("\n""I'm preforming a tree sort... Just kidding I'm done.")

# ---------------------------------------------------------

List3 = [*List]
start2 = time.time()
BbblSrt = BbblSrt(List3)   
BbblSrt.bubbleSort()
end2 = time.time()

# ---------------------------------------------------------


NumGen_Runtime = end - start
TreeSrt_Runtime = end1 - start1
BubbleSrt_Runtime = end2 - start2

print(List2)
print('\n\n\n\n\n\n', List3)

print('\n'f"Array Generator Runtime: {NumGen_Runtime}")
print(f"Tree Sort Runtime: {TreeSrt_Runtime}")
print(f"Bubble Sort Runtime: {BubbleSrt_Runtime}")

if TreeSrt_Runtime < BubbleSrt_Runtime:
    print("\n"f"Tree Sort is the faster sort method by {BubbleSrt_Runtime - TreeSrt_Runtime} seconds")
else:
    print("\n"f"Bubble Sort is the faster sort method by {TreeSrt_Runtime - BubbleSrt_Runtime} seconds")
    



  
        
    
    
        