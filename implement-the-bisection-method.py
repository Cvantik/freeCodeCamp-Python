def square_root_bisection(number: float, tolerance = 0.01, iterations = 8):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    if number == 0 or number == 1:
        print (f"The square root of {number} is {number}")
        return number
    
    low: float = 0
    high: float = max(1, number)
    success = False

    for i in range(iterations):
        mid: float = (low + high) / 2

        if (high - low) < tolerance:
            success = True
            break
            
        elif mid**2 > number:
            high = mid
        else:
            low = mid

    if success == True:
        print(f"The square root of {number} is approximately {mid}")
        return mid
    else:
        print(f"Failed to converge within {iterations} iterations")
        return None