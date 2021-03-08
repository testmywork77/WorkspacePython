from pytest_bdd import scenario, parsers, given, when, then
from cucumbers import CucumberBasket


@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add():
    pass


@given("the basket has 2 cucumbers", target_fixture="basket")
def basket():
    return CucumberBasket(initial_count=2)


@when("4 cucumbers are added to the basket")
def add_cucumbers(basket):
    basket.add(4)


@then("the basket contains 6 cucumbers")
def basket_has_total(basket):
    assert basket.count == 6


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=dict(Number=int)),
       target_fixture="basket")
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=dict(Number=int)))
def add_cucumbers(basket, some):
    basket.add(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=dict(Number=int)))
def basket_has_total(basket, total):
    assert basket.count == total
