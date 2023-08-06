Feature: Emag compare feature

  Background:
    Given home: I am a user on emag.ro Home page

    @compare_iphones
    Scenario: Compare 2 iphones
      When home: I search after "iphone"
      When products: I select for comparison item "2"
      When products: I select for comparison item "4"
      When products: I click Compara button
      Then compare: I verify that the title is correct

