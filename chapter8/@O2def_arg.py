# def find_primes(start,end):/

# Function to check whether a number is prime or not
def prim(strt,end):
    if strt>1:
        for num in range(strt,end+1):
            is_prme=True            # Assume the number is prime
            iteration_count = 0  # Count iterations

            for i in range(2,int(num**0.5)+1):
                iteration_count += 1
                if num%i==0:
                    is_prme=False
                    break
            print(f"Checked {iteration_count} divisors for {num}")

            if is_prme:
                print(num, "is a prime number")
            else:
                print(num, "is not a prime number")
    else:
        print("Start value should be greater than 1")

prim(1000000,1000000)