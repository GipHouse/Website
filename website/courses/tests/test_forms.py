from django.test import TestCase

from freezegun import freeze_time

from courses.forms import year_choices


class FormCoursesTest(TestCase):
    @freeze_time("2010-01-01")
    def test_year_choices(self):
        self.assertEqual(year_choices(), [(2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011)])
