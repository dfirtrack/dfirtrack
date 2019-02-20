from django.test import TestCase
from dfirtrack_main.models import Recommendation

class RecommendationModelTestCase(TestCase):
    """ recommendation model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Recommendation.objects.create(recommendation_name='recommendation_1', recommendation_note='lorem ipsum')

    def test_recommendation_string(self):

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # compare
        self.assertEqual(str(recommendation_1), 'recommendation_1')

    def test_recommendation_name_label(self):

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # get label
        field_label = recommendation_1._meta.get_field('recommendation_name').verbose_name
        # compare
        self.assertEquals(field_label, 'recommendation name')

    def test_recommendation_note_label(self):

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # get label
        field_label = recommendation_1._meta.get_field('recommendation_note').verbose_name
        # compare
        self.assertEquals(field_label, 'recommendation note')

    def test_recommendation_name_length(self):

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # get max length
        max_length = recommendation_1._meta.get_field('recommendation_name').max_length
        # compare
        self.assertEquals(max_length, 30)
