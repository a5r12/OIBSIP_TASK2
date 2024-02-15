
if __name__ == "__main__":
    while 1:
        try: 
            # if we enter non integer or float then it gives error but because of try it jumps to except 
            kg = float(input("Enter weight(kg)"))
            m = float(input("Enter height (m)"))
            bmi = float(kg)/(float(m)**2)
            bmi = round(bmi,1)
            
            
    # weight should be less than 200
    # height should be less than 2.5 ..... you can varry the range 
                    
            if ((kg<=200) and (m<=2.5 )):
                print(f"Your BMI score is {bmi} ")
                if bmi<18.5:
                    print("UNDER WEIGHT!!")
                elif 18.5<=bmi<25:
                    print("PERFECT WEIGHT!! ")
                elif 25<=bmi<30:
                    print("OVER WEIGHT!!")
                elif bmi>=30:
                    print("OBESITY!!")
            else :
                    print("inputs are not in valid range  .., for kg (1 to 200) and m (1 to 2.5) ,\n enter valid imput and try again")
            

        except ValueError:
            print("Please enter valid integer or float value in inputs")
