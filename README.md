
base_url: `https://task-api-nhnv.onrender.com`

## Authentication

JSON Web Tokens (JWT) for authentication. The authorization header must follow this format:

`Authorization: Access_token <your_access_token>`

The prefix is `Access_token`, not the standard `Bearer`.


## Endpoints

### 1. Register User
*   **url:** `base_url/register/`
*   **method:** `POST`
*   **payload:**
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "confirm_password": "your_password"
    }
    ```
*   **description:** Creates a new authentication user. Only then you may access the other endpoints.

### 2. Obtain Token
*   **url:** `base_url/access_token/`
*   **method:** `POST`
*   **payload:**
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
*   **response:**
    ```json
    {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    ```

### 3. Refresh Token
*   **url:** `base_url/refresh_token/`
*   **method:** `POST`
*   **payload:**
    ```json
    {
      "refresh": "<your_refresh_token>"
    }
    ```
*   **response:**
    ```json
    {
      "access": "<new_access_token>"
    }
    ```

### 4. Users 
requires the authentication header in request

*   **List Users:** `GET base_url/endpoints/users/`
*   **Create User Entry:** `POST base_url/endpoints/users/`
*   **Retrieve User:** `GET base_url/endpoints/users/<user_name>/`
*   **Update User:** `PUT base_url/endpoints/users/<user_name>/`
*   **Partial Update:** `PATCH base_url/endpoints/users/<user_name>/`
*   **Delete User:** `DELETE base_url/endpoints/users/<user_name>/`


### 5. Tasks
requires the authentication header in request

*   **List Tasks:** `GET base_url/endpoints/tasks/`
*   **Create Task:** `POST base_url/endpoints/tasks/`
*   **Retrieve Task:** `GET base_url/endpoints/tasks/<task_id>/`
*   **Update Task:** `PUT base_url/endpoints/tasks/<task_id>/`
*   **Partial Update:** `PATCH base_url/endpoints/tasks/<task_id>/`
*   **Delete Task:** `DELETE base_url/endpoints/tasks/<task_id>/`

## Throttling
To ensure fair usage, the following limits are applied:
- **Users Endpoints:** 50 requests/min
- **Tasks Endpoints:** 50 requests/min

## Filtering & Search
The tasks endpoint supports advanced filtering via `django-filter`. You can filter tasks based on various attributes.

**Examples:**
*   **Filter by Status:** `GET base_url/endpoint/tasks/?status=pending`
*   **Filter by Multiple Statuses:** `GET base_url/endpoint/tasks/?status__in=pending,running`
*   **Filter by Priority:** `GET base_url/endpoint/tasks/?priority=high`
*   **Filter by Assigned User:** `GET base_url/endpoint/tasks/?assigned_to=john_doe`
*   **Search by Task Name:** `GET base_url/endpoint/tasks/?task_name__icontains=database`

Available filters: 
*  [`status`, `priority`, `assigned_by`, `assigned_to`] (support `exact` and `in`) 
*  [`task_name`] (supports `exact` and `icontains`).

## Pagination
The API uses different pagination styles for Users and Tasks to demonstrate flexibility.

*   **Offset Pagination (users):**
    *   **Parameters:** `index` (offset), `size` (limit).
    *   **Example:** `GET base_url/endpoint/users/?index=0&size=5` => returns the 5 users where the first user's index is '0'
    *   **Limit:** Maximum of 7 users per page.

*   **Page Number Pagination (tasks):**
    *   **Parameters:** `page_no` (page number), `size` (page size).
    *   **Example:** `GET base_url/endpoint/tasks/?page_no=1&size=5` => returns the first page containing 5 tasks
    *   **Limit:** Maximum of 8 tasks per page.

## Tokens
- **Access Token Lifetime:** 30 minutes.
- **Refresh Token Lifetime:** 1 day.

