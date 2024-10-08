# Ecommerce API

This project is a FastAPI-based REST API for an ecommerce platform. It provides authentication, CRUD operations for users and products, and integrates with PostgreSQL for database management. The API is designed with scalability and security in mind, following modern development practices.

---

## Features

- User authentication with JWT
- CRUD operations for users, products, and orders
- Role-based access control (Admin, User)
- PostgreSQL database integration
- Docker for containerized development and deployment
- Pre-commit hooks for linting and code formatting

---

## Getting Started

Follow the steps below to set up and run the project locally.

### Prerequisites

- [Python 3.12](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/USERNAME/ecommerce-api.git
    cd ecommerce-api
    ```

2. **Install dependencies using Poetry**:
    ```bash
    poetry install
    ```

3. **Set up environment variables**:
    Create a `.env` file at the root of the project with the following content:
    ```env
    DATABASE_URL=postgresql://postgres:password@localhost:5432/ecommerce_db
    SECRET_KEY=your-secret-key
    ```

4. **Run database migrations**:
    ```bash
    alembic upgrade head
    ```

5. **Run the application**:
    ```bash
    poetry run uvicorn app.main:app --reload
    ```

---

## Running with Docker

1. **Build and run the Docker containers**:
    ```bash
    docker-compose up --build
    ```

2. The application will be available at `http://localhost:8000`.

---

## Running Tests

To run the test suite:
```bash
pytest


