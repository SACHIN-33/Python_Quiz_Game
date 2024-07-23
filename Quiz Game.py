def run_quiz():
    print("Welcome to the Tamil Nadu Quiz!")
    print("---------------------------------")
    
    # List of questions, options, and answers
    questions = [
        {
            "question": "1. Which city is the capital of Tamil Nadu?",
            "options": ["Chennai", "Madurai", "Coimbatore", "Tiruchirappalli"],
            "answer": "Chennai"
        },
        {
            "question": "2. Which is the state flower of Tamil Nadu?",
            "options": ["Lotus", "Kanikonna", "Neelakurinji", "Jasmine"],
            "answer": "Jasmine"
        },
        {
            "question": "3. Which is the longest river in Tamil Nadu?",
            "options": ["Kaveri", "Vaigai", "Palar", "Thamirabarani"],
            "answer": "Kaveri"
        },
        {
            "question": "4. What is the traditional dance form of Tamil Nadu?",
            "options": ["Bharatanatyam", "Kuchipudi", "Kathakali", "Mohiniyattam"],
            "answer": "Bharatanatyam"
        },
        {
            "question": "5. Who was the first woman Chief Minister of Tamil Nadu?",
            "options": ["Indira Gandhi", "J. Jayalalithaa", "Sonia Gandhi", "M. Karunanidhi"],
            "answer": "J. Jayalalithaa"
        }
    ]
    
    score = 0
    
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        
        user_answer = input("Enter your answer (1/2/3/4): ").strip().capitalize()
        
        # Check if the answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")
        
        print("-------------------------")
    
    print(f"You scored {score} out of {len(questions)}.")

if __sachin__ == "__main__":
    run_quiz()
