from calc_func import do_add, do_sub
from multiply import do_mul
from area import cal_area_rec

def main():

    print("Welcom to Calculator")
    print("""
          \nSelect the function from the given options 
          1. Add
          2. Subtract
          3. Multiply
          4. Area of rectangle
          """)
    
    user_input = input("Select the function")

    a = int(input("Value of A "))
    b = int(input("Value of B "))

    if user_input == "1":
        result = do_add(a, b)
    elif user_input == "2":
        result = do_sub(a, b)
    elif user_input == "3":
        result = do_mult(a, b)
    elif user_input == "4":
        result = cal_area_rec(a, b)
    
    return print("Result: ", result)

if __name__ == "__main__":
    main()