import Professor
import Student
import UndergraduateCourse
import GraduateCourse
import HwAssignment
import InClassAssignment

def main():
    prof = Professor.Professor('John','099337755')
    print(prof.contact_info)
    print(prof.courses)
    prof2 = Professor.Professor('Sam','055664455')
    student = Student.Student('Helen','091555688')
    student2 = Student.Student('Mia','092555933')

    python_course = UndergraduateCourse.UndergraduateCourse('python:intro',prof,'introduction',25,3)
    applied_statistics = GraduateCourse.GraduateCourse('statistics',prof2,'deep examination of statistics',30,'statistical testing')

    prof.teach_course(python_course)
    print(prof.courses)

    student.enroll_in_course(python_course)
    student2.enroll_in_course(applied_statistics)

    solve_problems = HwAssignment.HwAssignment('problem solving','solve 1-10 problems')
    python_course.add_assignment(solve_problems)
    student.submit_assignment(solve_problems)

    other_problems = InClassAssignment.InClassAssignment('pss','solve 3rd problem',100)
    applied_statistics.add_assignment(other_problems)
    student2.submit_assignment(other_problems)

    student.view_progress(python_course)
    student2.view_progress(applied_statistics)

    applied_statistics.ensure_to_pass()

main()

###