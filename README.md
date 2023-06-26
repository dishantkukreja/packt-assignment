# Stack Overflow Data Extraction Project

This project aims to extract data from the Stack Overflow API and perform various tasks on the retrieved data.

## Project Overview

The project focuses on extracting the following information from the Stack Overflow API:

1. Trending Tags: Retrieve the trending tags for the month of May 2023.
2. Active Users: Fetch the active users from the Stack Overflow API for the past week.
3. Highest Scored Question: Retrieve the question asked with the highest score for the month of June 2023.
4. Highest Scored Answers: Store the answers with the highest score for the month of June 2023.

## Prerequisites

Before running the project, ensure that you have the following dependencies installed:

- Docker: You can download and install Docker from the official website: https://www.docker.com/get-started

## Getting Started

Follow the steps below to run the project with a Postgres database using Docker (copy steps in terminal):

1- docker pull postgres

2- docker build --no-cache -t my-packt_image .

3- docker run -d -p 5432:5432 --name my-p-container my-packt_image

4- pip3 install -r requirements.txt

Note: Ensure that no other processes are using port 5432 on your local machine.

Once the container is running, the Postgres connection will be established, and you can proceed to run the main.py file. The project will then extract the required data from the Stack Overflow API and store it in the Postgres database.

## Additional Information

For additional information about the project, including its implementation details, data extraction process, and database schema, please refer to the project documentation or contact the project contributors.

## Contributors

- Dishant kukreja(dishantkukreja26@gmail.com)

Feel free to reach out to the contributors for any questions or feedback.
