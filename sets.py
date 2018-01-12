songs = {"Milligram Smile", "No Trivia", "Hang The Mason"}

songs.add("Treehouse Hula")

songs.update({"Python Two-Step", "Ruby Rhumba"},{"My PDF Files"})

#print(songs)

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topic):
    list = []
    for course in COURSES:
        if topic.intersection(COURSES[course]):
            list.append(course)
    return list

#print(covers({"Python"}))

def covers_all(topic):
    list = []
    for course in COURSES:
        if topic.intersection(COURSES[course]) == topic:
            list.append(course)
    return list

print(covers_all({'conditions', 'input'}))

