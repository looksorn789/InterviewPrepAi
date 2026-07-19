# InterviewPrepAi

## Overview

InterviewPrep AI is a full-stack web application designed to help software engineering candidates prepare for technical and behavioral interviews using AI-powered feedback.

The platform analyzes a user's resume, generates personalized interview plans, conducts mock interviews, and tracks progress over time. It is being built with scalability and cloud deployment in mind using modern software engineering practices and AWS infrastructure.

This project serves as a demonstration of production-ready software development, including authentication, cloud storage, containerization, automated deployment, and scalable backend architecture.
An AI-powered interview preparation platform that generates personalized technical and behavioral interviews based on a user's resume and career goals. 

## Features (Planned)

### Authentication
* Secure user authentication with Amazon Cognito
* Google and GitHub OAuth
* Email verification and password recovery
* Protected routes and role-based authorization

### Resume Analysis
* Upload resumes securely to Amazon S3
* Extract skills, education, projects, and technologies using AI
* Generate a personalized user profile

### Personalized Interview Plans
Generate interview questions tailored to:
* Python
* SQL
* Data Structures & Algorithms
* System Design
* Behavioral Interviews
Interview plans are customized using the user's resume and desired job role.

### Ai Coding Coach
Practice coding interview questions with AI-assisted guidance.

Features include:

* Personalized coding challenges
* Step-by-step hints
* Explanation of optimal solutions
* Follow-up questions based on common interview scenarios
* Mock Interviews

### Conduct AI-powered mock interviews covering:

* Behavioral questions
* Technical questions
* Coding interviews
* Role-specific interview questions

After each session, receive detailed feedback and improvement suggestions.

### Progress Dashboard

Track your interview preparation through:

* Questions completed
* Mock interviews taken
* Strengths and weaknesses
* Progress charts
* Learning streaks

## Tech Stack/Technologies used

Frontend
* React
* TypeScript
* Tailwind CSS

Backend
* Flask
* SQLAlchemy
* PostgreSQL

Cloud
* AWS Cognito
* Amazon EC2
* Amazon S3
* Amazon RDS
* CloudFront
* Route 53
* AWS Certificate Manager

DevOps
* Docker
* GitHub Actions
* Nginx

AI
* OpenAI API
