import allure
from allure import severity_level

from ui_helpers import steps


def test_search_issue_dynamic_labels():
    allure.dynamic.tag('tabs', 'issues')
    allure.dynamic.suite('Acceptance')
    allure.dynamic.description('Check that issue titles are visible')
    allure.dynamic.severity(severity_level.CRITICAL)
    allure.dynamic.feature('Issues')
    allure.dynamic.story('User can see issue list with titles')
    allure.dynamic.link('https://github.com', name='Testing')

    steps.open_github()
    steps.input_search_query(repo_name='allure-framework/allure-python')
    steps.open_repo_page(repo_name='allure-framework/allure-python')
    steps.open_issues_tab()
    steps.assert_issue_visibility(issue_text='Mark high level step as failed')


@allure.tag('tabs', 'issues')
@allure.suite('Acceptance')
@allure.description('Check that issue titles are visible')
@allure.severity(severity_level.CRITICAL)
@allure.feature('Issues')
@allure.story('User can see issue list with titles')
@allure.link('https://github.com', name='Testing')
def test_search_issue_decorator_labels():
    steps.open_github()
    steps.input_search_query(repo_name='allure-framework/allure-python')
    steps.open_repo_page(repo_name='allure-framework/allure-python')
    steps.open_issues_tab()
    steps.assert_issue_visibility(issue_text='Mark high level step as failed')
