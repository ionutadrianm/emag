from behave import *


@then('compare: I verify that the title is correct')
def step_impl(context):
    context.compare_page.verify_that_title_is_correct()
