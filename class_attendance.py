import pprint

#Approach 1
attendance_list = [
    {
        "student_id": "001",
        "student_name": "John Doe",
        "lecture_id": "001",
        "attendance": True
    }
]

def mark_attendance(student_id: str, student_name: str, lecture_id: str, attendance: bool = True):
    attendance_list.append({
        "student_id": student_id,
        "student_name": student_name,
        "lecture_id": lecture_id,
        "attendance": attendance
    })

def get_attendance(student_id, lecture_id):
    for attendance in attendance_list:
        if attendance["student_id"] == student_id and attendance["lecture_id"] == lecture_id:
            return attendance
    return None


#Approach 2
class AttendanceList:
    """AttendanceList class to manage attendance for a lecture"""
    def __init__(self, lecture_id: str):
        self.lecture_id = lecture_id
        self.attendance_list = []
        pass

    def mark_attendance(self, student_id: str, student_name: str, attendance: bool = True) -> None:
        """Mark attendance for a student
        
        Args:
            student_id (str): Student ID
            student_name (str): Student name
            attendance (bool, optional): Attendance status. Defaults to True.

        Returns:
            None
        """
        self.attendance_list.append({
            "student_id": student_id,
            "student_name": student_name,
            "attendance": attendance
        })

    def get_attendance(self, student_id):
        """Get attendance for a student

        Args:
            student_id (str): Student ID

        Returns:
            dict: Attendance record
        """
        for attendance in self.attendance_list:
            if attendance["student_id"] == student_id:
                return attendance
        return None
    

if __name__ == "__main__":
    # Initialize the AttendanceList class
    attendance_list = AttendanceList("001")

    # Mark attendance for students
    attendance_list.mark_attendance("001", "John Doe", True)
    attendance_list.mark_attendance("002", "Jane Doe", False)
    pprint.pp(attendance_list.attendance_list)