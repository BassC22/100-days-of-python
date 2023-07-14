
print("Welcome to the Love Calculator!")

# take in user input for both names
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# convert input to lower case
name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

# combine both names
combined_names = str(name1_lower_case) + str(name2_lower_case)

# count number of times t, r, u and e appear
count_t_true = combined_names.count("t")
count_r_true = combined_names.count("r")
count_u_true = combined_names.count("u")
count_e_true = combined_names.count("e")

# add together to get total
true_total = int(count_t_true) + int(count_r_true) + int(count_u_true) + int(count_e_true)

# repeat process for l, o, v and e
count_l_love = combined_names.count("l")
count_o_love = combined_names.count("o")
count_v_love = combined_names.count("v")
count_e_love = combined_names.count("e")

love_total = int(count_l_love) + int(count_o_love) + int(count_v_love) + int(count_e_love)

# string together two totals to get total score
total_score = str(true_total) + str(love_total)

# if-elif-else statements to display results
if int(total_score) < 10 or int(total_score) > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif int(total_score) >= 40 and int(total_score) <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")







