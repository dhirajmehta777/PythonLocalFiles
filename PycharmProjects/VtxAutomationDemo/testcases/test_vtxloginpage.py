import time

import pytest

from pages.vtxloginpage import LoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_login_page(self):
        lp=LoginPage(self.driver)
        assert lp.get_login_page_title()==ReadConfig.getLoginPageTitle()
        assert lp.is_Vtx_logo_exists()==True
        assert lp.is_Vtx_loginpage_description_exists()==True
        lp.do_login_with_valid_credentials(ReadConfig.getUserName(),ReadConfig.getPassword())
        assert lp.verify_tax_categorization_page_header()==ReadConfig.getTcPageHeader()


