from pytest_bdd import scenarios, scenario, parsers, given, when, then
from cucumbers import CucumberBasket

scenarios('../features/cucumbers_parameterize.feature')
EXTRA_TYPES = {
    'Number': int,
}

'''
As more tests are added to the feature file, it becomes a little cumbersome 
to always add a new test function for every single scenario.
We like to follow the principle of don't repeat yourself, and most times, we want to include all of the
scenarios in the feature file when we've run our tests. Thankfully, pytest-bdd includes a helper function to do this.

It's called the scenarios function
scenarios('../features/cucumbers_parameterize.feature')

@scenario('../features/cucumbers_parameterize.feature', 'Add cucumbers to a basket')
def test_add():
    pass


@scenario('../features/cucumbers_parameterize.feature', 'Remove cucumbers from a basket')
def test_remove():
    pass
'''


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES), target_fixture="basket")
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
def add_cucumbers(basket, some):
    basket.add(some)


@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total
