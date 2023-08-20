# Customer Delivery Location Management
    This is a location-based project built using Django, GeoDjango, Django Rest Framework, Rest Framework GIS, Docker, and other technologies. This project encompasses user authentication so that user can perform CRUD (Create, Read, Update, Delete) operations on their delivery locations. They can also set default/primary delivery. This provides a dedicated API for reteriving customer locations.

## Model Design:
    - User Model (Account App)
      - Extending Django `AbstractBaseUser` and `PermissionMixin` to create custom user model.
      - Thr user model includes fields like 'email', 'username','full_name' and custom booleans like `is_employee` and `is_customer`. This design allows for flexibility in user roles.
      - A custom user manager that handles custom user creations
      - The model also contains timestamps fields like joined_at, updated_at for tracking user registration and updates
      - A seperate Profile model having one to one relationship with the user model. It contains additional fields such as avatar, bio, etc which are common for all customers, employees, staffs and superusers.

    - Customer and Employee Models (Account App)
      - Seperate Customer and Employee models.
      - Each of them are linked to user model through a one-to-one relationship. This enables distinct user roles and functionalities.

    - DeliveryLocation Model:
      - The DeliveryLocation model is used for managing delivery locations.
      - It includes a foreign key relationship with the Customer model to associate each delivery location with a customer.
      - Fields like name, slug, location, and is_primary provide essential information about each delivery location.
      - Generate a unique slug for each location based on the customer's username and the location's name.
      - Slug is used in queries instead of using location_id.
      - The get_absolute_url method generates a URL for accessing a specific delivery location.

## Key Features:
    - User Authentication
        - Login: Registered customers can securely log in to access their delivery location management features.
        - Sign-up: New customers can create accounts to start managing their delivery locations.

    - Delivery Location Management
        - reate: Customers can add new delivery locations, specifying a name and geographic coordinates.
        - Read: Customers can view a list of all their saved delivery locations.
        - Update: Customers can edit the details of existing delivery locations, including their names and coordinates.
        - Delete: Customers can remove delivery locations they no longer need.

    - Technologies Used
        - Django: The core web framework that powers the project, offering a secure and structured development environment.
        - GeoDjango: An extension of Django for handling geospatial data, used for managing geographic coordinates.
        - Django Rest Framework: Simplifies the creation of RESTful APIs and provides robust serialization capabilities.
        - Django Rest Framework GIS: An extension of DRF for handling Geographic Information System (GIS) data.
        - Python-dotenv: python-dotenv is used to manage environment variables for your project. It allows you to keep sensitive information like API keys and database credentials secure.
        - psycopg2: Psycopg2 is a PostgreSQL adapter for Python. It enables Django to communicate with PostgreSQL databases, which are commonly used in Django projects.
        - Docker: Containerization for easy deployment and management of the project.
        - Django-cors-headers: handle Cross-Origin Resource Sharing (CORS) in your Django application.
        - Other Dependencies: A variety of additional packages such as Babel for localization crispy-bootstrap5 for form styling, and psycopg2 for PostgreSQL database communication.

## Installation:
    Follow these steps to set up and run the project:

### Prerequisites:
    - A computer/laptop
    - Internet Connection
    - Git (Versioning Tool)
    - Docker (optinal) or else Postgres Database
    - Maketools
    - Python 3.7 or greater

### Clone the Repository
    ```
    git clone https://github.com/ishanshre/GeoDjangoCLDM.git
    ```

### Environment Configuration
    Create a `.env` file in the project root directory and configure the necessary environment variables, such as database settings and API keys:
    ```
    DJANGO_SECRET=your-secret-key
    DEBUG=True
    db_container_name=new name of database container
    db_username=new database username
    db_password=new database password
    db_dbname=new database name
    db_host=database connection url or hostname or localhost or container ip address i.e. 172.17.0.2 (Only after the database container is created)
    ```

### Create Docker conaiter
    Run the make file from the root directory
    ```
    make createPostgis
    ```

    Or

    ```
    docker run --name db_container_name -e POSTGRES_USER=db_username -e POSTGRES_PASSWORD=db_password -e POSTGRES_DBNAME=db_dbname -p 5432:5432 -d postgis/postgis
    ```

### Populate the db_host in .env file
    ```
    docker inspect your-db-container-name
    ```
    You will find the IP address of container at last. And populate the db_host with it

### Create a Virtual Environment
    ```
    python -m venv venv
    ```

### Activate the Virutal Environment
    For linux (bash shell):
    ```
    source venv/bin/activate.bash
    ```
    For Windows (powershell):
    ```
    venv\Scripts\activate.bat
    ```

### Install Project Dependencies
    ```
    pip install -r requirements.txt
    ```

### Apply Database Migrations
    ```
    python manage.py migrate
    ```

### Create SuperUser
    ```
    python mannage.py createuseruser
    ```


# Access The Project
    - Web Application: http://localhost:8000
    - Django Admin Pannel: http://localhost:8000/admin
      - Use the username and password of superuser created in previous step

# API Documentation:
    - The Documentation is avaliable at:
      - APIDOC (Written in Markdown): [APIDOC](./APIDOCS.md) 
      - API ROOT: http://localhost:8000/api/v1
      - API SWAGGER: http://localhost:8000/api/docs/swagger
      - API REDOC: http://localhost:8000/api/docs/redoc

# Usuage:
    - Use the web application to input and manage delivery locations on the map.
    - Explore the API documentation to understand how to interact with the project's API endpoints.
    - Customize the project to meet your specific location-based needs.