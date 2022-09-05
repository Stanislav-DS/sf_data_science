user_dynamics = [-5, 2, 4, 8, 12, -7, 5]

for i, num_users in enumerate(user_dynamics):
    if num_users < 0:
        print(f"Number day: {i + 1}\n"
              f"Churn value: {num_users}")

# Number day: 1
# Churn value: -5
# Number day: 6
# Churn value: -7