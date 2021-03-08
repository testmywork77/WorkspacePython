from pytest_bdd import scenario, given, when, then


@scenario('../features/publish_article.feature', 'Publishing the article')
def test_publish():
    pass


@given("I'm an author user")
def author_user():
    pass


@given("I have an article", target_fixture="article")
def article():
    pass


@when("I go to the article page")
def go_to_article(article):
    pass


@when("I press the publish button")
def publish_article(article):
    pass


@then("I should not see the error message")
def no_error_message(article):
   pass


@then("the article should be published")
def article_is_published(article):
   pass