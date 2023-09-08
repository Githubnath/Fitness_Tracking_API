####  Fitness Tracking API
![Demo link](https://github.com/Githubnath
[Project link](https://g

# Fitness Tracking API

This is a RESTful API for tracking workouts and exercises. The API allows users to create and manage workouts, add exercises to workouts, and track their progress over time.

### Task - Webstack portfolio project (Fitness Tracking API)

### alx_africa
The ALX Holberton Software Engineering programme is a 12-month(70h/week) immersive programme that engages technology enthusiasts and budding software engineers in a variety of programmes across in-demand tech disciplines to prepare them for a global career as a Full-Stack Developer.

## Starting the project


## Installation
Clone the repository to your local machine. git clone https://github.com/your-username/Fitness_Tracking_API.git
Set up the database.

python manage.py makemigrations

python manage.py migrate

Create a superuser.
python manage.py createsuperuser

Run the development server.
python manage.py runserver

The API will be accessible at http://localhost:8000/ by default.
## Usage
# Authentication
To access the API endpoints, you need to authenticate using the token authentication method. You can obtain a token by sending a POST request to the /api-token-auth/ endpoint with your username and password in the request body. The API will respond with a token that you can use to authenticate subsequent requests.

## Endpoints

# Workouts
GET /workouts/: Returns a list of all workouts.
POST /workouts/: Creates a new workout.
GET /workouts/{id}/: Returns the details of a specific workout.
PUT /workouts/{id}/: Updates a specific workout.
DELETE /workouts/{id}/: Deletes a specific workout.
Exercises
GET /exercises/: Returns a list of all exercises.
POST /exercises/: Creates a new exercise.
GET /exercises/{id}/: Returns the details of a specific exercise.
PUT /exercises/{id}/: Updates a specific exercise.
DELETE /exercises/{id}/: Deletes a specific exercise.

> Housify is a Property management web app that helps people to rent or buy property at any part of the World. We are using Rapid API to list the available houses, With Agents to facilitate the process. 


### Task - Full Stack webstack portfolio project(Housify)

### alx_africa
The ALX Holberton Software Engineering programme is a 12-month(70h/week) immersive programme that engages technology enthusiasts and budding software engineers in a variety of programmes across in-demand tech disciplines to prepare them for a global career as a Full-Stack Developer.

## Starting the project

1. Clone the repo to your device.
2. From the backend directory, create a virtual environment and set the required environment variables.
3. Start the backend server using by Downloading the installer from [NodeJS WebSite](https://nodejs.org/en/)
    * Run the installer.
    * Follow the installer steps, agree the license agreement and click the next button.
    * Restart your system/machine.
    * Now, test NodeJS by printing its version using the following command in Command Prompt:
        * ` node -v `
4. Run another terminal session. In the frontend directory, run `npm install` to install the required dependencies.
5. Finally, start the frontend server using `npm start`
6. You can view the website by visiting [http://localhost:3000](http://localhost:3000) in your browser.

## Tech Used

`React` `Tailwind CSS` `Express JS` `Mongo DB`

AUTHORS

* Mildred Makori **[Github](https://github.com/kwamboka1)** , **[twitter](https://twitter.com/makori_mildred)**, **[Linkedin](https://www.linkedin.com/in/mildred-makori-892652120/)**
* Emma Udeji **[Github](https://github.com/emmaudeji)** , **[twitter](https://twitter.com/)**, **[Linkedin](https://linkedin.com/in/emmanuel-udeji)**
* Zelipha Wambui **[Github](https://github.com/Zelipha)**, **[twitter](https://twitter.com/Miss_zeliq)**, **[Linkedin](https://www.linkedin.com/in/zelipha-wambui)**
* Robert Mudzonga **[Github](https://github.com/RobertMudzonga)**, **[twitter]()**, **[Linkedin](linkedin.com/in/robert-mudzonga-06b1ba21a)**


> Show love by leaving a ⭐️ if you like this project and don't forget to fork, break and modify 
