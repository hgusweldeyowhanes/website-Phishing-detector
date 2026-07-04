from django.test import SimpleTestCase

from detector.ml.utils import predict_url


class AdvancedUrlDetectorTests(SimpleTestCase):
    def test_suspicious_url_is_flagged_as_phishing(self):
        result = predict_url("https://secure-paypal-login.example.com/account")

        self.assertEqual(result["prediction"], "Phishing")
        self.assertGreaterEqual(result["percentage"], 60)

    def test_safe_url_is_flagged_as_legitimate(self):
        result = predict_url("https://example.com")

        self.assertEqual(result["prediction"], "Legitimate")
        self.assertGreaterEqual(result["percentage"], 60)
