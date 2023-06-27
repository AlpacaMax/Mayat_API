# Mayat API

This will be an individual service that Anbuis interact with through HTTP. It runs mayat over students' code on github and stores the result in database.

## Usage

- **Create New Task**
    ``` JSON
    POST /check_git_repos

    {
        "urls": [ // SSH URLs for github repos
            "git@github.com:username1/something1.git",
            "git@github.com:username2/something2.git",
            "git@github.com:username3/soemthing3.git"
        ],
        "file": "user/sort.c", // Specific path for each directory
        "language": "C" // The language
    }
    ```
    ``` JSON
    {
        "status": 1, // Status of the task. 1 is Running. 2 is Finished. 3 is Error.
        "id": 10,
        "result": "", // Result from Mayat in JSON format
        "datetime_created": "2023-06-22T06:53:51",
        "message": "" // Additional messages for users
    }
    ```
- **Get a Task**
  ``` JSON
  GET /task/10
  ```
  ``` JSON
  // Aftering waiting for Mayat to finish
  {
    "result": "{\n    \"current_datetime\": \"2023-06-22 14:52:47 ... \"execution_time\": 0.022368\n}",
    "id": 10,
    "status": 2,
    "message": "",
    "datetime_created": "2023-06-22T06:53:51"
  }
  ```