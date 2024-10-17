name = str(input("Name: "))
sec = str(input("Section: "))

prelim = float(input("Enter the Preliminary Period Grade: "))
midterm = float(input("Enter the Midterm Period Grade: ")) 
finals = float(input("Enter the Final Period Grade: "))        
final_grade = round((prelim * 0.3333) + (midterm * 0.3333) + (finals * 0.3333))
            
if 99 <= final_grade <= 100:
    grade_points = 1.00      
elif 96 <= final_grade <= 98:
    grade_points = 1.25
elif 93 <= final_grade <= 95:
    grade_points = 1.50
elif 90 <= final_grade <= 92:
    grade_points = 1.75
elif 87 <= final_grade <= 89:
    grade_points = 2.00
elif 84 <= final_grade <= 86:
    grade_points = 2.25
elif 81 <= final_grade <= 83:
    grade_points = 2.50
elif 78 <= final_grade <= 80:
    grade_points = 2.75
elif 75 <= final_grade <= 77:
    grade_points = 3.00
else:
    print("Your Grade is below 75, You Failed.")

                
print(f"Final Grade: {final_grade}")
print(f"Grade Points: {grade_points}")
            