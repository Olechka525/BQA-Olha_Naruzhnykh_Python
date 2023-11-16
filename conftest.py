import pytest
from src.applications.github.api.github_api import GitHubAPIClient
from src.applications.github.ui.github_ui import GitHubUiLoginPage
from src.config.config import Config
from src.helpers.browsers_provider import BrowserProvider


@pytest.fixture
def github_api_client(scope="session"):
    api_client = GitHubAPIClient(Config.domain_api)
    yield api_client


@pytest.fixture
def github_login_page_object(scope="session"):
    driver = BrowserProvider.get_driver(Config.browser_name, True)

    github_login_page = GitHubUiLoginPage(driver, Config.domain_ui)
    github_login_page.navigate_to_login_page()

    yield github_login_page

    github_login_page.close_browser()
