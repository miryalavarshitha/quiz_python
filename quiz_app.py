import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",    # replace with your MySQL username
        password="root",  # replace with your MySQL password
        database="quiz_db"
    )

def get_questions():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    conn.close()
    return questions

def take_quiz():
    questions = get_questions()
    score = 0

    for q in questions:
        print(f"\n{q['question']}")
        print(f"A: {q['option_a']}")
        print(f"B: {q['option_b']}")
        print(f"C: {q['option_c']}")
        print(f"D: {q['option_d']}")
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['correct_answer']}.")

    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    take_quiz()  # Start the quiz
