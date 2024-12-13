# Description: A program which compiles the codes of the first 5 projects into functions and creates a menu for the user to choose which program they want to run.
# Author: Chris Morrison, Group 9
# Date: June 24, 2024
# Version: 1.0

# Libraries
import datetime
import random
import string
import collections
import statistics



def NL_chocolate_company():

# Description: A program for NL Chocolate Company to process salesperson travel claims.
# Author: Steve Morrison Group 9
# Date(s) 2024-06-17

# Define program constants.

    HST_RATE = 0.15
    KM_RATE = 0.17
    OVER_1000_KM_RATE = 0.04
    BONUS_3_DAYS = 100.00
    BONUS_EXEC = 45.00
    BONUS_DEC = 50.00

    # Main program starts here.

    while True:

        # Gather user inputs.

        while True:
            EmpNum = input("Enter the employee number (): ") 
            if EmpNum == "":
                print("Data Entry Error - Employee Number cannot be blank.")
            elif len(EmpNum) != 5:
                print("Data Entry Error - Phone Number must be 5 characters.")
            else: 
                break

        EmpFirstName = input("Enter employee first name: ").title()
        EmpLastName = input("Enter employee last name: ").title()
        TripLoc = input("Enter the location of the trip: ").title()
        
        while True:
            try:
                TripStartDate = input("Enter the start date (YYYY-MM-DD): ")
                TripStartDate = datetime.datetime.strptime(TripStartDate, "%Y-%m-%d")
            except:
                print("Data Entry Error - start date is not a valid format.")
            else:
                break
    
        while True:
            try:
                TripEndDate = input("Enter the end date (YYYY-MM-DD): ")
                TripEndDate = datetime.datetime.strptime(TripEndDate, "%Y-%m-%d")
            except:
                print("Data Entry Error - end date is not a valid format.")
            else:
                if TripEndDate < TripStartDate:
                    print("Data Entry Error - trip end date must be a later date than the start date.")
                elif (TripEndDate - TripStartDate).days > 7:
                    print("Data Entry Error - trip end date musst not be more than 7 days later than the start date")
                else:
                    break
        
        while True:
            OwnRent = input("Did the salesperson use their own car or rent a car?(O/R): ").upper()
            if OwnRent != "O" and OwnRent != "R":
                print("Data Entry Error - input must only be O or R")
            elif OwnRent == "O":
                while True:
                    try:
                        TotalKM = int(input("Enter the total number of kilometres driven during the trip: "))
                        if TotalKM > 2000:
                            print("Data Entry Error - total number of kilometres cannot exceed 2000")
                        else:
                            break
                    except:
                        print("Data Entry Error - total kilometres must only be a number")
                break
            else:
                TotalKM = 0
                break

        ClaimType = input("Enter claim type (S/E): ").upper()

        # Perform required calculations.

        NumDays = (TripEndDate - TripStartDate).days

        # Calculate the per diem amount based on car owned or rented.

        if OwnRent == "O":
            DayRate = 85.00
        else:
            DayRate = 65.00
        
        PerDiemAmt = NumDays * DayRate

        # Calculate the bonus.

        Bonus = 0.00

        if OwnRent == "O":
            MileageAmt = TotalKM * KM_RATE
        else:
            MileageAmt = 0

        if NumDays > 3: 
            Bonus += BONUS_3_DAYS
        if OwnRent == "O" and TotalKM > 1000:
            Bonus += TotalKM * OVER_1000_KM_RATE
        if ClaimType == "E":
            Bonus += NumDays * BONUS_EXEC
        if TripStartDate.month == 12 and TripStartDate.day >= 15 and TripStartDate.day <= 22:
            Bonus += NumDays * BONUS_DEC
        

        # Calculate the total claim amount
        
        ClaimAmt = PerDiemAmt + MileageAmt + Bonus
        HST = ClaimAmt * HST_RATE

        ClaimTotal = ClaimAmt + HST

        # Display Results

        PerDiemAmtDsp = "${:,.2f}".format(PerDiemAmt)
        MileageAmtDsp = "${:,.2f}".format(MileageAmt)
        BonusDsp = "${:,.2f}".format(Bonus)
        ClaimAmtDsp = "${:,.2f}".format(ClaimAmt)
        HSTDsp = "${:,.2f}".format(HST)
        ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)
        TripStartDateDsp = TripStartDate.strftime("%Y-%m-%d").upper()
        TripEndDateDsp = TripEndDate.strftime("%Y-%m-%d").upper()

        print(f"Employee Number: {EmpNum}")
        print(f"Employee Name: {EmpFirstName} {EmpLastName}")
        print()
        print(f"Trip Location: {TripLoc}")
        print(f"Trip Start Date: {TripStartDateDsp}")
        print(f"Trip End Date: {TripEndDateDsp}")
        
        if OwnRent == "O":
            print("Did emplyee use own car? Yes")
            print(f"Total kilometres: {TotalKM}km")
        else:
            print("Did employee use own car? No")
        
        if ClaimType == "S":
            print("Claim Type: Standard")
        else:
            print("Claim Type: Executive")

        print(f"Trip Number of Days: {NumDays}")
        print(f"Per Diem Amount: {PerDiemAmtDsp}")

        if OwnRent == "O":
            print(f"Mileage Amount: {MileageAmtDsp}")
        
        print(f"Bonus Amount: {BonusDsp}")
        print(f"Claim Amount: {ClaimAmtDsp}")
        print(f"HST: {HSTDsp}")
        print(f"Claim Total: {ClaimTotalDsp}")
        
        while True:
            Continue = input("Do you want to enter another employee claim? (Y / N): ").upper()

            if Continue != "Y" and Continue != "N":
                print("Data Entry Error - prompt to continue must be a Y or an N.")
            else:
                break
        
        if Continue == "N":
            break

