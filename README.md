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
![image](https://github.com/YKim0172/organAIze/assets/132183038/bb444934-09fc-45b6-a9a7-e239bebd1c1e)
- Our homepage provides the user with necessary information on how OrganAIze works and how they can use it


![image](https://github.com/YKim0172/organAIze/assets/132183038/5d20063e-7c53-4997-b774-5f5413935612)
- This is the login page where users can choose to login to their preexisting account or to signup as a new user


![image](https://github.com/YKim0172/organAIze/assets/132183038/a3ecd572-c967-4d11-b46a-f59d57855530)
- This is the signup page for new coming users to create an account in order to use OrganAIze


![image](https://github.com/YKim0172/organAIze/assets/132183038/f7e07c27-fcee-46ea-add5-e8e768e8d501)
- Our edit profile page allows the user to add in courses that they have already taken at the University of Michigan. This will prevent repeat classes from popping up in the ML algorithm

![ezgif-2-2f3e888972](https://github.com/YKim0172/organAIze/assets/132183038/75033178-af3c-444a-8d23-cc8735b1b912)

- This is a demo of the machine learning algorithm. Here, the user inputs "web development" as their topic of choice. The machine learning algorithm takes those keywords in and provides the user with the top 5 classes for their input. These classes are ranked on three different categories, relevancy, difficulty (average GPA), and time commitment


