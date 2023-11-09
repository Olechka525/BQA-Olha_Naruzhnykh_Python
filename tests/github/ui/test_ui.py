from src.providers.data.users_provider import UsersProvider


def test_github_login_failed_page_obj(github_login_page_object):
    user = UsersProvider.non_existent_user()
    github_login_page_object.try_to_login(user["username"], user["password"])

    # check error message
    assert github_login_page_object.check_error_message()
