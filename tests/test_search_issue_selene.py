from selene import be, by
from selene.support.shared import browser


def test_search_issue_selene():
    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('.QueryBuilder-Input').send_keys('allure-framework/allure-python')
    browser.element('.QueryBuilder-Input').submit()

    browser.element(by.partial_link_text('allure-framework/allure-python')).click()
    browser.element('#issues-tab').click()

    assert browser.element(by.partial_text('Mark high level step as failed')).should(be.visible)
