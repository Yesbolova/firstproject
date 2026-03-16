from types import SimpleNamespace

from django.test import SimpleTestCase

from .tokens import account_activation_token


class AccountActivationTokenGeneratorTests(SimpleTestCase):
    def test_hash_value_contains_user_state(self):
        inactive_user = SimpleNamespace(pk=42, is_active=False)
        active_user = SimpleNamespace(pk=42, is_active=True)

        inactive_hash = account_activation_token._make_hash_value(inactive_user, 12345)
        active_hash = account_activation_token._make_hash_value(active_user, 12345)

        self.assertEqual(inactive_hash, "4212345False")
        self.assertEqual(active_hash, "4212345True")
        self.assertNotEqual(inactive_hash, active_hash)
