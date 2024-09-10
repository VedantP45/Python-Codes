def student_ranking(student_scores, student_names):
    
    ranking = [f"{i+1}. {name}: {score}" for i, (score, name) in enumerate(zip(student_scores, student_names))]
    return ranking

# Test cases
student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names = ['Ved', 'Krishna', 'Jeet', 'Harshil', 'Akhilesh', 'Karan', 'Pratik']
print(student_ranking(student_scores, student_names))
# Output: ['1. Aditya: 100', '2. Leslie: 99', '3. Vinayak: 90', '4. Shivam: 84', '5. Abhilash: 66', '6. Karan: 53', '7. Vishnu: 47']
