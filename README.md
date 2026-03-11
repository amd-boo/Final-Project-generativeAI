CodeCraftHub Learning Management System

A simple personalized learning platform for developers to track courses they want to learn.
Features

    Add courses with target completion dates
    View all your courses
    Update course information and status
    Delete completed courses
    JSON file-based storage (no database needed)
    RESTful API design
    Proper error handling

Installation

    Clone or download the project
    Install Python dependencies:

    pip install -r requirements.txt

Running the Application

Start the Flask server:

python app.py

The API will be available at http://localhost:5000
API Endpoints
1. Add a Course
POST /api/courses

Request body:
{
  "name": "Python Basics",
  "description": "Learn Python fundamentals",
  "target_date": "2025-12-31",
  "status": "Not Started"
}

2. Get All Courses
GET /api/courses

4. Get Specific Course
GET /api/courses/<id>

4. Update Course
PUT /api/courses/<id>

Request body (all fields optional):
{
  "status": "In Progress"
}

5. Delete Course
DELETE /api/courses/<id>

Testing

Test 1: Add a New Course (POST):
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Basics",
    "description": "Learn Python fundamentals including variables, loops, and functions",
    "target_date": "2025-12-31",
    "status": "Not Started"
  }'

Expected Response (201 Created):
{
  "success": true,
  "message": "Course added successfully",
  "course": {
    "id": 1,
    "name": "Python Basics",
    "description": "Learn Python fundamentals including variables, loops, and functions",
    "target_date": "2025-12-31",
    "status": "Not Started",
    "created_at": "2025-11-04 10:30:00"
  }
}

Test 2: Get All Courses (GET)
curl http://localhost:5000/api/courses

Expected Response (200 OK):
{
  "success": true,
  "count": 1,
  "courses": [
    {
      "id": 1,
      "name": "Python Basics",
      "description": "Learn Python fundamentals",
      "target_date": "2025-12-31",
      "status": "Not Started",
      "created_at": "2025-11-04 10:30:00"
    }
  ]
}

Test 3: Get Specific Course (GET)
curl http://localhost:5000/api/courses/1

Test 4: Update Course (PUT)
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress"
  }'

Test 5: Delete Course (DELETE)
curl -X DELETE http://localhost:5000/api/courses/1

Error Test Cases

Test 6: Missing Required Fields
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Incomplete Course"
  }'

Expected Response (400 Bad Request):
{
  "success": false,
  "error": "Missing required field: description"
}

Test 7: Invalid Status Value
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Course",
    "description": "Test",
    "target_date": "2025-12-31",
    "status": "Invalid Status"
  }'

Test 8: Course Not Found
curl http://localhost:5000/api/courses/999

Expected Response (404 Not Found):
{
  "success": false,
  "error": "Course not found"
}


Troubleshooting
Problem: "Module not found: flask"
Solution: Run pip install -r requirements.txt

Problem: "Port already in use"
Solution: Stop other applications using port 5000 or change the port in app.py


Project Structure
/
├── app.py           # Main Flask application
├── courses.json     # Data storage (auto-created)
└── requirements.txt # Dependencies
