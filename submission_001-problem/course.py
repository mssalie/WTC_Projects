
def create_outline():
    """
    TODO: implement your code here
    """

    def sorted_func(index): #function to sort specific index
        return index[4]
    
    #step 1 

    print("Course Topics:")
    
    course_set1 = set(["Introduction to Python","Introduction to Python", "Tools of the Trade"])
    course_set2 = set(["How to make decisions", "How to repeat code", "How to structure data"])
    course_set3 = set(["Functions","Modules"])
    course_set = course_set1|course_set2|course_set3

    course_list = ["Introduction to Python","Tools of the Trade",   #step 4 - putting all info in alphabetical order
    "How to make decisions", "How to repeat code",
    "How to structure data", "Functions","Modules"]
    
    sorted_course_list = sorted(course_list)
    joint_sorted_course_list = "\n* ".join(sorted_course_list)
    print("*", joint_sorted_course_list)

    #step 2 

    print("Problems:")

    problems = ["Problem 1, ", "Problem 2, ", "Problem 3 "]
    joint_probs = "".join(problems)

    dictionary_problems = {}
    dictionary_problems["* Introduction to Python"] = joint_probs
    dictionary_problems["* Tools of the Trade"] = joint_probs
    dictionary_problems["* How to make decisions"] = joint_probs
    dictionary_problems["* How to repeat code"] = joint_probs
    dictionary_problems["* How to structure data"] = joint_probs
    dictionary_problems["* Functions"] = joint_probs
    dictionary_problems["* Modules"] = joint_probs

    for i in dictionary_problems:
        print(i, dictionary_problems[i], sep = " : ")

    #step 3

    print("Student Progress:")

    student1 = ("2. ", "Jzuma - ", "Introduction to python -", "Problem 2 ", "[GRADED]")
    student2 = ("3. ", "Jmalema - ", "How to make decision -", "Problem 1 ", "[COMPLETED]")
    student3 = ("1. ", "Jcena - ", "Functions -", "Problem 3 ", "[STARTED]")

    list_students = (student1, student2, student3)
    
    list_students = sorted(list_students, key = sorted_func, reverse = True) #step 4 - sorting status

    for students in range(0,3):
        for j in range(0,5):
            print(list_students[students][j], end = "")
        print()

if __name__ == "__main__":
    create_outline()
