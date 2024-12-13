from modules.input_module import get_numbers
from modules.processing_module import add, subtract, multiply, divide
from modules.output_module import print_result, append_to_file

def main():
   
    num1, num2 = get_numbers()

   
    sum_result = add(num1, num2)
    diff_result = subtract(num1, num2)
    prod_result = multiply(num1, num2)
    quot_result = divide(num1, num2)

    
    print_result("sum", num1, num2, sum_result)
    append_to_file("sum", num1, num2, sum_result)

    print_result("difference", num1, num2, diff_result)
    append_to_file("difference", num1, num2, diff_result)

    print_result("product", num1, num2, prod_result)
    append_to_file("product", num1, num2, prod_result)

    print_result("quotient", num1, num2, quot_result)
    append_to_file("quotient", num1, num2, quot_result)

if __name__ == "__main__":
    main()
