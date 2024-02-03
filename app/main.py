from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students = list[Student]


def write_groups_information(groups: list[Group]):
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]):
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information(filename: str):
    with open(filename, "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    specialties = []
    for group in groups:
        specialties.append(group.specialty)
    return set(specialties)

def read_students_information(filename: str):
    with open(filename, "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students

