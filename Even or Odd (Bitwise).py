def even_or_add(n=int(input())):
    # Time Complexity = O(1) 
    
    if n&1:
        print("Odd")
    else:
        print("Even")

even_or_add()
