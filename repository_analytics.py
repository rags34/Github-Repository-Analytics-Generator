import requests

# Function to fetch repository information using the GitHub API
def fetch_repository_info(owner, repo_name, access_token):
    # Prepare headers with the access token for authentication
    headers = {
        "Authorization": f"token {access_token}"
    }
    
    # Construct the URL to access the repository information
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    
    # Send a GET request to the GitHub API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the JSON response containing repository information
        return response.json()
    else:
        # Return None if the request failed
        return None

# Main function to execute the code
def main():
    # Ask the user to input repository details
    repository_owner = input("Enter the repository-owner's name: ")
    repository_name = input("Enter the repository-name: ")
    
    # Replace 'Enter Your API token after generating here' with your generated API token
    github_token = "Enter Your API token after generating here"

    # Fetch repository information using the provided details and access token
    repo_info = fetch_repository_info(repository_owner, repository_name, github_token)

    # Display repository information if fetched successfully
    if repo_info:
        print(f"Repository: {repo_info['full_name']}")
        print(f"Description: {repo_info['description']}")
        print(f"Stars: {repo_info['stargazers_count']}")
        print(f"Forks: {repo_info['forks_count']}")
        print(f"Primary Language: {repo_info['language']}")
    else:
        # Display a message if repository information couldn't be fetched
        print("Failed to fetch repository information.")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
