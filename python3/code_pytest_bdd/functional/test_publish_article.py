import pytest

from pytest_bdd import scenario, given, when, then

# from urllib import urljoin
from pytest_bdd.feature import STEP_PREFIXES
from pytest_bdd import types

STEP_PREFIXES[:] = []

STEP_PREFIXES.append(('機能: ', 'feature'))
STEP_PREFIXES.append(('シナリオアウトライン: ', 'scenario outline'))
STEP_PREFIXES.append(('Examples: Vertical', 'examples vertical'))
STEP_PREFIXES.append(('例:', 'examples'))
STEP_PREFIXES.append(('シナリオ: ', 'scenario'))
STEP_PREFIXES.append(('背景:', 'background'))
STEP_PREFIXES.append(('前提 ', 'given'))
STEP_PREFIXES.append(('もし ', 'when'))
STEP_PREFIXES.append(('ならば ', 'then'))
STEP_PREFIXES.append(('@', 'tag'))
STEP_PREFIXES.append(('かつ ', None))
STEP_PREFIXES.append(('* ', None))
STEP_PREFIXES.append(('ただし ', None))


@pytest.fixture
def browser():
    return object()

@scenario('publish_article.feature', '記事を公開する')
def test_publish():
    pass


@given("ユーザは記事の執筆者")
def author_user(): # auth , author):
    #auth['user'] = author.user
    print("執筆sy")


@given('記事を持っている')
def article():
    print("記事1作成")


@when('書いた記事のページを開く')
def go_to_article(browser):
    #browser.visit(urljoin(browser.url, '/manage/articles/{0}/'.format(article.id)))
    # browser.visit("http://google.com")
    pass


@when('公開ボタンを押す')
def publish_article(browser):
    # browser.find_by_css('button[name=publish]').first.click()
    pass


@then('処理が正常に行われる')
def no_error_message(browser):
    # browser.find_by_css('.message.error').first
    pass


@then('記事が公開されている')
def article_is_published():
    # assert article.is_published
    print("published!")
