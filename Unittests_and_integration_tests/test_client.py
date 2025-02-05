#!/usr/bin/env python3
"""Unit and integration tests for the GithubOrgClient class."""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import Dict, List, Any
import requests

class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")  # Mock get_json
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        Test that the 'org' property of GithubOrgClient returns the correct
        values for different organizations.

        Args:
            org_name (str): The name of the organization to be tested.
            mock_get_json (Mock): Mocked version of the get_json function.
        """

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
        """
        Test that the '_public_repos_url' property returns the correct URL
        for the given organization.

        This method tests the functionality of the '_public_repos_url' property
        in the GithubOrgClient class using a mocked version of 'org' property.

        Args:
            None
        """

        # Define the mocked payload for the org property
        mocked_org_payload: Dict[str, str] = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # Use patch.object to mock the org property as a PropertyMock
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org: Mock = mock_org

            mock_org.return_value = mocked_org_payload

            # Instantiate the client
            client: GithubOrgClient = GithubOrgClient("google")

            # Test the _public_repos_url property
            result: str = client._public_repos_url

            # Checks that the result is the expected URL
            self.assertEqual(result, mocked_org_payload["repos_url"])

            # Check that org is only accessed once
            mock_org.assert_called_once()

    @patch("client.get_json")  # Mock get_json
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """
        Test that the 'public_repos' method returns a list of repository names
        for the given organization.

        This method tests the behavior of the 'public_repos' method by mocking
        the response from the 'get_json' function.

        Args:
            mock_get_json (Mock): Mocked version of the get_json function.
        """

        # Define the mocked response from get_json
        mocked_repos_payload: List[Dict[str, str]] = [
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
            result: List[str] = client.public_repos()

            # Expected list of repo names
            expected_result: List[str] = ["repo1", "repo2", "repo3"]

            # Assert the result matches expectations
            self.assertEqual(result, expected_result)

            # Ensure get_json was called once with the correct URL
            mock_get_json.assert_called_once_with(mocked_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
        self, repo: Dict[str, Any], license_key: str, expected_result: bool
    ) -> None:
        """
        Test that the 'has_license' method correctly checks for the given
        license key in the repository's license information.

        Args:
            repo (Dict[str, Dict[str, str]]): A dictionary representing the
                repository's license data.
            license_key (str): The license key to check for in the repository.
            expected_result (bool): The expected result based on license check.
        """
        result: bool = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the patcher for requests.get to mock external API calls."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            if 'orgs' in url:
                return MockResponse(cls.org_payload)
            elif 'repos' in url:
                return MockResponse(cls.repos_payload)
            return MockResponse({})

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method with mocked data."""
        client = GithubOrgClient("google")

        repos = client.public_repos()

        self.assertEqual(repos, self.expected_repos)

    def test_apache2_repos(self):
        """Test public_repos with apache2 repositories."""
        client = GithubOrgClient("apache2")

        repos = client.public_repos()

        self.assertEqual(repos, self.apache2_repos)


class MockResponse:
    """Helper class to mock the responses returned by requests.get."""
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


if __name__ == "__main__":
    unittest.main()
