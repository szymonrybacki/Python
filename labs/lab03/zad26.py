class StudentRegistry:
    def __init__(self):
        self.students = {}  # Słownik przechowujący studentów i ich oceny
    
    def add_student(self, name):
        if name not in self.students:
            self.students[name] = []
            print(f"Dodano studenta: {name}")
            return True
        else:
            print(f"Student {name} już istnieje")
            return False
    
    def add_grade(self, name, grade):
        if name not in self.students:
            print(f"Student {name} nie istnieje")
            return False
        
        try:
            grade_value = float(grade)
            if 2.0 <= grade_value <= 5.0:
                self.students[name].append(grade_value)
                print(f"Dodano ocenę {grade} dla studenta {name}")
                return True
            else:
                print("Ocena musi być w zakresie 2.0-5.0")
                return False
        except ValueError:
            print("Nieprawidłowy format oceny")
            return False
    
    def get_grades(self, name):
        if name in self.students:
            return self.students[name]
        return None
    
    def print_all_students(self):
        print("Lista studentów:")
        for name, grades in self.students.items():
            avg = sum(grades) / len(grades) if grades else 0
            print(f"{name}: oceny {grades}, średnia: {avg:.2f}")

# Test klasy
if __name__ == "__main__":
    rejestr = StudentRegistry()
    
    rejestr.add_student("Jan Kowalski")
    rejestr.add_student("Anna Nowak")
    rejestr.add_student("Piotr Wiśniewski")
    
    rejestr.add_grade("Jan Kowalski", 4.0)
    rejestr.add_grade("Jan Kowalski", 5.0)
    rejestr.add_grade("Anna Nowak", 3.5)
    rejestr.add_grade("Nieistniejący Student", 4.0)  # Próba dodania oceny dla nieistniejącego studenta
    
    rejestr.print_all_students()