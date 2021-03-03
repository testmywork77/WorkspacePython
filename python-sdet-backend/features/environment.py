# Hooks done by environment.py user-defined python module
# environment.py is a convention by name
# Integrate Hooks and Tags
def before_scenario(context, scenario):
    if "smoke" in scenario.tags:
        print(f'before_scenario: smoke')
    elif "regression":
        print(f'before_scenario: regression')


def after_scenario(context, scenario):
    if "smoke" in scenario.tags:
        print(f'after_scenario: smoke')
        print(f"New User Id: {context.userId}")
    elif "regression":
        print(f'after_scenario: regression')
        print(f"New User Id: {context.userId}")