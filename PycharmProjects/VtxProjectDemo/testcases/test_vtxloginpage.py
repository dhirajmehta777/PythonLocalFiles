import time

import pytest

from pages.vtxloginpage import VtxLoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_login_page(self):
        lp=VtxLoginPage(self.driver)
        assert lp.get_vtx_login_page_title()==ReadConfig.getExpectedTitleOfPage()
        assert lp.is_vtx_logo_exists()==True
        lp.do_Vtx_login_with_valid_credentials(ReadConfig.getUserName(),ReadConfig.getPassword())
        time.sleep(10)
        # lp.do_login_with_invalid_credentials(ReadConfig.getInvalidUserName(),ReadConfig.getInvalidPassword())
        # assert lp.is_invalid_credential_message_displayed()==ReadConfig.getExpectedInvaliCredentialMessage()