from webdriver_manager.core import driver

from pages.google import Google_class
from pages.forms import form_class
import pytest

@pytest.mark.usefixtures('config')
class Test_google:

    def test_googles(self):

        google_object = Google_class(self.driver)
        form_object = form_class(self.driver)

        google_object.search_text("jana nayagan")

        form_object.enter_first_name("subash")


