
<h1 align="center">Fitness Tracking API</h1>
<p align="center"><i>Your best API  for managing fitness related data <br> (A user-friendly API).</i></p>

<h3>Demo</h3>
<hr>

<ul>
<li><b>Demo</b> - click <a href="https://youtu.be/uwYHgeGOwIc?si=jAIYV8tTga9pqUWu"><b>here </b></a>
<ul>
<li><b>Login:</b>adminemenikefitness2023</li>
</ul>

<h3>Description</h3>
<hr>
<p align="justify">
	This Fitness Tracking API built with Django framework is designed to  provide a comprehensive set of endpoints that allow users to track and manage their fitness-related data, such as creating and managing workouts, adding exercises to workouts, and tracking their progress over time.

By offering a standardized and efficient way to access and manage fitness data, the API will empower developers to create a wide range of fitness applications and services.
</p>

<h3>Reason/Purpose</h3>
<hr>

<p align="justify">
    
The purpose of building this fitness tracking API with Django is to provide a strong and expandable  platform for managing and analyzing fitness-related data. This API serves several key reasons:


1.	User Empowerment: This API will empower users to take control of their fitness journey. It allows them to record and monitor their workouts, making it easier to set and achieve fitness goals.


2.	Customization: Users can create personalized workout routines by adding specific exercises, repetitions, and sets tailored to their fitness objectives. This level of customization enhances the effectiveness of their training.


3.	Progress Tracking: Users can track their progress over time, which is essential for motivation and goal attainment. The API can generate visual representations of their improvements, such as charts or graphs, making it easier to see the results of their hard work.


4.	Consistency: Users can maintain consistency in their fitness routines by having a digital record of their workouts. This minimizes the risk of forgetting exercises or losing track of their training history.


5.	Data-Driven Decision-Making: The API can provide insights into the effectiveness of different exercises and workout routines. Users can make data-driven decisions to optimize their training strategies and maximize their results.


6.	Accountability: Users can share their workout data with trainers, friends, or workout buddies, fostering a sense of accountability and support within their fitness community.


7.	Accessibility: The API ensures that users can access their workout data from various devices, including mobile apps and websites, making it convenient to record and review their progress wherever they go.

</p>

<p align="justify">
    Furthermore,  building a fitness tracking API with Django focused on workout tracking, exercise management, and progress monitoring enables users to take charge of their fitness journeys. It provides customization, data-driven insights, and accessibility, all contributing to more effective and enjoyable workouts, as well as facilitating research in the fitness and healthcare domains.
</p>


<h2>Installation</h2>

<h4> Clone the repository to your local machine</h4>

git clone https://github.com/your-username/Fitness_Tracking_API.git


<h4>Set up the database</h4>


python manage.py makemigrations

python manage.py migrate

<h4>Create a superuser</h4>


python manage.py createsuperuser


<h4>Run the development server</h4>


python manage.py runserver


The API will be accessible at http://localhost:8000/ by default.


<h2>Usage </h2>

<h3>Authentication</h3>

To access the API endpoints, you need to authenticate using the token authentication method. You can obtain a token by sending a POST request to the /api-token-auth/ endpoint with your username and password in the request body. The API will respond with a token that you can use to authenticate subsequent requests.

<h3>Endpoints</h3>

<h4>Workouts</h4>

GET /workouts/: Returns a list of all workouts.

POST /workouts/: Creates a new workout.

GET /workouts/{id}/: Returns the details of a specific workout.

PUT /workouts/{id}/: Updates a specific workout.

DELETE /workouts/{id}/: Deletes a specific workout.

<h4>Exercises</h4>

GET /exercises/: Returns a list of all exercises.

POST /exercises/: Creates a new exercise.

GET /exercises/{id}/: Returns the details of a specific exercise.

PUT /exercises/{id}/: Updates a specific exercise.

DELETE /exercises/{id}/: Deletes a specific exercise.

</p>

<h2>Future development plans</h2>

<h3>Improvements</h3>
<p>
	<i> Generally,  I will just add some bug fixes/improvements from time to time </i>
</p>	
<hr>
<h3>Contributing</h3>
<p>
        <i>I would be happy to receive your help and participation with enhancing the solutions and code contained here. Please visit the
<a href="https://github.com/Githubnath/Personal-management-system/blob/main/CONTRIBUTING.md">guidelines for contributing</a
<i>
</p>

<h3>Technologies Used</h3>

<ul>
<li>Django: As the core web framework for API development</li>
<li>Django REST framework: For building RESTful APIs efficiently</li>
<li>SQLite: For database storage and management</li>
<li>Postman: To test API endpoints during development</li>
<li>Git: Version control for collaborative development
</li>
</ul>

<h2>Special thanks to</h2>
<ul>
	<li><a href="https://github.com/lomsey41">Salome Bassey</a> - For  her  technical  support
</ul>

<h3>License</h3>
<p>
        <i>README.md Unless otherwise noted, the software in this repository is licensed under the [MIT] license.</i>
</p>
<hr>

<h3> Author</h3>
<ul>
<li>Name: Nathaniel Emenike </li>
</ul>

<h3>Linkedin</h3>

<ul>
        <li><a href="https://www.linkedin.com/mwlite/in/nathaniel-emenike">Emenike Nathaniel</a> - Author's  Linkedin
</ul>


<h3>Twitter</h3>

<ul>
        <li><a href="https://www.twitter.com/EngrNath3">Emenike Nathaniel</a> - Author's  Twitter Handle
</ul>

<h3>Email</h3>
<hr>
- <p align="left"><b>Mail</b> - <a href="mailto:emenikenathaniel55@gmail.com"><i>emenike.nathaniel@gmail.com</i></a></p>
