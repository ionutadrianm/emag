from behave import *


@when('products: I add product to basket "{product_name}"')
def step_impl(context, product_name):
    context.products_page.add_to_basket_by_partial_product_name(product_name)


@when('products: I click Vezi detalii cos')
def step_impl(context):
    context.products_page.click_vezi_detalii_cos()


@when('products: I select for comparison item "{product_index}"')
def step_impl(context, product_index):
    context.products_page.select_for_comparison(int(product_index))

@when('products: I click Compara button')
def step_impl(context):
    context.products_page.click_compara_button()


@then('products: I verify that results contain search query "{query}"')
def step_impl(context, query):
    context.products_page.verify_results_contain_text(query)
