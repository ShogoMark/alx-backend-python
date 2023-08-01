#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

def mock_get_json(url):
    mock_responses = {
		"https://api.github.com/orgs/google": {
			"login": "google", "repos_url": "https://api.github.com/orgs/google/repos"},
        "https://api.github.com/orgs/abc": {"login": "abc", "repos_url": "https://api.github.com/orgs/abc/repos"},
    }
class TestGithubOrgClient(unittest.TestCase):
    def test_org
