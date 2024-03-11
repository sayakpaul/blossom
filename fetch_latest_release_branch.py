import requests
from packaging.version import parse

# GitHub repository details
USER = "sayakpaul"
REPO = "blossom"


def fetch_all_branches(user, repo):
    branches = []  # List to store all branches
    page = 1  # Start from first page
    while True:
        # Make a request to the GitHub API for the branches
        response = requests.get(f"https://api.github.com/repos/{user}/{repo}/branches", params={"page": page})

        # Check if the request was successful
        if response.status_code == 200:
            # Add the branches from the current page to the list
            branches.extend([branch["name"] for branch in response.json()])

            # Check if there is a 'next' link for pagination
            if "next" in response.links:
                page += 1  # Move to the next page
            else:
                break  # Exit loop if there is no next page
        else:
            print("Failed to retrieve branches:", response.status_code)
            break

    return branches


def main():
    # Fetch all branches
    branches = fetch_all_branches(USER, REPO)

    # Filter branches.
    # print(f"Total branches: {len(branches)}")
    filtered_branches = []
    for branch in branches:
        if branch.startswith("v"):
            filtered_branches.append(branch)
            # print(f"Filtered: {branch}")

    sorted_branches = sorted(filtered_branches, key=lambda x: parse(x.split("-")[0][1:]), reverse=True)
    latest_branch = sorted_branches[0]
    # print(f"Latest branch: {latest_branch}")
    return latest_branch


if __name__ == "__main__":
    print(main())