from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.CSS_SELECTOR,
                    'a.home-link2.headline__personal-enter.headline__personal-enter.home-link2_color_black')
    LOGIN_FIELD = (By.CLASS_NAME, 'Textinput-Control')
    CHOOSE_EMAIL_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button')
    EMAIL_LOGIN_BUTTON = (By.CSS_SELECTOR, '#passp\:sign-in')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'data-testid="logout"')
    PASSWORD_FIELD = (By.ID, 'passp-field-passwd')
    LOGIN_AUTOFILL = (By.ID, 'login')
    PHONE_SUBMIT = (By.CSS_SELECTOR, 'type=submit')
    AVATAR = (By.CSS_SELECTOR, 'body > main > div.headline > div > a.home-link2.headline__personal-avatar.usermenu-portal.i-bem.avatar.avatar_size_adaptive.usermenu-portal_js_inited')
    DISK_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/a[4]')
    CLOSE_ADS = (By.CSS_SELECTOR, 'aria-label="Закрыть"')
    BUTTON_CREATE = (By.CLASS_NAME, 'create-resource-popup-with-anchor')
    CREATE_FOLDER = (By.CSS_SELECTOR, 'body > div.Popup2.Popup2_visible.Popup2_target_anchor.Popup2_view_default.create-resource-popup-with-anchor__popup > div > button:nth-child(1)')
    RENAME_FIELD = (By.CSS_SELECTOR, 'body > div.Modal.Modal_visible.Modal_hasAnimation.Modal_theme_normal.dialog.confirmation-dialog.resource-rename-dialog.js-prevent-deselect > div.Modal-Wrapper > div > div > div > div > div > div.confirmation-dialog__content > div > form > span > input')
    RENAME_BUTTON = (By.CSS_SELECTOR, 'body > div.Modal.Modal_visible.Modal_hasAnimation.Modal_theme_normal.dialog.confirmation-dialog.resource-rename-dialog.js-prevent-deselect > div.Modal-Wrapper > div > div > div > div > div > div.confirmation-dialog__footer > button')
    FOLDER = (By.CSS_SELECTOR, '#app > div > div > div.root__content.root__content_has-bottom-ad.root__content_page_listing > div.root__content-wrap > div.root__content-inner.root__content-inner_page_listing > div > div > div.listing.listing_with-mouse-selection.listing_with-drag-and-drop.listing_theme_tile.listing_completed > div > div.listing-item.listing-item_theme_tile.listing-item_size_m.listing-item_type_dir.listing-item_selected.js-prevent-deselect')
    SELECTED_FOLDER = (By.CSS_SELECTOR, '#app > div > div > div.root__content.root__content_has-bottom-ad.root__content_page_listing > div.root__content-wrap > div.root__content-inner.root__content-inner_page_listing > div > div > div.listing.listing_with-mouse-selection.listing_with-drag-and-drop.listing_theme_tile.listing_completed > div > div.listing-item.listing-item_theme_tile.listing-item_size_m.listing-item_type_dir.listing-item_selected.js-prevent-deselect')
    RENAME_DOC_FIELD = (By.CSS_SELECTOR, 'body > div.Modal.Modal_visible.Modal_hasAnimation.Modal_theme_normal.dialog.confirmation-dialog.Document-Title-Dialog.js-prevent-deselect > div.Modal-Wrapper > div > div > div > div > div > div.confirmation-dialog__content > div > form > span > input')
    CREATE_DOC = (By.CSS_SELECTOR, 'body > div.Popup2.Popup2_visible.Popup2_target_anchor.Popup2_view_default.create-resource-popup-with-anchor__popup > div > button:nth-child(2)')
    CREATE_DOC_BUTTON = (By.CSS_SELECTOR, 'body > div.Modal.Modal_visible.Modal_hasAnimation.Modal_theme_normal.dialog.confirmation-dialog.Document-Title-Dialog.js-prevent-deselect > div.Modal-Wrapper > div > div > div > div > div > div.confirmation-dialog__footer > button')
    CAPTCHA_CHECKBOX = (By.CLASS_NAME, 'CheckboxCaptcha-Button')
    NOT_NOW = (By.CLASS_NAME, 'Button2.Button2_size_l.Button2_view_pseudo.Button2_width_max')
    DOC_NAME = (By.CSS_SELECTOR, '#app > div > div > div.root__content.root__content_has-bottom-ad.root__content_page_listing > div.root__content-wrap > div.root__content-inner.root__content-inner_page_listing > div > div > div.listing.listing_with-mouse-selection.listing_with-drag-and-drop.listing_theme_tile.listing_completed > div > div.listing-item.listing-item_theme_tile.listing-item_size_m.listing-item_type_file.js-prevent-deselect > div.listing-item__info > div > span')
