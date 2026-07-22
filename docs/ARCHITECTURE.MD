# Architecture

InterviewPrepAI is a cloud-native full-stack web application that helps software engineering candidates prepare for technical interviews using AI-powered tools such as resume analysis, mock interviews, coding challenges, and personalized feedback.

The application follows a client-server architecture where the React frontend communicates with an ASP.NET Core Web API backend. The backend manages authentication, business logic, database operations, AI integrations, and file storage through PostgreSQL, AWS services, and the OpenAI API.

## Table of Contents

- High-Level Architecture
- Authentication Flow
- Resume Upload Flow
- AI Processing
- Database Architecture
- Deployment Architecture

---

## High-Level Architecture

![Architecture](../design/architecture/Overview.png)

> Editable source: [architecture.drawio](../design/architecture/Overview.drawio)