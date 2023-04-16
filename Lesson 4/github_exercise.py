# API Testing

# 1.
# Create a program in python that goes to the following API and
# checks that at least 5 git repositories exists - https://api.github.com/users/avielb/repos

import requests

url = 'https://api.github.com/users/avielb/repos'

response = requests.get(url)

# Check if response status code is 200 (OK)
if response.status_code == 200:
    # Parse response JSON data
    repos = response.json()
    print(repos)

    # Check if at least 5 repositories exist
    if len(repos) >= 5:
        print("At least 5 repos exist for user avielb.")
    else:
        print("Less than 5 repos exist for user avielb.")
else:
    print("Error: Failed to access API endpoint.")


