class OnCopyErrorValues:
    """
    Class which represents possible values for error handling when a stage performs a copy operation. See
    https://docs.snowflake.net/manuals/sql-reference/sql/copy-into-table.html#copy-options-copyoptions for more details.
    """

    CONTINUE = "CONTINUE"
    """
    Continue loading the file.
    """

    SKIP_FILE = "SKIP_FILE"
    """
    Skip file if any errors encountered in the file.
    """

    ABORT_STATEMENT = "ABORT_STATEMENT"
    """
    Abort the COPY statement if any error is encountered.
    """

    @staticmethod
    def skip_file(num: int):
        """
        Skip file when the number of errors in the file is equal to or exceeds the specified number.
        """
        if not isinstance(num, int):
            raise Exception("skip_file can only be called with an integer argument")
        return f'SKIP_FILE_{num}'

    @staticmethod
    def skip_file_percent(num: int):
        """
        Skip file when the percentage of errors in the file exceeds the specified percentage.
        """
        if not isinstance(num, int):
            raise Exception("skip_file_percent can only be called with an integer argument")
        return f'SKIP_FILE_{num}%'

