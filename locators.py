from selenium.webdriver.common.by import By

class Locators():
    # --- Account Page Locators ---
    GOOGLE_SSO=(By.XPATH, '//*[@id="sso_providers"]/a[1]/i/img')
    OFFICE365_SSO=(By.XPATH,'//*[@id="sso_providers"]/a[2]/i/img')

    # -- Google Sign In Locators ---
    GOOGLE_ID_TEXTBOX=(By.ID, 'identifierId')
    GOOGLE_NEXT_BUTTON_1=(By.CSS_SELECTOR, '#identifierNext > span:nth-child(3)')
    GOOGLE_PASSWORD_TEXBOX=(By.NAME, 'password')
    GOOGLE_NEXT_BUTTON_2=(By.CSS_SELECTOR, '#passwordNext > span:nth-child(3)')

    # -- Office365 Sign In Locators ---
    OFFICE365_ID_TEXTBOX=(By.ID, 'i0116')
    OFFICE365_NEXT_BUTTON=(By.ID, 'idSIButton9')
    OFFICE365_PASSWORD_TEXTBOX=(By.ID, 'i0118')