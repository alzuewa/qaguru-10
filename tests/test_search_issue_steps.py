import allure
from selene import be, by
from selene.support.shared import browser

from ui_helpers import steps


def test_search_issue_dynamic_steps():
    with allure.step('Open GitHub main page'):
        browser.open('https://github.com')

    with allure.step('Input search request with repo name'):
        browser.element('.header-search-button').click()
        browser.element('.QueryBuilder-Input').send_keys('allure-framework/allure-python')
        browser.element('.QueryBuilder-Input').submit()

    with allure.step('Click by link with repo name'):
        browser.element(by.partial_link_text('allure-framework/allure-python')).click()

    with allure.step('Switch to [Issues] tab'):
        browser.element('#issues-tab').click()

    with allure.step('Assert target issue is present'):
        browser.element(by.partial_text('Mark high level step as failed')).should(be.visible)


def test_search_issue_decorator_steps():
    steps.open_github()
    steps.input_search_query(repo_name='allure-framework/allure-python')
    steps.open_repo_page(repo_name='allure-framework/allure-python')
    steps.open_issues_tab()
    steps.assert_issue_visibility(issue_text='Mark high level step as failed')
