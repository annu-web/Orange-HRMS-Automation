from selenium.webdriver.common.by import By


class LoginLocators:

    #login page locators

            L_usErname = (By.NAME,"username")
            L_pssword = (By.NAME,"password")
            L_loginbtn = (By.XPATH,"//button[@type='submit']")
            L_login_title = (By.LINK_TEXT,"Dashboard")
            L_invalid_crds = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
            L_reqrd_filds = (By.XPATH,"//input[@name='username']//parent::div//following-sibling::span[text()='Required']")

    #Admin Page locators

class Adminlocators:
           
           Admin_btn = (By.LINK_TEXT,"Admin")
           system_user_txt = (By.LINK_TEXT,"System Users")
           add_btn = (By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']")
           User_slct_drpdwn = (By.XPATH,"//label[text()='User Role']//parent::div['oxd-input-group__label-wrapper']//following-sibling::div//descendant::div[text()='-- Select --']")
           EmpName = (By.XPATH,"//input[@placeholder='Type for hints...']")
           #EmpName_1 = (By.CSS_SELECTOR,"div.oxd-autocomplete-wrapper")
           Emp_name_slct = (By.XPATH,"//div[@class='oxd-autocomplete-option']")
           Status_slct_drpdwn = (By.XPATH,"//label[text()='Status']//parent::div['oxd-input-group__label-wrapper']//following-sibling::div//descendant::div[text()='-- Select --']")
           Admin_pswd = (By.XPATH,"//label[text()='Password']//parent::div//following-sibling::div/input[@type='password']")
           Admin_confrm_pswd = (By.XPATH,"//label[text()='Confirm Password']//parent::div//following-sibling::div/input[@type='password']")
           Admin_sav_btn= (By.XPATH,"//button[@type='submit']")
           Admin_cancl_btn = (By.XPATH,"//button[text()=' Cancel ']")
           ESS_slct_btn = (By.XPATH,"(//span[text()='ESS'])")
           disabled_slct_btn= (By.XPATH,"(//span[text()='Disabled'])")
           admn_usrnme_slct = (By.XPATH,"//label[text()='Username']//parent::div//following-sibling::div/input")
           add_success_msg = (By.XPATH,"(//*[text()='Successfully Saved'])") 
           dlt_cancl_btn = (By.LINK_TEXT," No, Cancel ")

           #delete admin user locators

           #Admin_dlt_btn = (By.XPATH,"(//div[text()='Actions']//parent::div//parent::div//following-sibling::div[@class='oxd-table-body']//div[@class='oxd-table-row oxd-table-row--with-border'])[2]")
           Admin_dlt_btn = (By.XPATH,"(//i[@class='oxd-icon bi-trash'])")
           dlt_cnfrm_btn = (By.XPATH,"(//*[@class='oxd-icon bi-trash oxd-button-icon'])")
           success_msg = (By.XPATH,"(//*[text()='Successfully Deleted'])") 
           Admin_txt  = (By.XPATH,"//*[@class='oxd-table-card']//div[@class='oxd-table-cell oxd-padding-cell']")

           #adding admin user without fields locators

           Admin_reqrd_btn = (By.XPATH,"(//label[text()='User Role']//parent::div//following-sibling::span[text()='Required'])")
           Admin_pswd_nt_mtch = (By.XPATH,"(//span[text()='Passwords do not match'])")
 
           #edit admin user locators

           Admin_edit_btn = (By.XPATH,"(//button[@class='oxd-icon-button oxd-table-cell-action-space']//i[@class='oxd-icon bi-pencil-fill'])")
           Edit_success_msg = (By.XPATH,"(//*[text()='Successfully Updated'])")

           #admin search locators

           Admin_search = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
           Admin_reset_btn = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--ghost']")
           Admin_usrnme_result = (By.XPATH,"(//div[@class='oxd-table-cell oxd-padding-cell' and @role='cell'])[2]")
           Admn_checkbx = (By.XPATH,"//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']")
           Admn_invalid_srch = (By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message' and text()='Invalid']")
           No_info_found_msg = (By.XPATH,"(//*[text()='No Records Found'])")
           Admn_user_role_verify = (By.XPATH,"//div[@class='oxd-table-cell oxd-padding-cell']/div[text()='ESS']")

           
class  Job_titlelocator:
            
           #Job title locators

           Job_btn = (By.XPATH,"//*[@class='oxd-topbar-body-nav-tab-item' and text()='Job ']")
           job_title_txt = (By.LINK_TEXT,"Job Titles")
           job_title_ele = (By.XPATH,"//h6[text()='Job Titles']")
           add_job_ttle_txt= (By.XPATH,"//h6[text()='Add Job Title']")
           job_add_btn = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
           add_jb_ttle_txt = (By.XPATH,"//h6[text()='Add Job Title']")
           jb_ttle_entry = (By.XPATH,"//div[@class='oxd-input-group__label-wrapper']//following::div//input")
           jb_descrptn_entry = (By.XPATH,"//textarea[@placeholder='Type description here']")
           add_nte_btn = (By.XPATH,"//textarea[@placeholder='Add note']")
           jb_ttle_sve_btn = (By.XPATH,"//button[@type='submit']")
           ttle_upload_fle= (By.XPATH,"//div[@class='oxd-file-button' and text()='Browse']")
           jb_rqrd_btn = (By.XPATH,"//span[text()='Required']")


           cncl_btn = (By.LINK_TEXT," Cancel ")
           chnge_pswd_chckbx= (By.XPATH,"//span[@class='oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input']")
           yes_cncl_btn = (By.LINK_TEXT," No, Cancel ")
           list_sort_btn = (By.XPATH,"//i[@class='oxd-icon bi-sort-alpha-down oxd-icon-button__icon oxd-table-header-sort-icon']")
           descending_btn = (By.LINK_TEXT,"Descending")
           Alrdy_exist_msg = (By.XPATH,"//span[text()='Already exists']")
           dlt_cncl_btn= (By.XPATH,"//button[text()=' No, Cancel ']")
           #jb_ttle_chckboxes = (By.XPATH,"//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']")
           jb_ttle_checkbox = (By.XPATH,"(//div[@class='oxd-table-header-cell oxd-padding-cell oxd-table-th'])[1]")
           dlt_selected_chckboxs = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")

class branding():
        
        crprte_brndng_btn = (By.LINK_TEXT,"Corporate Branding")
        prmry_fnt_clr = (By.XPATH,"//label[text()='Primary Font Color']//following-sibling::div")
        prmry_fnt_clr_1 = (By.XPATH,"//label[text()='Primary Font Color']//following-sibling::div/div")
        scndry_fnt_clr= (By.XPATH,"//label[text()='Secondary Font Color']//following-sibling::div")
        scndry_fnt_clr_1 = (By.XPATH,"//label[text()='Secondary Font Color']//following-sibling::div/div")
        scial_mda_tgle_btn = (By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--focus --label-right']")
        clint_logo_upld_btn = (By.XPATH,"//label[text()='Client Logo']//parent::div//following::div/div")
        login_banner_uplod_btn = (By.XPATH,"//label[text()='Login Banner']//parent::div//following-sibling::div//div")
        rst_to_dfult = (By.XPATH,"//button[text()=' Reset to Default ']")
        prview_btn = (By.XPATH,"//button[text()=' Preview ']")
        pblsh_btn = (By.XPATH,"//button[@type='submit' and @class='oxd-button oxd-button--medium oxd-button--secondary' and text()=' Publish ']")
        header_bckgrnd_clr = (By.XPATH,"//div[@class='oxd-topbar-header']")
        hex_clr_input_bx = (By.XPATH,"//label[text()='HEX']//following::input")
        dlt_crnt_radio_btn = (By.XPATH,"input[type='radio'][value='deleteCurrent']")
        doc_preview_btn = (By.XPATH,"//div[@class='orangehrm-file-preview']")
        form_pg = (By.XPATH,"//form[@class='oxd-form']")