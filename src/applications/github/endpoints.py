class Endpoints:
    login = "/login"
    search_repositories = "/search/repositories"

    def get_user(self, username: str):
        return f"/users/{username}"
