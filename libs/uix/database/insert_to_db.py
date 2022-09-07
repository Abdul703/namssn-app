import sqlite3


conn = sqlite3.connect("database")
c = conn.cursor()


def insert_courses():
    '''insert all courses offered in maths department to the database
    in form of "code" "title" "unit" "type"'''
    l = [
        ["MAT 111", "algebra", "2", "C"],
        ["MAT 112", "Trigonometry", "1", "C"],
        ["MAT 113", "History of Maths", "1", "C"],
        ["MAT 114", "Static", "1", "C"],
        ["MAT 121", "Differential Calculus", "2", "C"],
        ["MAT 122", "Co-ordinate Geometry", "1", "C"],
        ["MAT 123", "Mathematics Methodology", "1", "C"],
        ["MAT 124", "Mathematics Labratory Practical", "1", "C"],
        ["MAT 125", "Introduction To Computer", "1", "E"],
        ["MAT 211", "Integral Calculus", "2", "C"],
        ["MAT 212", "Problem Solving", "1", "C"],
        ["MAT 213", "Number Theory", "1", "C"],
        ["MAT 214", "Probability", "2", "C"],
        ["MAT 221", "Dynamics", "1", "C"],
        ["MAT 222", "Vector Analysis I", "2", "C"],
        ["MAT 223", "Real Analysis", "1", "C"],
        ["MAT 224", "JSS Content", "1", "C"],
        ["MAT 225", "Research Methodology", "1", "C"],
        ["MAT 321", "Statics", "1", "C"],
        ["MAT 322", "Linear Algebra", "1", "C"],
        ["MAT 323", "Real Analysis II", "2", "E"],
        ["MAT 324", "Abstract Algebra", "1", "E"],
        ["MAT 325", "Differential Equations", "1", "C"],
    ]

    c.executemany("INSERT INTO courses VALUES(?, ?, ?, ?)", l)
    conn.commit()


def insert_lecturers():
    """insert lectures information to the database in form of
    code(image name), fullname, phone number and rank"""
    l = [
        [
            "li",
            "Mal. Liman Muhammad",
            "Head Of Department",
            "08065647929"
        ],
        [
            "al",
            "Mal. Alhassan Isah Diadia",
            "Former Head of Department",
            "07069438305"
        ],
        [
            "ab",
            "Dr Abdullahi Moh'd Baba",
            "Former HOD Mathematics",
            "08036380231"
        ],
        [
            "ma",
            "Dr Mahmud Mamman",
            "MIS Director",
            "08035233762"
        ],
        [
            "ab1",
            "Mal.Abubakar sadiq Ndagara",
            "School Of Science Exam Officer",
            "07034867874",
        ],
        [
            "um",
            "Dr Umar Chado",
            "Former Dean School of Science",
            "08069452706"
        ],
        [
            "ah",
            "Dr Ahmad Umar Manko",
            "Dept Exam Officer/Namssn Patron",
            "08065386808"
        ],
        [
            "ba",
            "Dr Bala Abubakar",
            "Maths TP Coordinator",
            "08020382464"
        ],
        [
            "ha",
            "Dr Hassan Usman",
            "Exam Officer LVSP Programme",
            "08065651578"
        ],
    ]

    c.executemany("INSERT INTO lecturers VALUES(?, ?, ?, ?)", l)
    conn.commit()


def insert_excos():
    """insert excos information to the database in form of
    code(image name), fullname, phone number and rank"""
    l = [
        [
            "sa",
            "Comrade Sadiq Yunusa",
            "President",
            "09037631817"
        ],
        [
            "na", "Comrade Nafisat Abdulsalam",
            "Vice President",
            "08147182403"
        ],
        [
            "id",
            "Comrade Idris Ahmad Enagi",
            "Sectary General",
            "08130249263"
        ],
        [
            "ak",
            "Comrade Akinbinu Mobolaji",
            "Assist Sectary General",
            "08144746943"
        ],
        [
            "ab",
            "Comrade AbdulAzeez Nuhu",
            "Research Director",
            "08062291995"
        ],
        [
            "ag",
            "Comrade Agnes Amina Shaba",
            "Treasurer",
            "08148191959"
        ],
        [
            "ra",
            "Comrade Rahama Abubakar Rogan",
            "Financial Sectary",
            "09030684169"
        ],
        [
            "he",
            "Comrade Helen Chigozie Oseji",
            "Assistant Financial Sectary",
            "08170243529",
        ],
        [
            "ro",
            "Comrade Rofiat Ibrahim Adewumi",
            "Auditor General",
            "09031518800"],
        [
            "mu",
            "Comrade Muhammad Musa Koroka",
            "Public Relation Officer I (PRO I)",
            "08137995017",
        ],
        [
            "ab1",
            "Comrade Abdullahi Hammed",
            "Public Relation Officer II (PRO II)",
            "07053390581",
        ],
        [
            "ab2",
            "Comrade Abubakar Sadik Sonfada",
            "Director of Social",
            "09065683185"
        ],
        [
            "um",
            "Comrade Umar Mahmud",
            "Director of Sport",
            "07069438305"
        ],
        [
            "ha",
            "Comrade Halima Musa",
            "Welfare Director",
            "09078372303"
        ],
    ]

    c.executemany("INSERT INTO excos VALUES(?, ?, ?, ?)", l)
    conn.commit()


def insert_sras():
    """insert SRAs information to the database in form of
    code(image name), fullname, phone number and rank"""
    l = [
        [
            "ab",
            "Senator Abdurrazak Suleiman",
            "Senate President",
            "08101014336"
        ],
        [
            "ib",
            "Senator Ibrahim Muh'd Sheikh",
            "Deputy Senate President",
            "08144982482",
        ],
        [
            "mu",
            "Senator Muhammad Aliyu Liman",
            "Clerk",
            "09063301382"
        ],
        [
            "al",
            "Senator Almustafa Usman",
            "Chief Whip",
            "08065607203"
        ],
        [
            "pa",
            "Senator Patrick Aondongusha",
            "Senator 200 Level",
            "09030931637"
        ],
        [
            "mu1",
            "Senator Mujaheed Ahmad",
            "Senator 100 Level",
            "0805726117"
        ],
    ]

    c.executemany("INSERT INTO sras VALUES(?, ?, ?, ?)", l)

    conn.commit()


insert_courses()
insert_excos()
insert_sras()
insert_lecturers()

conn.close()
