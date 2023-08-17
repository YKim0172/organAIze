# OrgAInize 
is a website developed using Python and Django that provides a user-precise class recommendation through our machine learning algorithm for the University of Michigan EECS department. 

## Motivation: 
As current undergraduate students studying computer science at the University of Michigan, we have both grown tired of the need to constantly scroll through the course catalog to search for specific classes. A simple Google-like search on our website allows for students to quickly get a list of classes that are ranked in different categories to meet a student's needs. 

## How to use: 
1. The database allows a user to create an account by storing their email and password.
2. Users are able to indicate classes that they have taken. This would prevent recommendations of already taken classes. 
3. After registering/logging-in, the user is taken to the main page where they will be able to enter a prompt into the textbook (e.g “I want to learn about web development). 
4.  The machine learning algorithm will take the prompt and return 5 classes (excluding classes-taken), under 3 different categories. 
    - Most relevant classes to the prompt
    - The classes that have the highest average GPA
    - The classes that require the least amount of time/work

## Screenshots:
![image](https://github.com/YKim0172/organAIze/assets/132183038/a15ceb07-1073-40c2-b698-515443403a69)
- Our homepage provides the user with necessary information on how OrganAIze works and how they can use it.


![image](https://github.com/YKim0172/organAIze/assets/132183038/b2370367-4869-4f06-9d79-cb4c969fb4e5)
- This is the login page where users can choose to login to their preexisting account or to signup as a new user. 


![image](https://github.com/YKim0172/organAIze/assets/132183038/ef3f389c-deb3-4529-87bd-253b5fe0310c)
- This is the signup page for new coming users to create an account in order to use OrganAIze.  


![image](https://github.com/YKim0172/organAIze/assets/132183038/c105349d-187f-41c7-992f-2d56873c039f)
- Our edit profile page allows the user to add in courses that they have already taken at the University of Michigan. This will prevent repeat classes from popping up in the ML algorithm. 

![image](https://github.com/YKim0172/organAIze/assets/132183038/b963965a-5db7-4fab-9a3d-dde24053c500)


