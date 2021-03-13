from pytest_bdd import scenarios, parsers, given, when, then
from cucumbers import CucumberBasket

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int
}

scenarios('../features/cucumbers_scenario_outline.feature', example_converters=CONVERTERS)


@given('the basket has "<initial>" cucumbers', target_fixture="basket")
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket, some):
    basket.add(some)


@when('"<some>" cucumbers are removed from the basket')
def remove_cucumbers(basket, some):
    basket.remove(some)


@then('the basket contains "<total>" cucumbers')
def basket_has_total(basket, total):
    assert basket.count == total
