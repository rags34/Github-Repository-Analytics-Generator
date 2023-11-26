import requests

def fetch_repository_info(owner, repo_name, access_token):
    headers = {
        "Authorization": f"token {access_token}"
    }
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    # Replace these values with your repository details and access token
    repository_owner = input("Enter the repository-owner's name: ")
    repository_name = input("Enter the repository-name: ")
    github_token = "Enter Your API token after generating here"

    repo_info = fetch_repository_info(repository_owner, repository_name, github_token)

    if repo_info:
        print(f"Repository: {repo_info['full_name']}")
        print(f"Description: {repo_info['description']}")
        print(f"Stars: {repo_info['stargazers_count']}")
        print(f"Forks: {repo_info['forks_count']}")
        print(f"Primary Language: {repo_info['language']}")
    else:
        print("Failed to fetch repository information.")

if __name__ == "__main__":
    main()
