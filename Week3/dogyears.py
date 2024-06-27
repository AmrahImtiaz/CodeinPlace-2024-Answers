# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    try:
        age_human_years = float(input("Enter an age in calendar years: "))
        age_dog_years = age_human_years * DOG_YRS_MULTIPLIER
        print(f"That's {age_dog_years} in dog years!")  # Display the entire float
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()
