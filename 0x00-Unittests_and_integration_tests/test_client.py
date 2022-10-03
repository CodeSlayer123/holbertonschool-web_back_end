#!/usr/bin/env python3
"""Test cases for client class
"""
import unittest
from unittest import mock
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import (
    GithubOrgClient,
    access_nested_map,
    memoize,
)
import urllib.error
import fixtures

class TestGithubOrgClient(unittest.TestCase):
    """Test github org client class"""

    @parameterized.expand([

        ("google"),
        ("abc"),

        ])
    @patch("client.get_json", return_value={"key": "val"})
    def test_org(self, org_name, json):
        """Test github org client function"""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {'key': 'val'})
        json.assert_called_once()

    def test_public_repos_url(self):
        """Test public repos url function"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_last_transaction:
            mock_last_transaction.return_value = {"repos_url": "url"}
            myclass = GithubOrgClient("org_name")
            self.assertEqual(myclass._public_repos_url, "url")
            mock_last_transaction.assert_called_once_with()

    @patch("client.get_json", return_value={"key": "val"})
    def test_public_repos(self, get_json):
        """Test public repos function"""
        with patch('client.GithubOrgClient.public_repos', new_callable=PropertyMock) as mock_last_transaction:
            mock_last_transaction.return_value = {"repos_url": "url"}
            myclass = GithubOrgClient("org_name")
            x = get_json()
            self.assertEqual(myclass.public_repos, {'repos_url': 'url'})
            mock_last_transaction.assert_called_once_with()
            get_json.assert_called_once_with()


    @parameterized.expand([

            ({"license": {"key": "my_license"}}, ("my_license"), True),
            ({"license": {"key": "other_license"}}, ("my_license"), False),

            ])
    def test_has_license(self, repo, license_key, expected):
        """Test has license function"""

        myclass= GithubOrgClient("org_name")
        self.assertEqual(myclass.has_license(repo, license_key), expected)

@parameterized_class(
    
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    fixtures.TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test Integration github org client function"""
    @classmethod
    def setUpClass(cls):
        """sets up class"""
        print("setUp")
        cls.get_patcher = patch('requests.get', side_effect=urllib.error.HTTPError)
    @classmethod
    def tearDownClass(cls):
        """tears down class"""
        cls.get_patcher.stop()

