from unittest import mock

from django.contrib.auth import get_user_model
from django.test import TestCase

from requests.exceptions import RequestException

from github_oauth.backends import GithubOAuthBackend
from github_oauth.backends import (
    GithubOAuthBadResponse,
    GithubOAuthConnectionError,
    GithubOAuthError,
    GithubOAuthJSONDecodeError,
)

from registrations.models import Employee

User: Employee = get_user_model()


class GithubOAuthBackendTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.github_id = 0
        cls.github_username = "test_user"
        cls.github_code = "fake code"
        cls.github_access_token = "fake token"

        cls.test_user = User.objects.create_user(github_id=cls.github_id)

    def test_authenticate_success(self):
        backend = GithubOAuthBackend()

        backend.get_github_info = mock.MagicMock(return_value={"id": self.github_id})

        result_user = backend.authenticate(None, self.github_code)

        self.assertEqual(self.test_user, result_user)

    def test_authenticate_fail(self):
        backend = GithubOAuthBackend()

        backend.get_github_info = mock.MagicMock(return_value={"id": self.github_id + 1})

        result_user = backend.authenticate(None, self.github_code)

        self.assertIsNone(result_user)

    def test_authenticate_exception(self):
        backend = GithubOAuthBackend()

        backend.get_github_info = mock.MagicMock(return_value={"not": "id"})
        self.assertRaises(GithubOAuthBadResponse, backend.authenticate, None, self.github_code)

    def test_authenticate_exception_request(self):
        backend = GithubOAuthBackend()

        backend.get_github_info = mock.MagicMock(side_effect=GithubOAuthConnectionError)

        self.assertRaises(GithubOAuthError, backend.authenticate, None, self.github_code)

    def test_get_user_success(self):
        backend = GithubOAuthBackend()
        result_user = backend.get_user(self.test_user.id)

        self.assertEqual(result_user, self.test_user)

    def test_get_user_fail(self):
        backend = GithubOAuthBackend()
        result_user = backend.get_user(self.test_user.id + 1)

        self.assertIsNone(result_user)

    @mock.patch("requests.post")
    def test__get_access_token(self, mock_post):
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            "access_token": self.github_access_token,
            "token_type": "bearer",
            "scope": "user:email",
        }
        mock_post.return_value = mock_response

        access_token = GithubOAuthBackend._get_access_token(self.github_code)

        self.assertEqual(access_token, self.github_access_token)

    @mock.patch("requests.post", side_effect=RequestException)
    def test__get_access_token_exception_requests(self, mock_post):
        self.assertRaises(GithubOAuthConnectionError, GithubOAuthBackend._get_access_token, self.github_code)

    @mock.patch("requests.post")
    def test__get_access_token_exception_json(self, mock_post):
        mock_response = mock.Mock()
        mock_response.json.side_effect = ValueError
        mock_post.return_value = mock_response

        self.assertRaises(GithubOAuthJSONDecodeError, GithubOAuthBackend._get_access_token, self.github_code)

    @mock.patch("requests.post")
    def test__get_access_token_exception_key(self, mock_post):
        mock_response = mock.Mock()
        mock_response.json.side_effect = KeyError
        mock_post.return_value = mock_response

        self.assertRaises(GithubOAuthBadResponse, GithubOAuthBackend._get_access_token, self.github_code)

    @mock.patch("requests.get")
    def test_get_github_info(self, mock_get):
        backend = GithubOAuthBackend()

        backend._get_access_token = mock.Mock(return_value=self.github_access_token)

        mock_response = mock.Mock()
        mock_response.json.return_value = {"login": self.github_username, "id": self.github_id}

        mock_get.return_value = mock_response

        github_info = backend.get_github_info(self.github_code)

        self.assertEqual(github_info, mock_response.json.return_value)

    def test_get_github_info_connection_error(self):
        backend = GithubOAuthBackend()

        backend._get_access_token = mock.Mock(side_effect=GithubOAuthJSONDecodeError)

        self.assertRaises(GithubOAuthJSONDecodeError, backend.get_github_info, self.github_code)

    @mock.patch("requests.get", side_effect=RequestException)
    def test_get_github_info_exception_requests(self, mock_get):
        backend = GithubOAuthBackend()
        backend._get_access_token = mock.Mock(return_value=self.github_access_token)

        self.assertRaises(GithubOAuthConnectionError, backend.get_github_info, self.github_code)

    @mock.patch("requests.get")
    def test_get_github_info_exception_json(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.side_effect = ValueError
        mock_get.return_value = mock_response

        backend = GithubOAuthBackend()
        backend._get_access_token = mock.Mock(return_value=self.github_access_token)

        self.assertRaises(GithubOAuthJSONDecodeError, backend.get_github_info, self.github_code)
