from django.test import TestCase
from dfirtrack_main.forms import RecommendationForm

class RecommendationFormTestCase(TestCase):
    """ recommendation form tests """

    def test_recommendation_name_label(self):

        # get object
        form = RecommendationForm()
        # compare
        self.assertEquals(form.fields['recommendation_name'].label, 'Recommendation name (*)')

    def test_recommendation_note_label(self):

        # get object
        form = RecommendationForm()
        # compare
        self.assertEquals(form.fields['recommendation_note'].label, 'Recommendation note')

    def test_recommendation_name_empty(self):

        # get object
        form = RecommendationForm(data = {'recommendation_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_recommendation_name_filled(self):

        # get object
        form = RecommendationForm(data = {'recommendation_name': 'recommendation_1'})
        # compare
        self.assertTrue(form.is_valid())
