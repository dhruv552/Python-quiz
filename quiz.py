marks = 0
answer = []
an = {"Section 1": "DSA"}

def dsa():
    ans = 0
    a = [
        ["Que1. What does DSA stand for?", 
         "1. Data Structure and Algorithm", 
         "2. Dynamic System Analysis", 
         "3. Data Storage Architecture", 
         "4. Domain Specific Applications", 1],
        
        ["Que2. What is the time complexity for searching an element in a balanced Binary Search Tree (BST) on average?", 
         "1. O(n)", 
         "2. O(log n)", 
         "3. O(n log n)", 
         "4. O(1)", 2],
        
        ["Que3. Which data structure works on the principle of Last In, First Out (LIFO)?", 
         "1. Queue", 
         "2. Stack", 
         "3. Array", 
         "4. Deque", 2],
        
        ["Que4. What is the time complexity for accessing an element in an array using its index?", 
         "1. O(n)", 
         "2. O(1)", 
         "3. O(log n)", 
         "4. O(n log n)", 2],
        
        ["Que5. Which algorithm is often used to calculate the shortest path in a weighted graph?", 
         "1. Depth-First Search (DFS)", 
         "2. Breadth-First Search (BFS)", 
         "3. Dijkstra's Algorithm", 
         "4. Prim's Algorithm", 3]
    ]
    for i in range(len(a)):
        for j in range(5):
            print(a[i][j])
        answer.append(a[i][-1])
        an[a[i][0]] = a[i][a[i][-1]]

        ans1 = int(input("Enter your answer: "))
        print("\n")
        if ans1 == a[i][-1]:
            ans += 1
    
    return ans

def dbms():
    an["Section 2"] = ["DBMS"]
    ans = 0
    a = [
        ["Que1. What is a primary key in a database table?", 
         "1. A column with unique values for each record", 
         "2. A column that can have duplicate values", 
         "3. A column that links two tables", 
         "4. A column that can store null values", 1],
        
        ["Que2. What does ACID refer to in database transactions?", 
         "1. Atomicity, Consistency, Integrity, Data", 
         "2. Accuracy, Consistency, Isolation, Durability", 
         "3. Atomicity, Consistency, Isolation, Durability", 
         "4. Availability, Coherence, Integrity, Durability", 3],
        
        ["Que3. Which SQL command is used to create a new table?", 
         "1. CREATE TABLE", 
         "2. INSERT INTO", 
         "3. MODIFY TABLE", 
         "4. UPDATE", 1],
        
        ["Que4. Which type of JOIN will return all records from both tables when there is a match?", 
         "1. INNER JOIN", 
         "2. OUTER JOIN", 
         "3. FULL JOIN", 
         "4. LEFT JOIN", 3],
        
        ["Que5. What is the goal of normalization in a database?", 
         "1. To reduce redundancy and ensure data consistency", 
         "2. To make the database structure more complex", 
         "3. To allow storage of multiple copies of data", 
         "4. To make querying faster", 1]
    ]
    for i in range(len(a)):
        for j in range(5):
            print(a[i][j])
        answer.append(a[i][-1])
        an[a[i][0]] = a[i][a[i][-1]]

        ans1 = int(input("Enter your answer: "))
        print("\n")
        if ans1 == a[i][-1]:
            ans += 1
    
    return ans

def python():
    an["Section 3"] = ["Python"]
    ans = 0
    a = [
        ["Que1. Which Python data type is mutable?", 
         "1. Tuple", 
         "2. List", 
         "3. String", 
         "4. Integer", 2],
        
        ["Que2. Which keyword is used to define a function in Python?", 
         "1. func", 
         "2. def", 
         "3. define", 
         "4. create", 2],
        
        ["Que3. Which function is used to find the length of a list in Python?", 
         "1. length()", 
         "2. count()", 
         "3. len()", 
         "4. size()", 3],
        
        ["Que4. How do you declare a variable with value 10 in Python?", 
         "1. let x = 10", 
         "2. x := 10", 
         "3. x = 10", 
         "4. int x = 10", 3],
        
        ["Que5. What will `type(3.14)` return in Python?", 
         "1. int", 
         "2. float", 
         "3. decimal", 
         "4. double", 2]
    ]
    for i in range(len(a)):
        for j in range(5):
            print(a[i][j])
        answer.append(a[i][-1])
        an[a[i][0]] = a[i][a[i][-1]]

        ans1 = int(input("Enter your answer: "))
        print("\n")
        if ans1 == a[i][-1]:
            ans += 1
    
    return ans

def answ():
    print("Do you want to see the answers then enter 1 else 0")
    f=int(input("Enter your choice="))
    print("\n")
    if f==0:
        return
    else:
        for i in an:
            
             print(f"{i}\nanswer={an[i]}\n")
        

print("----------------Online Test------------------\n\n")
print("             Register as a user           ")
name=input("Enter your name: ").lower()
password=input("Enter your password:").lower()
n=False
l=False

print("              Login          ")
while l!=True:
    m=input("Enter your user name: ").lower()
    if m!=name:
       print("Invalid credentials\n Renter your details")
       l=False
    else:
        l=True
        while n!=True:
            k=input("Enter your password:").lower()
            print("\n")
            if k!=password:
               print("Invalid password")
               n=False
            else:
                n=True
                print("----------Quiz--------\n")
                print("Quiz Details\n\nQuiz Contains 3 sections\n 1.DSA\n 2.DBMS\n 3.Python\n")
                print("1.Each section contains 5 question carrying 1 mark for correct answer.")
                print("2.To clear the quiz you have to score minimum 6 marks.")
                print("3.Read all questions carefully and the enter your answer.")
                print("4.All the best for quiz")
                print("\n\n")
                print("Section 1:DSA\n")
                
                d=dsa()
                print("Section 2:DBMS\n")
                e=dbms()
                print("Section 3:Python\n")
                f=python()
                marks=d+e+f
                answ()
                
                if marks<6:
                    print(f"You fail the quiz and your  marks:{marks}")
                    print("Try better next time")
                    
                else:
                    print(f"You Passed the quiz with marks={marks}")
