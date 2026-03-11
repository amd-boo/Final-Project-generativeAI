"""
CodeCraftHub - Flask REST API for Course Management
A simple REST API to manage coding courses with JSON file storage.
"""

from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Configuration
COURSES_FILE = 'courses.json'


# ============== Helper Functions ==============

def load_courses():
    """Load courses from JSON file. Returns empty list if file doesn't exist."""
    if not os.path.exists(COURSES_FILE):
        return []
    
    try:
        with open(COURSES_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []


def save_courses(courses):
    """Save courses list to JSON file."""
    try:
        with open(COURSES_FILE, 'w') as file:
            json.dump(courses, file, indent=2)
        return True
    except IOError as e:
        print(f"Error saving courses: {e}")
        return False


def get_next_id(courses):
    """Generate the next available course ID."""
    if not courses:
        return 1
    return max(course['id'] for course in courses) + 1


def get_current_timestamp():
    """Get current timestamp in readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def find_course_by_id(courses, course_id):
    """Find a course by ID. Returns (course, index) or (None, -1) if not found."""
    for index, course in enumerate(courses):
        if course['id'] == course_id:
            return course, index
    return None, -1


def validate_course_data(data, required_fields=None):
    """Validate course data. Returns (is_valid, error_message)."""
    if required_fields is None:
        required_fields = ['name']
    
    if not data:
        return False, "Request body is required"
    
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return False, f"'{field}' is required and cannot be empty"
    
    # Validate status if provided
    valid_statuses = ['Not Started', 'In Progress', 'Completed']
    if 'status' in data and data['status'] not in valid_statuses:
        return False, f"Status must be one of: {', '.join(valid_statuses)}"
    
    # Validate target_date format if provided
    if 'target_date' in data and data['target_date']:
        try:
            datetime.strptime(data['target_date'], "%Y-%m-%d")
        except ValueError:
            return False, "target_date must be in YYYY-MM-DD format"
    
    return True, None


# ============== API Routes ==============

@app.route('/')
def home():
    """Home endpoint with API information."""
    return jsonify({
        "message": "Welcome to CodeCraftHub API",
        "version": "1.0.0",
        "endpoints": {
            "GET /api/courses": "Get all courses",
            "GET /api/courses/<id>": "Get a specific course",
            "POST /api/courses": "Add a new course",
            "PUT /api/courses/<id>": "Update a course",
            "DELETE /api/courses/<id>": "Delete a course",
            "GET /api/courses/stats": "Get course statistics",
            "GET /api/courses/search?q=term": "Search courses
