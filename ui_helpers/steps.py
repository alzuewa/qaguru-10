import allure
from selene import be, by
from selene.support.shared import browser


@allure.step('Open GitHub main page')
def open_github():
    browser.open('https://github.com')


@allure.step('Input search request with repo name: {repo_name}')
def input_search_query(repo_name: str):
    browser.element('.header-search-button').click()
    browser.element('.QueryBuilder-Input').send_keys(repo_name)
    browser.element('.QueryBuilder-Input').submit()


@allure.step('Open repository page: {repo_name}')
def open_repo_page(repo_name: str):
    browser.element(by.partial_link_text(repo_name)).click()


@allure.step('Switch to [Issues] tab')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Assert target issue with text {issue_text} is present')
def assert_issue_visibility(issue_text: str):
    browser.element(by.partial_text(issue_text)).should(be.visible)
