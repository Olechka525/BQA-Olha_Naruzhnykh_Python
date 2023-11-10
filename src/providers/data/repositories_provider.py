class RepositoriesProvider:
    @staticmethod
    def existing_repository():
        return {
            "repository_name": "BQA-Olha_Naruzhnykh_Python",
            "total_count": 1,
            "items_count": 1,
        }

    @staticmethod
    def non_existent_repository():
        return {
            "repository_name": "jdvjdnvjn_repo",
            "total_count": 0,
            "items_count": 0,
        }
