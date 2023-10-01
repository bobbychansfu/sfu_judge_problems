def main():
    # Input: Desired Number
    desired_num = int(input("Enter the desired number: "))
    
    # Input: Type of multiples - even/odd
    multiple_type = input("Enter the type you want (even/odd): ").strip().lower()
    
  
    # Input: Number of multiples
    num_multiples = int(input("Enter the number of multiples you want: "))
    

    # Calculating and displaying multiples
    print(f"Here are the first {num_multiples} {multiple_type} multiples of {desired_num}:")
    
    count = 1
    multiple = 0
    
    while count < num_multiples+1:
        
        if multiple_type == 'even':
            print(2*count*desired_num)
            count += 1
        else:
            print((2*count-1)*desired_num)
            count += 1


if __name__ == "__main__":
    main()
