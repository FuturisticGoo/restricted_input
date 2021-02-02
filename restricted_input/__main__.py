import restricted_input
for i in restricted_input.get_input_types():
    print(restricted_input.r_input(f"Enter {i}: ", i,
                                   warning=f"Only {i} allowed. Enter {i}: "))
