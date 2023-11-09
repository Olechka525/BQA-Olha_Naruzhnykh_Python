import requests
import urllib
from src.applications.github.endpoints import Endpoints


class GitHubAPIClient:
    """Current class contains every API call we use in tests and discribes rules for communication with GitHub."""

    def __init__(self, domain: str) -> None:
        self.domain = domain

    def get_user(self, username: str):
        user_url = Endpoints()
        r = requests.get(urllib.parse.urljoin(self.domain, user_url.get_user(username)))
        r.raise_for_status()

        return r.json()

    def search_repos(self, repo_name):
        r = requests.get(
            urllib.parse.urljoin(self.domain, Endpoints.search_repositories),
            params={"q": repo_name},
        )
        r.raise_for_status()

        return r.json()
