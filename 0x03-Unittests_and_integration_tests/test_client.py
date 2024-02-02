#!/usr/bin/env python3
"""Tests the GitHubOrgClient

Classes:
    TestGithubOrgClient
"""
import unittest
from unittest import mock
from unittest.mock import patch, PropertyMock, MagicMock

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
    def test_org(self, org_name: str, mock_get_json: MagicMock):
        """Tests the org property"""

        test_client = GithubOrgClient(org_name)
        res = test_client.org
        mock_get_json.assert_called_once_with(
                GithubOrgClient.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """Tests the _public_repos_url property"""

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            google_payload = {'login': 'google',
                              'id': 1342004,
                              'node_id': 'MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=',
                              'url': 'https://api.github.com/orgs/google',
                              'repos_url': ('https://api.github.com'
                                            '/orgs/google/repos'),
                              'description': 'Google ❤️ Open Source',
                              'name': 'Google',
                              'company': None,
                              'public_repos': 2598,
                              'followers': 35376,
                              'following': 0,
                              'html_url': 'https://github.com/google',
                              'created_at': '2012-01-18T01:30:18Z',
                              'updated_at': '2021-12-30T01:40:20Z',
                              'archived_at': None,
                              'type': 'Organization'
                              }

            mock_org.return_value = google_payload

            test_client = GithubOrgClient('google')
            assert test_client._public_repos_url == google_payload["repos_url"]
