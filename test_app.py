
import unittest
from app import (
    add_student,
    view_students,
    search_student,
    delete_student,
    students
)


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        students.clear()

    # Test Case 1: Add student
    def test_add_student(self):
        result = add_student(1, "Ravi", 85)
        self.assertEqual(result, "Student added successfully")

    # Test Case 2: View students
    def test_view_students(self):
        add_student(2, "Ram", 90)
        self.assertEqual(len(view_students()), 1)

    # Test Case 3: Search student
    def test_search_student(self):
        add_student(3, "Krishna", 80)
        result = search_student(3)
        self.assertEqual(result["name"], "Krishna")

    # Test Case 4: Delete student
    def test_delete_student(self):
        add_student(4, "John", 75)
        result = delete_student(4)
        self.assertEqual(result, "Student deleted successfully")

    # Test Case 5: Invalid marks
    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            add_student(5, "David", 150)


if __name__ == "__main__":
    unittest.main()
