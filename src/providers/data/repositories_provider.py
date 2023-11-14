from src.config.config_harder import JSONConfigProvider


class RepositoriesProvider:
    @staticmethod
    def existing_repository():
        return {
            "repository_name": JSONConfigProvider.get_repository_data(
                "repository_name_exists"
            ),
            "total_count": 1,
            "items_count": 1,
        }

    @staticmethod
    def non_existent_repository():
        return {
            "repository_name": JSONConfigProvider.get_repository_data(
                "repository_name_not_exist"
            ),
            "total_count": 0,
            "items_count": 0,
        }
