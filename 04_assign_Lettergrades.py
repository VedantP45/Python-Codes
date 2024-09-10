def letter_grades(highest):
   
    interval = (highest - 40) // 4
    
    thresholds = [41 + i * interval for i in range(4)]
    return thresholds


print(letter_grades(100))  
print(letter_grades(88))   
