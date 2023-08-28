import time

import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CategoryReviewPage():
    LogoOfVtxForCategoryReviewPage_Xpath="//*[@alt='Home']"
    CategoryReviewPage_Description_Xpath="//*[@class='reviewPageDesc']"
    Tax_Categorization_Page_Header_Xpath="//div[text()='Category Review']"
    Tax_Categorization_Main_Menu_Xpath="//ul[@class='main-menu']"
    Tax_Categorizations_Modules_Xpath="//*[@class='main-menu']//a[contains(@class, 'menu-item-content')]"
    Tax_Categorizations_Links_Xpath="//ul[@class='main-menu']//a"
    Click_On_Batch_Number_Column_Xpath="//*[text()='Batch Number']"
    column_values_Xpath="//*[@class='ant-table-row ant-table-row-level-0']//td[1]"
    added_date_time_filter_icon_Xpath="(//*[@class='anticon anticon-filter'])[1]"
    filter_option_drp_Xpath="(//*[@class='vtx-icon vtx-icon vtx-icon-down'])[2]"
    Equals_Xpath="//div[@class='vtx-select searchTypeSelect__single-value css-qc6sy-singleValue']"
    date_picker_Xpath="//*[@class='react-datepicker__input-container']"
    date_picker_month_Xpath="//*[@class='react-datepicker__month-select']"
    date_picker_year_Xpath="//*[@class='react-datepicker__year-select']"
    date_picker_date_Xpath="//*[@class='react-datepicker__week']//div"
    filter_btn_Xpath="//*[text()='Filter']"
    filter_result_Xpath="//div[text()='No Data']"


    def __init__(self, driver):
        self.driver = driver

    def is_Vtx_logo_exists_on_category_review_page(self):
        wait = WebDriverWait(self.driver, 100)
        vtx_logo_element = wait.until(ec.visibility_of_element_located((By.XPATH, self.LogoOfVtxForCategoryReviewPage_Xpath)))
        return bool(vtx_logo_element)

    def verify_tax_categorization_page_header(self):
        wait = WebDriverWait(self.driver, 100)
        tc_header = wait.until(ec.visibility_of_element_located((By.XPATH, self.Tax_Categorization_Page_Header_Xpath)))
        return tc_header.text

    def is_Vtx_CategoryReviewPage_description_exists(self):
        wait = WebDriverWait(self.driver, 100)
        vtx_CategoryReview_description_element = wait.until(ec.visibility_of_element_located((By.XPATH, self.CategoryReviewPage_Description_Xpath)))
        return bool(vtx_CategoryReview_description_element)

    def verify_main_menu_of_tax_categorizations_exists(self):
        wait = WebDriverWait(self.driver, 100)
        tc_main_menu = wait.until(ec.visibility_of_element_located((By.XPATH, self.Tax_Categorization_Main_Menu_Xpath)))
        return bool(tc_main_menu)

    def verify_broken_links_of_tax_categorizations_panel(self):
        all_links = self.driver.find_elements(By.XPATH, self.Tax_Categorizations_Links_Xpath)
        count = 0
        for link in all_links:
            url = link.get_attribute('href')
            res = requests.head(url)
            if res.status_code >= 400:
                print(url, "is a broken link")
                count += 1
            else:
                print(url, "is valid link")
        print("Total number of broken links:", count)

    def verify_number_of_links_listed_under_tax_categorizations_panel(self):
        all_links = self.driver.find_elements(By.XPATH, self.Tax_Categorizations_Links_Xpath)
        return len(all_links)

    def list_the_modules_under_tax_categorizations(self):
        all_links_text = self.driver.find_elements(By.XPATH, self.Tax_Categorizations_Links_Xpath)
        for link in all_links_text:
            print("The tax categorizations panel includes following modules:",link.text)

    def click_on_batch_number_column(self):
        self.driver.find_element(By.XPATH, self.Click_On_Batch_Number_Column_Xpath).click()

    def check_for_ascending_sorting_of_batch_number_column(self):
        asc_batch_numbers=self.driver.find_elements(By.XPATH, self.column_values_Xpath)
        asc_values=[int(asc_value.text) for asc_value in asc_batch_numbers]
        return asc_values

    def check_for_descending_sorting_of_batch_number_column(self):
        des_batch_numbers=self.driver.find_elements(By.XPATH, self.column_values_Xpath)
        desc_values=[int(des_value.text) for des_value in des_batch_numbers]
        return desc_values

    def click_on_added_date_and_time_filter_icon(self):
        self.driver.find_element(By.XPATH,self.added_date_time_filter_icon_Xpath).click()

    def select_filter_option_from_drp(self):
        wait = WebDriverWait(self.driver, 100)
        #filter_option = wait.until(ec.visibility_of_element_located((By.XPATH, self.filter_option_drp_Xpath)))
        filter_option = self.driver.find_element(By.XPATH, self.filter_option_drp_Xpath)
        filter_option.click()
        self.driver.find_element(By.XPATH,self.Equals_Xpath).click()
        # select_from_drp = Select(filter_option)
        # select_from_drp.select_by_visible_text("Equals")
        time.sleep(5)

    def select_date_to_be_filter_from_datepicker(self, month,year,day):
        self.driver.find_element(By.XPATH,self.date_picker_Xpath).click()
        datepicker_month=Select(self.driver.find_element(By.XPATH,self.date_picker_month_Xpath))
        datepicker_month.select_by_visible_text(month)
        datepicker_year = Select(self.driver.find_element(By.XPATH, self.date_picker_year_Xpath))
        datepicker_year.select_by_visible_text(year)
        all_dates=self.driver.find_elements(By.XPATH,self.date_picker_date_Xpath)
        for dt in all_dates:
            if dt.text==day:
                dt.click()
                break

    def click_on_filter_button(self):
        self.driver.find_element(By.XPATH,self.filter_btn_Xpath).click()


    def check_fiter_functionality_for_added_date_and_time_column(self,month,year,day):
        self.click_on_added_date_and_time_filter_icon()
        self.select_filter_option_from_drp()
        self.select_date_to_be_filter_from_datepicker(month,year,day)
        self.click_on_filter_button()

    def check_for_filter_result(self):
        filter_result=self.driver.find_element(By.XPATH,self.filter_result_Xpath)
        return filter_result.text



