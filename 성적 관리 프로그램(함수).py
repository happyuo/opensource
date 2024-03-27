# 학점계산 함수
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
subjects = ["영어", "C-언어", "파이썬"]

students = []
student_scores = []

# 입력 함수
def input_scores(i):
    student_id = input("학번: ")
    student_name = input("이름: ")
    student_scores.append([])
    print("점수를 입력하세요:")
    for j in range(num_subjects):
        score = int(input(subjects[j] + ": "))
        student_scores[i].append(score)
    students.append([student_id, student_name])

# 총점, 평균, 학점 계산함수
def calculate(i):
    total_score = sum(student_scores[i])
    average_score = total_score / num_subjects
    grade = calculate_grade(average_score)
    students[i].extend([total_score, average_score, grade])

# 등수 계산함수
def calculate_rank():
    ranks = [1] * num_students  # 각 학생의 초기 등수를 1로 설정
    for i in range(num_students):
        for j in range(num_students):
            if students[i][-3] < students[j][-3]:  # 평균 점수를 비교하여 등수를 증가시킴
                ranks[i] += 1
    # 학생들의 정보에 등수 추가
    for i in range(num_students):
        students[i].append(ranks[i])

# 출력함수
def print_results():
    print("\t\t\t\t\t성적관리 프로그램\t\t\t\t")
    print("==================================================================")
    print("학번\t\t이름\t\t", end="")
    for subject in subjects:
        print(subject + "\t\t", end="")
    print("총점\t\t평균\t\t학점\t\t등수")
    for student in students:
        print(student[0], student[1], end="\t")  # 학번과 이름 출력
        for score in student_scores[students.index(student)]:  # 과목 성적 출력
            print(score, end="\t\t")
        # 총점, 평균, 학점, 등수 출력
        print(student[-4],end="\t\t")
        print("{:.1f}".format(student[-3]), end="\t\t")
        print(student[-2], student[-1], end="\t\t\t")
        print()  # 다음 줄로 넘어감

# 메인 함수
def main():
    for i in range(num_students):
        input_scores(i)
        calculate(i)
    calculate_rank()
    print_results()

if __name__ == "__main__":
    main()
