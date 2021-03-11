from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    NAME = "chips"
    DESCRIPTION = "I love chips"
    USERNAME = "tester"
    USER_EMAIL = "test@email.com"
    USER_PASS = "pass"

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username=self.USERNAME,
            email=self.USER_EMAIL,
            password=self.USER_PASS
        )

        self.snack = Snack.objects.create(
            name=self.NAME,
            description=self.DESCRIPTION,
            user=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), self.NAME)


    def test_snack_content(self):
        self.assertEqual(self.snack.name, self.NAME)
        self.assertEqual(str(self.snack.user), self.USER_EMAIL)
        self.assertEqual(self.snack.description, self.DESCRIPTION)

    def test_snack_list_view(self):
        self.client.login(email=self.USER_EMAIL, password=self.USER_PASS)
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.NAME)
        self.assertTemplateUsed(response, "snacks/snack-list.html")
        self.assertTemplateUsed(response, "_base.html")

    def test_snack_detail_view(self):
        self.client.login(email=self.USER_EMAIL, password=self.USER_PASS)
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/999999/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.USER_EMAIL)
        self.assertTemplateUsed(response, "snacks/snack-detail.html")
        self.assertTemplateUsed(response, "_base.html")
