def calculate_grade(mark):
    """Calculate the grade based on the mark."""
    if mark >= 70:
        return "Distinction"
    elif mark >= 60:
        return "Merit"
    elif mark >= 40:
        return "Pass"
    else:
        return "Fail"

def validate_data(mark, weight, total_weight):
    """Validate the mark and weight data."""
    if not (0 <= mark <= 100):
        raise ValueError(f"Mark {mark} is invalid. Must be between 0 and 100")
    if total_weight > 100:
        raise ValueError(f"Total weight exceeds 100%")
    return True

def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            # Write header to output file
            f_out.write("Name, Mark, Grade\n")
            
            current_student = None
            weighted_sum = 0
            total_weight = 0
            
            for line in f_in:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                    
                if ',' not in line:  # This is a student name
                    # Process previous student if exists
                    if current_student and total_weight == 100:
                        final_mark = round(weighted_sum, 1)
                        grade = calculate_grade(final_mark)
                        f_out.write(f"{current_student}, {final_mark}, {grade}\n")
                    
                    # Reset for new student
                    current_student = line
                    weighted_sum = 0
                    total_weight = 0
                else:
                    # Process unit data
                    unit, mark, weight = [x.strip() for x in line.split(',')]
                    mark = float(mark)
                    weight = int(weight)
                    
                    # Validate data
                    validate_data(mark, weight, total_weight + weight)
                    
                    # Calculate weighted mark
                    weighted_sum += (mark * weight / 100)
                    total_weight += weight
            
            # Process last student
            if current_student and total_weight == 100:
                final_mark = round(weighted_sum, 1)
                grade = calculate_grade(final_mark)
                f_out.write(f"{current_student}, {final_mark}, {grade}\n")
                
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except ValueError as e:
        print(f"Error processing data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_file = "students.txt"
    output_file = "results.txt"
    process_student_data(input_file, output_file)
    print("Processing complete. Check results.txt for output.")
