
 #!/usr/bin/env python3

if __name__ == '__main__':

    def get_grade(mark):
        if mark >= 70:
            return 'A'
        elif mark > 60:
            return 'B'
        elif mark > 50:
            return 'C'
        elif mark > 40:
            return 'D'
        else:
            return 'F'

    def get_marks():
        marks = []
        while True:
            user_input = input("Enter a mark (or press Enter to finish): ")
            if user_input == "":
                break
            try:
                mark = float(user_input)
                if 0 <= mark <= 100:
                    marks.append(mark)
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        return marks  # Return the marks list

    def display_results(marks):
        if marks:
            mean = sum(marks) / len(marks)
            print(f"Highest mark: {max(marks)}")
            print(f"Lowest mark: {min(marks)}")
            print(f"Mean mark: {mean:.2f}")
            print(f"Grade: {get_grade(mean)}")
        else:
            print("No marks entered.")


    display_results(get_marks()) # Run the program