def fizz_bizz():

# Description: This program solves the FizzBizz problem. The task is to print numbers from 1 to 100. However, for multiples of five, it prints "Fizz" 
#              and for multiples of eight, it prints "Bizz." For numbers which are multiples of both five and eight, it prints "FizzBizz."
# Author: Steve Morrison Group 9
# Date(s) 2024-06-18

    n = 1
    while True:
        if n > 100:
            break
        if n % 5 == 0 and n % 8 == 0:
            print("FizzBizz")
        elif n % 5 == 0:
            print("Fizz")
        elif n % 8 == 0:
            print("Bizz")
        else:
            print(n)

        n += 1

def membership_card():

# Description: A program designed to manage membership information and generate membership card for a hypothetical organization "TECHTITANS". 
# Author: Steve Morrison Group 9
# Date(s) 2024-06-19 - 2024-06-21

    # Define program constants

    RENEW_FEE = 50.00
    RENEW_DISCOUNT = 5.00
    FIVE_YEAR_DISCOUNT = 10.00
    HST_RATE = 0.15

    # Define program functions.

    def PasswordGenerator(MemberBirthDate):

        BirthMonth = MemberBirthDate.strftime("%m")
        Birthday = MemberBirthDate.strftime("%d")

        PSWDUpperLetters = "".join(random.choices(string.ascii_uppercase, k = 2))
        PSWDLowerLetters = "".join(random.choices(string.ascii_lowercase, k = 2))
        PSWDNumbers = "".join(random.choices(string.digits, k = 4))
        PSWDSymbols = "".join(random.choices(string.punctuation, k = 4))

        GeneratedPSWD = BirthMonth + Birthday + PSWDUpperLetters + PSWDLowerLetters + PSWDNumbers + PSWDSymbols
        return GeneratedPSWD

    # Main program starts here.

    while True:

        # Gather user inputs.

        MemFirstName = input("Enter member first name: ").title()
        MemLastName = input("Enter member last name: ").title()
        
        while True:
            MemPhone = input("Enter the member's phone number (9999999999): ") 
            if MemPhone == "":
                print("Data Entry Error - Phone Number cannot be blank.")
            elif len(MemPhone) != 10:
                print("Data Entry Error - Phone Number must be 10 digits.")
            elif MemPhone.isdigit() == False:
                print("Data Entry Error - Phone Number contains invalid characters.")
            else: 
                break
        
        while True:
            try:
                MemberOpenDate = input("Enter the membership start date (YYYY-MM-DD): ")
                MemberOpenDate = datetime.datetime.strptime(MemberOpenDate, "%Y-%m-%d")
            except:
                print("Data Entry Error - start date is not a valid format.")
            else:
                break
        
        while True:
            try:
                MemberBirthDate = input("Enter the member birth date (YYYY-MM-DD): ")
                MemberBirthDate = datetime.datetime.strptime(MemberBirthDate, "%Y-%m-%d")
            except:
                print("Data Entry Error - birth date is not a valid format.")
            else:
                break

        # Perform required calculations.

        # Create Membership ID.

        if len(MemFirstName) <= 3 and len(MemLastName) <= 3:
            MemID = MemFirstName[0:2] + MemLastName[0:2] + MemPhone[6:10]
        elif len(MemFirstName) < 3 and len(MemLastName) >= 3:
            MemID = MemFirstName[0:2] + MemLastName[0:3] + MemPhone[6:10]
        elif len(MemFirstName) >= 3 and len(MemLastName) < 3:
            MemID = MemFirstName[0:3] + MemLastName[0:2] + MemPhone[6:10]
        else:
            MemID = MemFirstName[0:3] + MemLastName[0:3] + MemPhone[6:10]

        # Create Membership Password.

        MemPSWD = MemFirstName[0] + MemLastName[-1] + PasswordGenerator(MemberBirthDate)

        # Caculate time until membership expires

        Today = datetime.datetime.now()
        MemberCurYearStart = datetime.datetime(year = Today.year, month = MemberOpenDate.month, day = MemberOpenDate.day)
        
        if Today.month >= MemberCurYearStart.month and Today.day > MemberOpenDate.day:
            MemberEndDate = MemberCurYearStart.replace(year = MemberCurYearStart.year + 1)
        else:
            MemberEndDate = MemberCurYearStart

        # Calculate days until member birthdate

        BirthDateCurYear = datetime.datetime(year = Today.year, month = MemberBirthDate.month, day = MemberBirthDate.day)
        BirthDateNextYear = datetime.datetime(BirthDateCurYear.year + 1, month = MemberBirthDate.month, day = MemberBirthDate.day)

        if BirthDateCurYear > Today:
            DaysUntilBirthDay = (BirthDateCurYear - Today).days
        else:
            DaysUntilBirthDay = (BirthDateNextYear - Today).days
        
        # Calculate time as a member

        MemYears = Today.year - MemberOpenDate.year
        if Today.month < MemberOpenDate.month or (Today.month == MemberOpenDate.month and Today.day < MemberOpenDate.day):
            MemYears -=1
        
        MemMonths = Today.month - MemberOpenDate.month
        if Today.day < MemberOpenDate.day:
            MemMonths -= 1
        if MemMonths < 0:
            MemMonths += 12
        
        if Today.day >= MemberOpenDate.day:
            MemDays = Today.day - MemberOpenDate.day
        else:
            MemDays = MemberOpenDate.day - Today.day
            MemMonths -=1
        
        if MemMonths < 0:
            MemMonths += 12
            MemYears - 1

        MemberLength = str(MemYears) + " year(s), " + str(MemMonths) + " month(s), " + str(MemDays) + " day(s)" 

        # Calculate the renewal Fee

        if (MemberEndDate - Today).days < 30:
            RenewalFee = RENEW_FEE
        else:
            RenewalFee = RENEW_FEE - RENEW_DISCOUNT
        
        if MemYears > 5:
            RenewalFee = RENEW_FEE - FIVE_YEAR_DISCOUNT
        
        HST = RenewalFee * HST_RATE

        TotalRenewFee = RenewalFee + HST
        
        # Display results.

        MemberBirthDateDsp = MemberBirthDate.strftime("%Y-%m-%d")
        MemberOpenDateDsp = MemberOpenDate.strftime("%Y-%m-%d")
        MemberEndDateDsp = MemberEndDate.strftime("%Y-%m-%d")
        TotalRenewFeeDsp = "${:,.2f}".format(TotalRenewFee)
        MemPhoneDSP = "(" + MemPhone[0:3] + ") " + MemPhone[3:6] + "-" + MemPhone[6:10]
        MemberNameDSP = f"{MemFirstName} {MemLastName}"

        
        print("+----------------------------------------------------------+")
        print("|                        TECHTITANS                        |")
        print(f"| Member Name:    {MemberNameDSP:>41s}|")
        print(f"| Member Phone Number:                       {MemPhoneDSP}|")
        print(f"| Member Birthdate                               {MemberBirthDateDsp}|")
        print(f"| Days Until Birthday:                                  {DaysUntilBirthDay:>3d}|")
        print("|                                                          |")
        print(f"| Member ID:                                     {MemID:>10s}|")
        print(f"| Member Password:                       {MemPSWD}|")
        print("|                                                          |")
        print(f"| Member Since:                                  {MemberOpenDateDsp}|")
        print(f"| Membership Expiry Date:                        {MemberEndDateDsp}|")
        print(f"| Time as a Member:        {MemberLength:>32s}|")
        print("|                                                          |")
        print(f"| Renewal Fee if Renewed Today:                      {TotalRenewFeeDsp}|")
        print("+----------------------------------------------------------+")
        
        while True:
            Continue = input("Do you want to print another membership card? (Y / N): ").upper()

            if Continue != "Y" and Continue != "N":
                print("Data Entry Error - prompt to continue must be a Y or an N.")
            else:
                break
        
        if Continue == "N":
            break

