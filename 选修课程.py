classmates=['刘达','王尔','张鹏','陈思','张悟']
courses=['高等数学','高等代数','python程序设计','学术英语','美国社会与文化','大学生英语交流']

grade1={'刘达':90,'王尔':89,'张鹏':79,'陈思':98,'张悟':99} #高等数学
grade2={'刘达':77,'王尔':96,'张鹏':74,'陈思':95,'张悟':54} #高等代数
grade3={'刘达':77,'王尔':70,'张鹏':69,'陈思':91,'张悟':100} #python程序设计
grade4={'刘达':95,'王尔':78,'张鹏':97} #学术英语
grade5={'陈思':76,'张悟':77} #美国社会与文化
grade6={'刘达':100,'王尔':89,'张鹏':87,'陈思':97,'张悟':98} #大学生英语交流
grades_course=[grade1,grade2,grade3,grade4,grade5,grade6]

student1,student2,student3,student4,student5={},{},{},{},{}
grades_student=[student1,student2,student3,student4,student5]

for i in range(len(classmates)):
    for j in range(len(courses)):
        if grades_course[j].get(classmates[i]):#用get不用grade[k]
            grades_student[i][courses[j]]=grades_course[j].get(classmates[i])
            
for i in range(len(classmates)):
    print(classmates[i]+'选修了'+str(len(grades_student[i]))+'门课程:')
    for j in range(len(courses)):
        if grades_student[i].get(courses[j]):
            print('\t'+courses[j]+':'+str(grades_student[i].get(courses[j])))


