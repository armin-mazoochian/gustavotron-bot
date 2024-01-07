class EnvironmentFileError(Exception):
    def __str__(self):
        return "Improperly Configured. Check Env file"
