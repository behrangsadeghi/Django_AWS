# Django AWS Lambda Event-Driven Project

This project demonstrates a simple primitive serverless, event-driven architecture using Django ORM, AWS Lambda, AWS EventBridge, and AWS SQS. The Lambda function interacts with the Django ORM for database operations and processes events/messages passed through EventBridge and SQS.

## Project Structure

- **Django ORM**: Manages the PostgreSQL database interactions.
- **AWS Lambda**: Executes the main handler for processing messages from SQS and triggering Django ORM operations.
- **AWS EventBridge**: Routes events to SQS.
- **AWS SQS**: Acts as a message queue to handle asynchronous tasks.

## Features

- Event-driven architecture with AWS EventBridge and SQS.
- Integration with Django ORM in a serverless environment.
- Easy deployment to AWS Lambda with environment-based configuration.

## Setup Instructions

### Prerequisites

- **Python 3.8+**
- **Django** and **Django Rest Framework** for ORM and API.
- **AWS CLI** configured with permissions for Lambda, SQS, and EventBridge.

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/behrangsadeghi/Django_AWS.git
    cd Django_AWS
    ```

2. **Set up a virtual environment and install dependencies**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Configure environment variables**:

    Copy the `.env.example` to `.env` and fill in the necessary values:

    ```plaintext
    SECRET_KEY=your_secret_key
    DB_NAME=your_database_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_PORT=your_db_port
    AWS_SQS_QUEUE_URL=your_sqs_queue_url
    ```

4. **Run database migrations**:

    ```bash
    python manage.py migrate
    ```

### Running Locally

For testing Django locally:

```bash
python manage.py runserver