def maintenance_schedule():

# A program to create a maintenance schedule for XYZ Company to perform basic cleaning in 10 days, tube and fluid checks in 3 weeks, and a major inspection in 6 months
# Author: Daniel Efford
# Date: June 17th, 2024 - June 21st, 2024

    # Set Constants
    USEFUL_MONTHS = 180
    SALVAGE_RATE = 0.1

    # Define Functions
    def PPrint(screenWidth, *args):
        """
        Stands for 'Positional Print'
        Positions multiple text elements along a line.

        *args allows functions to take arguments as they're given: 
            Earch arg is a tuple of variable length. Each tuple contains:
                - content (str): The string to print.
                - position (int or str): The position along the line if an int, or one of 'left', 'right', 'center'.
                - align (str, optional): If position is an int, align can be 'left' or 'right'. Defaults to 'left'.

        Returns the elements along a line specifically positioned.
        """

        line = [' '] * screenWidth  # Creates a list of spaces to build the line

        for content, position, *optional in args:
            if content: 
                align = optional[0] if optional else 'left'
                if isinstance(position, int): 
                    start = position if align == 'left' else position - len(content)
                elif position == 'left':
                    start = 0
                elif position == 'right':
                    start = screenWidth - len(content)
                elif position == 'center':
                    start = (screenWidth - len(content)) // 2

                # Insert the content into the line list
                for i, char in enumerate(content):
                    if 0 <= start + i < screenWidth:
                        line[start + i] = char
            else:
                print() 


        # Convert list back to string and print
        print(''.join(line))

    # Enter purchase details and check for validation
    while True:
        equipmentCost = input("Enter the cost of the equipment: ")
        if equipmentCost.isdigit():
            equipmentCost = float(equipmentCost)
            break
        else:
            print("Invalid input. Please enter a valid cost.")

    while True:
        purchaseDate = input("Enter the date of purchase (YYYY-MM-DD): ")
        if len(purchaseDate) == 10 and purchaseDate[4] == '-' and purchaseDate[7] == '-':
            purchaseDate = datetime.datetime.strptime(purchaseDate, "%Y-%m-%d")
            break
        else:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    # Optional Code to determine date range for the report period.

    # while True:
    #     startDate = input("Enter the start of report period (YYYY-MM-DD): ")
    #     if len(startDate) == 10 and startDate[4] == '-' and startDate[7] == '-':
    #         startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    #         break
    #     else:
    #         print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    # while True:
    #     endDate = input("Enter the last date of report period (YYYY-MM-DD): ")
    #     if len(endDate) == 10 and endDate[4] == '-' and endDate[7] == '-':
    #         endDate = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    #         break
    #     else:
    #         print("Invalid date format. Please enter the date in YYYY-MM-DD format.")



    # Define calculations


    salvageValue = equipmentCost * 0.1
    amortization = (equipmentCost - salvageValue) / USEFUL_MONTHS

    # Store all dates in list
    cleaningDates = []
    fluidCheckDates = []
    inspectionDates = []

    amortizationPeriod = purchaseDate + datetime.timedelta(weeks=(52 * 15))

    for day in range(0, (365 * 15), 10):
        cleaningDate = purchaseDate + datetime.timedelta(days=day)
        cleaningDate = cleaningDate.strftime("%Y-%m-%d")
        cleaningDates.append(cleaningDate)

    for week in range(0, (52 * 15), 3):
        fluidCheckDate = purchaseDate + datetime.timedelta(weeks=week)
        fluidCheckDate = fluidCheckDate.strftime("%Y-%m-%d")
        fluidCheckDates.append(fluidCheckDate)

    for week in range(0, (52 * 15), 26):
        inspectionDate = purchaseDate + datetime.timedelta(weeks=week)
        inspectionDate = inspectionDate.strftime("%Y-%m-%d")
        inspectionDates.append(inspectionDate)

    if datetime.datetime.strptime(cleaningDates[len(inspectionDates) - 1], "%Y-%m-%d") < amortizationPeriod:
        cleaningDates[len(inspectionDates) - 1] = "And so on..."

    if datetime.datetime.strptime(fluidCheckDates[len(inspectionDates) - 1], "%Y-%m-%d") < amortizationPeriod:
        fluidCheckDates[len(inspectionDates) - 1] = "And so on..."

    # Print out schedule

    print()
    PPrint(70, (("+", "-" * 68, "+"), "left"))
    PPrint(70, ("|", "left"), ("XYZ Company - Equipment Maintenance Schedule", "center"), ("|", "right"))
    PPrint(70, (("+", "-" * 68, "+"), "left"))
    PPrint(70, ("|", "left"), ("Basic Cleaning", 5, "left"), ("Tube and Fluid Check", "center"), ("Major Inspection", 65, "right"), ("|", "right"))
    PPrint(70, ("|", "left"), ("Every 10 Days", 5), ("Every 3 Weeks", "center"), ("Every 6 Months", 64, "right"), ("|", "right"))
    PPrint(70, (("+", "-" * 68, "+"), "left"))

    for cleaningDate, fluidCheckDate, inspectionDate in zip(cleaningDates, fluidCheckDates, inspectionDates):
        PPrint(70, ("|", "left"), (cleaningDate, 7), (fluidCheckDate, 29, "left"), (inspectionDate, 62, "right"), ("|", "right"))

    PPrint(70, ("|", "left"), ("|", "right"))
    PPrint(70, (("+", "-" * 68, "+"), "left"))
    PPrint(70, ("|", "left"), ("Amortization Details", "center"), ("|", "right"))
    PPrint(70, (("+", "-" * 68, "+"), "left"))
    PPrint(70, ("|", "left"), ("|", "right"))
    PPrint(70, ("|", "left"), ("Purchase Value:", 5), (f"${equipmentCost:,.2f}", 50), ("|", "right"))
    PPrint(70, ("|", "left"), ("Amortization End Date:", 5), (amortizationPeriod.strftime("%Y-%m-%d"), 50), ("|", "right"))
    PPrint(70, ("|", "left"), ("Salvage Value:", 5),(f"${salvageValue:,.2f}", 50), ("|", "right"))
    PPrint(70, ("|", "left"), ("|", "right"))
    PPrint(70, (("+", "-" * 68, "+"), "left"))

