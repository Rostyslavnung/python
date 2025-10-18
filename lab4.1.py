text = "lorem ipsum dolor sit amet,   consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
max_run = 0
current_run = 0

for char in text:
    if char == ' ':
        current_run += 1
        if current_run > max_run:
            max_run = current_run
    else:
        current_run = 0

print("Maximum number of consecutive spaces:", max_run)