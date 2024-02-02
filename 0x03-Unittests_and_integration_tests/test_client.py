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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock):
        """Tests the public_repos method"""

        google_prepos_payload = [
            {
                "id": 3248507,
                "name": "ruby-openid-apps-discovery",
                "license": None
            },
            {
                "id": 3248531,
                "name": "autoparse",
                "license": {
                    "key": "apache-2.0",
                    "name": "Apache License 2.0",
                    "spdx_id": "Apache-2.0",
                }
            },
            {
                "id": 3975462,
                "name": "anvil-build",
                "license": {
                    "key": "other",
                    "name": "Other",
                    "spdx_id": "NOASSERTION",
                }
            },
            {
                "id": 5072378,
                "name": "googletv-android-samples",
                "license": None
            },
            {
                "id": 5844236,
                "name": "embed-dart-vm",
                "license": None
            }
        ]
        mock_get_json.return_value = google_prepos_payload
        expected_prepos = [r['name'] for r in google_prepos_payload]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_prepos_url:

            mock_prepos_url.return_value = (
                    'https://api.github.com/orgs/google/repos')

            test_client = GithubOrgClient('google')
            prepos = test_client.public_repos()
            assert prepos == expected_prepos

            mock_prepos_url.assert_called_once()
            mock_get_json.assert_called_once()
