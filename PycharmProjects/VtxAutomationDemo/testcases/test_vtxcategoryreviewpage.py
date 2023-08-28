import time

import pytest

from pages.vtxcategoryreviewpage import CategoryReviewPage
from pages.vtxloginpage import LoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestCategoryReviewPage:

    def test_category_review_page(self):
        lp=LoginPage(self.driver)
        lp.do_login_with_valid_credentials(ReadConfig.getUserName(),ReadConfig.getPassword())
        cr=CategoryReviewPage(self.driver)
        assert cr.is_Vtx_logo_exists_on_category_review_page()==True
        assert cr.verify_main_menu_of_tax_categorizations_exists()==True
        assert cr.verify_tax_categorization_page_header()==ReadConfig.getTcPageHeader()
        assert cr.is_Vtx_CategoryReviewPage_description_exists()==True
        cr.verify_broken_links_of_tax_categorizations_panel()
        assert cr.verify_number_of_links_listed_under_tax_categorizations_panel()==3
        cr.list_the_modules_under_tax_categorizations()
        cr.click_on_batch_number_column()
        assert cr.check_for_ascending_sorting_of_batch_number_column()==sorted(cr.check_for_ascending_sorting_of_batch_number_column())
        cr.click_on_batch_number_column()
        assert cr.check_for_descending_sorting_of_batch_number_column()==sorted(cr.check_for_descending_sorting_of_batch_number_column(),reverse=True)
        cr.click_on_batch_number_column()
        cr.check_fiter_functionality_for_added_date_and_time_column("January","2023","25")
        assert cr.check_for_filter_result()=="No Data"
        time.sleep(5)




