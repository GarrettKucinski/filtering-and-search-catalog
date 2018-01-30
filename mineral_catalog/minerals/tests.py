from django.test import TestCase
from django.urls import reverse

from .models import Mineral


class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        self.mineral = Mineral.objects.create(
            name="testite",
            color="greenish"
        )
        self.assertIn(self.mineral, Mineral.objects.all())


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="testite",
            color="greenish"
        )
        self.mineral1 = Mineral.objects.create(
            name="luddite",
            color="red"
        )
        self.mineral2 = Mineral.objects.create(
            name="pyrite",
            color="gold"
        )
        self.mineral3 = Mineral.objects.create(
            name="florite",
            color="white"
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertIn(self.mineral3, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'mineral_list.html')
        self.assertContains(resp, self.mineral.name)
        self.assertContains(resp, self.mineral1.name)
        self.assertContains(resp, self.mineral2.name)
        self.assertContains(resp, self.mineral3.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(
            reverse('minerals:mineral_detail', kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'mineral_detail.html')
        self.assertContains(resp, self.mineral.name)
