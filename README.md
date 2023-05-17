OrgAInise is a machine learning model developed under Python that provides a user precise class recommendation for the University of Michigan EECS department. 

Motivation : As current undergraduate students studying computer science at the University of Michigan, we have both grown tired of the need to constantly scroll through the course catalog to search for specific classes. A simple Google-like search on our website allows for students to quickly get a list of classes that are ranked in different categories to meet a student's needs. 

How to use: 
The database allows a user to create an account by storing their email, password, and classes-taken. 
After registering/logging-in, the user is taken to the main page where they will be able to enter a prompt into the textbook (e.g “I want to learn about web development). 
The machine learning algorithm will take the prompt and return 5 classes (excluding classes-taken), under 3 different categories. 
Most relevant classes to the prompt
The classes that have the highest average GPA
The classes that require the least amount of time/work


How it works: We first trained the classifier by implementing the “Bag of Words” model which would associate each EECS class with certain keywords. Then, with the trained classifier, it assigns each EECS class a log-probability score dependent on the prompt that was inputted by the user. The EECS classes’ scores are compared and depending on the category, they are outputted in the order of the top five highest scores. 

