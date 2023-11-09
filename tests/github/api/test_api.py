import requests
import pytest
from src.providers.data.users_provider import UsersProvider
from src.providers.data.repositories_provider import RepositoriesProvider


def test_user_exists(github_api_client):
    user = UsersProvider.existing_user()
    api_user = github_api_client.get_user(user["username"])

    assert api_user["login"] == user["username"]
    assert api_user["id"] == user["id"]


def test_user_non_exists(github_api_client):
    user = UsersProvider.non_existent_user()
    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user(user["username"])


def test_search_for_existing_repo(github_api_client):
    repo = RepositoriesProvider.existing_repository()
    repos = github_api_client.search_repos(repo["repository_name"])

    print("Cheking total count is not 0")
    assert repos["total_count"] == repo["total_count"]
    assert len(repos["items"]) == repo["items_count"]


def test_search_for_nonexisting_repo(github_api_client):
    repo = RepositoriesProvider.non_existent_repository()
    repos = github_api_client.search_repos(repo["repository_name"])

    print("Cheking total count is 0")
    assert repos["total_count"] == repo["total_count"]
    assert len(repos["items"]) == repo["items_count"]
