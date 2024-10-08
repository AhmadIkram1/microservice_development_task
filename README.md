This project consists of two Django applications (acss and sis) running as separate microservices. Each service has its own server, with acss running on port 8000 and sis on port 8001. This project requires Python and Django, along with other dependencies listed in the requirements.txt file.
Prerequisites
Before you begin, ensure you have Python installed on your system. You can download Python from the official site:

•	Python Download
After installing Python, make sure you have pip (Python's package installer) available.
Setting up the Project
Follow the steps below to set up and run the project:

1. Clone the Repository
If you haven't already, clone the repository to your local machine.

```
git clone https://github.com/AhmadIkram1/microservice_development_task.git/
```

```
cd microservice_development_task
```

2. Open Two Terminals

You'll need two terminal windows to run each Django app simultaneously.

Terminal 1 - Running acss Application

3.	Navigate to the acss directory:
```
cd acss
```

4.	Install the required dependencies from the requirements.txt file:
```   
pip install -r requirements.txt
```
5.	Run the Django development server on port 8000:
```   
python manage.py runserver 8000
```
Terminal 2 - Running sis Application

6.	Navigate to the sis directory:
```
cd sis
```
7.	Run the Django development server on port 8001:
```
python manage.py runserver 8001
```
8. Access the Applications
   
•	The acss application will be running on http://127.0.0.1:8000/.

•	The sis application will be running on http://127.0.0.1:8001/.

9. Both Systems are communicating with each other using API'S.

 SIS API Endpoints:

  API to get the list of enrolled studends

```
http://127.0.0.1:8001/api/getenrollments/

```

  API to get the list of courses

```
http://127.0.0.1:8001/api/getcourses/

```

 ACSS API Endpoints:

  API to get the schedule list

```
http://127.0.0.1:8000/api/schedules/

```