#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")  # Mock get_json
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """Test that GithubOrgClient.org() returns the correct value"""
        # Mock API response
        mocked_response: Dict[str, str] = {
            "name": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }
        mock_get_json.return_value = mocked_response

        # Instantiate the client and calls
        client: GithubOrgClient = GithubOrgClient(org_name)
        result: Dict[str, str] = client.org

        # asserts it is only ran once
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, mocked_response)

    def test_public_repos_url(self) -> None:
        """Test that _public_repos_url returns the expected value"""

        # Define the mocked payload for the org property
        mocked_org_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # Use patch.object to mock the org property as a PropertyMock
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = mocked_org_payload

            # Instantiate the client
            client = GithubOrgClient("google")

            # Test the _public_repos_url property
            result = client._public_repos_url

            # Checks that the result is the expected URL
            self.assertEqual(result, mocked_org_payload["repos_url"])

            # Check that org is only accessed once
            mock_org.assert_called_once()

    @patch("client.get_json")  # Mock get_json
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """Test that public_repos returns as expected"""

        # Define the mocked response from get_json
        mocked_repos_payload: list[dict[str, str]] = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = mocked_repos_payload

        # Define the mocked URL for _public_repos_url
        mocked_url: str = "https://api.github.com/orgs/google/repos"

        # Patch _public_repos_url directly here to return the mocked URL
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value=mocked_url
        ):
            client: GithubOrgClient = GithubOrgClient("google")

            # Call the method under test
            result: list[str] = client.public_repos()

            # Expected list of repo names
            expected_result: list[str] = ["repo1", "repo2", "repo3"]

            # Assert the result matches expectations
            self.assertEqual(result, expected_result)

            # Ensure get_json was called once with the correct URL
            mock_get_json.assert_called_once_with(mocked_url)


if __name__ == "__main__":
    unittest.main()
