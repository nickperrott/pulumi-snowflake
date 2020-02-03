from typing import Optional

from pulumi import Input

class CopyOptions:
    """
    Represents options for copying data, used as part of a COPY statement or for creating a STAGE resource.  See
    https://docs.snowflake.net/manuals/sql-reference/sql/copy-into-table.html#copy-options-copyoptions for more details.
    """
    def __init__(self,
                 size_limit: Input[int] = None,
                 on_error: Input[Optional[str]] = None,
                 purge: Input[bool] = None,
                 return_failed_only: Input[bool] = None,
                 match_by_column_name: Input[Optional[str]] = None,
                 enforce_length: Input[bool] = None,
                 truncate_columns: Input[bool] = None,
                 force: Input[bool] = None,
                 load_uncertain_files: Input[bool] = None,
                 ):
        """
        :param pulumi.Input[str] size_limit: Maximum size (in bytes) of data to be loaded for a given COPY statement.
        :param pulumi.Input[str] on_error: String (constant) that specifies the action to perform when an error is
        encountered while loading data from a file.  Should be one of OnCopyErrorValues.
        :param pulumi.Input[bool] purge: Boolean that specifies whether to purge the data files from the location
        automatically after the data is successfully loaded.
        :param pulumi.Input[bool] return_failed_only: Boolean that specifies whether to return only files that have
        failed to load in the statement result.
        :param pulumi.Input[Optional[str]] match_by_column_name: String that specifies whether to load semi-structured
        data into columns in the target table that match corresponding columns represented in the data.  Should be one
        of `MatchByColumnNameValues`.
        :param pulumi.Input[bool] enforce_length: Boolean that specifies whether to truncate text strings that exceed
        the target column length.
        :param pulumi.Input[bool] truncate_columns:  Boolean that specifies whether to truncate text strings that exceed
        the target column length.
        :param pulumi.Input[bool] force: Boolean that specifies to load all files, regardless of whether they’ve been
        loaded previously and have not changed since they were loaded. Note that this option reloads files, potentially
        duplicating data in a table.
        :param pulumi.Input[bool] load_uncertain_files: Boolean that specifies to load files for which the load status
        is unknown. The COPY command skips these files by default.
        """
        self.size_limit = size_limit
        self.on_error = on_error
        self.purge = purge
        self.return_failed_only = return_failed_only
        self.match_by_column_name = match_by_column_name
        self.enforce_length = enforce_length
        self.truncate_columns = truncate_columns
        self.force = force
        self.load_uncertain_files = load_uncertain_files

    def as_dict(self):
        fields = [
            "size_limit",
            "on_error",
            "purge",
            "return_failed_only",
            "match_by_column_name",
            "enforce_length",
            "truncate_columns",
            "force",
            "load_uncertain_files"
        ]
        return { field: getattr(self, field) for field in fields }