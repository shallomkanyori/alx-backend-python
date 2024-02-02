#!/usr/bin/env python3
"""Tests the GitHubOrgClient

Classes:
    TestGithubOrgClient
"""
import unittest
from unittest import mock
from unittest.mock import patch

import client
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GitHubOrgClient"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: mock.MagicMock):
        """Tests the org property"""

        test_client = GithubOrgClient(org_name)
        res = test_client.org
        mock_get_json.assert_called_once_with(
                GithubOrgClient.ORG_URL.format(org=org_name))
