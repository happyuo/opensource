def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 학생 수와 과목 수 설정
num_students = 5
num_subjects = 3

# 학생들의 정보를 저장할 리스트 초기화
students = []

# 학생 정보 입력 받기
for i in range(num_students):
    print(f"학생 {i+1}의 성적을 입력하세요:")
    student_scores = []
    print("영어 성적 입력: ", end="") # 출력이 같은 줄에 나오게 하기 위해 end="" 사용
    english_score = int(input())
    student_scores.append(english_score)
    print("C-언어 성적 입력: ", end="")
    c_score = int(input())
    student_scores.append(c_score)
    print("파이썬 성적 입력: ", end="")
    python_score = int(input())
    student_scores.append(python_score)
    students.append(student_scores)

# 총점, 평균, 학점 계산
for i in range(num_students):
    total_score = sum(students[i])
    average_score = total_score / num_subjects
    grade = calculate_grade(average_score)
    students[i].append(total_score)
    students[i].append(average_score)
    students[i].append(grade)

# 등수 계산
ranks = [1] * num_students  # 각 학생의 초기 등수를 1로 설정
for i in range(num_students):
    for j in range(num_students):
        if students[i][-2] < students[j][-2]:  # 평균 점수를 비교하여 등수를 증가시킴
            ranks[i] += 1

# 학생들의 정보에 등수 추가
for i in range(num_students):
    students[i].append(ranks[i])

# 결과 출력
print("학생 성적표:")
print("번호  영어  C언어  파이썬  총점  평균 학점 등수")
for i in range(num_students):
    print(f"{i+1}\t\t{students[i][0]}\t{students[i][1]}\t\t{students[i][2]}\t\t{students[i][3]}\t{students[i][4]:.2f}\t{students[i][5]}\t{students[i][6]}")
