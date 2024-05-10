from calc_func import do_add, do_sub

def main():

    print("Welcom to Calculator")
    print("""
          \nSelect the function from the given options 
          1. Add
          2. Subtract
          """)
    
    user_input = input("Select the function")

    a = int(input("Value of A "))
    b = int(input("Value of B "))

    if user_input == "1":
        result = do_add(a, b)
    else:
        result = do_sub(a, b)
    
    return print("Result: ", result)

if __name__ == "__main__":
    main()