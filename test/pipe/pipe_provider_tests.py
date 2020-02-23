import unittest

from unittest.mock import Mock, call

from pulumi_snowflake.pipe import PipeProvider


class WarehouseProviderTests(unittest.TestCase):

    def test_create_pipe_simple_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = PipeProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": 'test_wh',
            "comment": 'test comment',
            "auto_ingest": True,
            "aws_sns_topic": "test_topic",
            "integration": "test_integration",
            "code": '''copy into snowpipe_db.public.mytable
from @snowpipe_db.public.mystage
file_format = (type = 'JSON');'''
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                "CREATE PIPE test_wh",
                "AUTO_INGEST = TRUE",
                "AWS_SNS_TOPIC = 'test_topic'",
                "INTEGRATION = 'test_integration'",
                "COMMENT = 'test comment'",
                "AS copy into snowpipe_db.public.mytable",
                "from @snowpipe_db.public.mystage",
                "file_format = (type = 'JSON');",
            ]))
        ])

    def test_create_pipe_minimal_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = PipeProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": 'test_wh',
            "comment": None,
            "auto_ingest": None,
            "aws_sns_topic": None,
            "integration": None,
            "code": '''copy into snowpipe_db.public.mytable
from @snowpipe_db.public.mystage
file_format = (type = 'JSON');'''
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                "CREATE PIPE test_wh",
                "AS copy into snowpipe_db.public.mytable",
                "from @snowpipe_db.public.mystage",
                "file_format = (type = 'JSON');",
            ]))
        ])

        def test_create_pipe_minimal_args(self):
            mock_cursor = Mock()
            mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

            provider = PipeProvider(self.get_mock_provider(), mock_connection_provider)
            provider.create({
                "name": 'test_wh',
                "comment": None,
                "auto_ingest": None,
                "aws_sns_topic": None,
                "integration": None,
                "code": '''copy into snowpipe_db.public.mytable
    from @snowpipe_db.public.mystage
    file_format = (type = 'JSON');'''
            })

            mock_cursor.execute.assert_has_calls([
                call("\n".join([
                    "CREATE PIPE test_wh",
                    "AS copy into snowpipe_db.public.mytable",
                    "from @snowpipe_db.public.mystage",
                    "file_format = (type = 'JSON');",
                ]))
            ])

    def test_delete_pipe(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = PipeProvider(self.get_mock_provider(), mock_connection_provider)
        provider.delete("test_pipe", {
            "name": "test_pipe"
        })

        mock_cursor.execute.assert_has_calls([
            call(f"DROP PIPE test_pipe")
        ])

    # HELPERS

    def get_mock_connection_provider(self, mock_cursor):
        mockConnection = Mock()
        mockConnection.cursor.return_value = mock_cursor
        mock_connection_provider = Mock()
        mock_connection_provider.get.return_value = mockConnection
        return mock_connection_provider

    def get_mock_provider(self):
        mock_provider = Mock()
        mock_provider.database = None
        mock_provider.schema = None
        return mock_provider