def PSWD_strength():
    # Description: Program to evaluate the statistical strength and implied security of a password entered by the user
    # Author: Chris Morrison, Group 9
    # Date: June 21, 2024 - June 26, 2024
    # Version: 1.0

    # Constants
    MIN_PASSWORD_LENGTH = 1
    MAX_PASSWORD_LENGTH = 25

    # Functions

    # Normalization (to be able to compare all values on a consisten scale from 0-1)
    def normalize(value, min_value, max_value):
        if min_value == max_value:
            return 1
        norm_value = (value - min_value) / (max_value - min_value)
        return round(norm_value, 4)

    # Main body of program
    while True:

        # Gather user inputs (25 characters is used as the max bound password length but can be updated in constants)
        while True:
            print()
            password = input("Enter a password for evaluation: ")
            if len(password) < 1 or len(password) > 25:
                print("Password must be between 1 and 25 characters")
            else:
                break

        # Perform calculations

        # Determine password length (longer is better for score)
        password_length = len(password)
    
        # Normalize length (as to add it to the strength score in a consistent way)
        password_length_norm = normalize(password_length, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)
        
        password_length_score = password_length_norm * 100
        password_length_score = round(password_length_score)

        # Use COLLECTIONS to count occurrences of each unique character in the password (diversity better for strength score)
        character_count = collections.Counter(password)

        # Take average of number of counts per character (the higher the average character score, the less diverse the characters)
        total_counts = sum(character_count.values())
        num_unique_characters = len(character_count)
        average_count = total_counts / num_unique_characters 
        average_count = round(average_count, 4)
    
        # Find the highest count value in character_count (need for upper bound of normalization function for average character count normalization)
        max_count = max(character_count.values())
        
        # Normalize average number of counts per character (as to add it to the strength score in a consistent way - though this is a penalty)
        average_count_norm = normalize(average_count, 1, max_count) 
        average_count_norm_invert = 1 - average_count_norm
        average_count_round = round(average_count_norm_invert, 4)

        # Use SET to determine how diverse the characters are overall
        unique_characters = set(password)
        num_unique_characters = len(unique_characters)

        # Normalize how diverse the characters are overall (as to add it to the strength score in a consistent way)
        unique_characters_norm = normalize(num_unique_characters, 1, MAX_PASSWORD_LENGTH)

        # Use LIST COMPREHENSION to filter character types into their own lists
        uppercase_characters = [character for character in password if character.isupper()]
        lowercase_characters = [character for character in password if character.islower()]
        digits = [character for character in password if character.isdigit()]
        special_characters = [character for character in password if not character.isalnum()]

        # Use LEN to determine the total number of unique characters in each list of character types
        num_uppercase_characters = len(uppercase_characters)
        num_lowercase_characters = len(lowercase_characters)
        num_digits = len(digits)
        num_special_characters = len(special_characters)

        # Use SET to determine how diverse the uppercase characters are
        unique_uppercase_characters = set(uppercase_characters)
        num_unique_uppercase_characters = len(unique_uppercase_characters)

        # Use SET to determine how diverse the lowercase characters are
        unique_lowercase_characters = set(lowercase_characters)
        num_unique_lowercase_characters = len(unique_lowercase_characters)

        # Use SET to determine how diverse the digits are
        unique_digits = set(digits)
        num_unique_digits = len(unique_digits)

        # Use SET to determine how diverse the special characters are
        unique_special_characters = set(special_characters)
        num_unique_special_characters = len(unique_special_characters)

        # Calculate the ratio of unique characters to the total number of characters for each character type
        if num_uppercase_characters > 0:
            ratio_uppercase = num_unique_uppercase_characters / num_uppercase_characters
        else: 
            ratio_uppercase = 0
        ratio_uppercase = round(ratio_uppercase, 4)
        
        if num_lowercase_characters > 0:
            ratio_lowercase = num_unique_lowercase_characters / num_lowercase_characters
        else: 
            ratio_lowercase = 0
        ratio_lowercase = round(ratio_lowercase, 4)

        if num_digits > 0:
            ratio_digits = num_unique_digits / num_digits
        else: 
            ratio_digits = 0
        ratio_digits = round(ratio_digits, 4)

        if num_special_characters > 0:
            ratio_special = num_unique_special_characters / num_special_characters
        else: 
            ratio_special = 0
        ratio_special = round(ratio_special, 4)

        # Use VARIANCE from statistics to determine variance of the character type ratios, essentially rewarding greater equal distribution
        ratios = [ratio_uppercase, ratio_lowercase, ratio_digits, ratio_special]
        variance = statistics.variance(ratios)
        variance = round(variance, 4)

        # Normalize variance (as to add it to the strength score in a consistent way - must be inverted as lower result would normally be better)
        max_variance = (1/4) # as there are 4 possible ratios
        normalized_variance = 1 - normalize(variance, 0, max_variance)
        normalized_variance = round(normalized_variance, 4)

        # Combine values to tally strength score
        combined_score = (password_length_norm + average_count_norm_invert + unique_characters_norm + normalized_variance) / 4
        combined_score = round(combined_score, 4)

        # Convert score to percentage
        score_percent = combined_score * 100
        score_percent = round(score_percent)

        """ # Not needed if score is tallied via an average
        # Normalize the combined score
        max_possible_score = 4  # as there are 4 components
        normalized_combined_score = normalize(combined_score, 0, max_possible_score)
        normalized_combined_score = round(normalized_combined_score, 4)
        """
        # Password strength classification
        if combined_score > 0.97:
            password_rating = "Impenetrable"
        elif combined_score > 0.9:
            password_rating = "Extremely Strong"
        elif combined_score > 0.8:
            password_rating = "Very Strong"
        elif combined_score > 0.7:
            password_rating = "Strong"
        elif combined_score > 0.6:
            password_rating = "Moderate"
        elif combined_score > 0.5:
            password_rating = "Weak"
        elif combined_score > 0.4:
            password_rating = "Very Weak"
        else: 
            password_rating = "Extremely Weak"



        # Display results
        print()
        print("+-------------------------------------------+")
        print("|                                           |")
        print("|        PASSWORD STRENGTH EVALUATOR        |")
        print("|        ___________________________        |")
        print("|                                           |")
        print("|                                           |")
        print(f"|    PASSWORD SCORE:    {score_percent:>15d}%    |")
        print(f"|    PASSWORD RATING:   {password_rating:>16s}    |")
        print("|                                           |")
        print("|-------------------------------------------|")



        # Continue or end program
        while True:
            go_or_stop = input("Would you like to evaluate another password? (y or n): ").upper()

            if go_or_stop != "Y" and go_or_stop != "N":
                print("Invalid Selection")
            else:
                break
        
        if go_or_stop == "N":
            break
    
    print("Stay safe!")

# Create function for the menu 

def menu():
    print("[1] Complete a travel claim.")
    print("[2] Fun interview question.")
    print("[3] Cool stuff with strings and dates")
    print("[4] A little bit of everything.")
    print("[5] Something old, something new.")
    print("[6] Quit.")
       
while True:
    menu()
    Option = input("Please enter which program you would like to run: ")
    if not Option.isdigit() or len(Option) != 1 or int(Option) not in range(1, 7):
        print("Program choice must be 1, 2, 3, 4, 5 or 6")
    else:
        Option = int(Option)

        if Option == 1:
            NL_chocolate_company()
        elif Option == 2:
            fizz_bizz()
        elif Option == 3:
            membership_card()
        elif Option == 4:
            maintenance_schedule()
        elif Option == 5:
            PSWD_strength()
        elif Option == 6:
            break

        print()