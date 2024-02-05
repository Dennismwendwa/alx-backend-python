#!/usr/bin/env python3
"""This script uses unittest for testing"""
from requests import HTTPError
from typing import Dict
from parameterized import parameterized, parameterized_class
from unittest.mock import MagicMock, Mock, patch, PropertyMock
from unittest import TestCase

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """Testing the githugorgclient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, response: Dict, mocked_obj: MagicMock
                 ) -> None:
        """Testing githuhorg"""
        mocked_obj.return_value = MagicMock(return_value=response)
        github_c = GithubOrgClient(org)
        self.assertEqual(github_c.org(), response)
        mocked_obj.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """Testing get public repos method"""
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock
                   ) as impte:
            impte.return_value = {
                "repos_url": "https://api.github.com/users/google/repos",
            }
            self.assertEqual(GithubOrgClient("google")._public_repos_url,
                             "https://api.github.com/users/google/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Testing public method"""
        t_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "The river between",
                    "url": "https://api.github.com/repos/google/episodes.dart",
                },
                {
                    "id": 8566972,
                    "name": "Fwaru",
                    "url": "https://api.github.com/repos/google/kratu",
                },
            ]
        }
        mock_get_json.return_value = t_payload["repos"]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as pub_repos_call:
            pub_repos_call.return_value = t_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "The river between",
                    "Fwaru",
                ],
            )
            pub_repos_call.assert_called_once()
        mock_get_json.assert_called_once()
