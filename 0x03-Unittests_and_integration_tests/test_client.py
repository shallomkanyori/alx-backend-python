#!/usr/bin/env python3
"""Tests the GitHubOrgClient

Classes:
    TestGithubOrgClient
    TestIntegrationGithubOrgClient
"""
import unittest
from unittest import mock
from unittest.mock import patch, PropertyMock, MagicMock

import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from typing import Dict, Union


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, license: Dict[str, Dict], license_key: str,
                         expected: bool):
        """Tests the has_license static method"""
        assert GithubOrgClient.has_license(license, license_key) == expected


@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"), [
    TEST_PAYLOAD[0]
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Intergration tests for GithubOrgClient"""

    get_patcher = None
    org = 'google'

    @classmethod
    def mock_get(cls, url: str) -> Union[MagicMock, None]:
        """Mock the requests.get method"""

        if url == GithubOrgClient.ORG_URL.format(org=cls.org):
            return MagicMock(**{'json.return_value': cls.org_payload})
        elif url == cls.org_payload['repos_url']:
            return MagicMock(**{'json.return_value': cls.repos_payload})

    @classmethod
    def setUpClass(cls):
        """Set up the patcher"""

        cls.get_patcher = patch('requests.get', side_effect=cls.mock_get)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Intergration tests the public_repos method"""

        test_client = GithubOrgClient(self.org)
        output = test_client.public_repos()

        assert output == self.expected_repos

    def test_public_repos_with_license(self):
        """Intergration tests the public_repos method with license argument"""

        test_client = GithubOrgClient(self.org)
        output = test_client.public_repos(license="apache-2.0")

        assert output == self.apache2_repos
