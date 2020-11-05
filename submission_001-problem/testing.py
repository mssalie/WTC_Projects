

def create_outline():
    """
    TODO: implement your code here
    """
    #step 1 - set

    print("Course Topics:")
    
    course_set = set(["Introduction to Python","Tools of the Trade",
    "How to make decisions", "How to repeat code",
    "How to structure data", "Functions","Modules"])

    for course_topics in course_set:
        print("* " + course_topics)

    #step 2 - mapping

    problems = ["Problem 1, ", "Problem 2, ", "Problem 3, "]
    joint_probs = "".join(problems)

    dictionary_problems = {}
    dictionary_problems["Introduction to Python:"] = joint_probs
    dictionary_problems["Tools of the Trade:"] = joint_probs
    dictionary_problems["How to make decisions:"] = joint_probs
    dictionary_problems["How to repeat code:"] = joint_probs
    dictionary_problems["How to structure data:"] = joint_probs
    dictionary_problems["Functions:"] = joint_probs
    dictionary_problems["Modules:"] = joint_probs

    for i in dictionary_problems:
        print(i, dictionary_problems[i], sep = " : ")


if __name__ == "__main__":
    create_outline()
