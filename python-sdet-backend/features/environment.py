def before_scenario(context, scenario):
    print('before_scenario')


def after_scenario(context, scenario):
    print('after_scenario')
    print(f"New User Id: {context.userId}")
