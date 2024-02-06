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
                    "id": 4444,
                    "name": "The river between",
                },
                {
                    "id": 4444,
                    "name": "Fwaru",
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

    @parameterized.expand([
        ({"license": {"key": "bsd-3-clause"}}, "bsd-3-clause", True),
        ({"license": {"key": "bsl-1-.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """This method is testing has license function"""
        github_c = GithubOrgClient("google")
        client_license = github_c.has_license(repo, key)
        self.assertEqual(client_license, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """Testing integration of https requests"""

    @classmethod
    def setUpClass(cls) -> None:
        """This method sets up all common features for the test methods"""
        comm_urls = {"return_value.json.side_effect":
            [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload,
            ]
        }

        cls.get_patcher = patch("requests.get", **comm_urls)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Testing the public method"""
        test_c = GithubOrgClient("google")

        self.assertEqual(test_c.org, self.org_payload)
        self.assertEqual(test_c.repos_payload, self.repos_payload)
        self.assertEqual(test_c.public_repos(), self.expected_repos)
        self.assertEqual(test_c.public_repos("EXLICENCE"), [])
        self.mock.assert_called()

    def test_public_repos_license(self) -> None:
        """Testing if public repo has license"""
        test_c = GithubOrgClient("google")

        self.assertEqual(test_c.public_repos(), self.expected_repos)
        self.assertEqual(test_c.public_repos("XLICENCE"), [])
        self.assertEqual(test_c.public_repos(
            "apache-2.0"), self.apache2_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """Cleaning test data"""
        cls.get_patcher.stop()
