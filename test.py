def test_for_all_accounts(db_connection):
    db_connection.seed("seeds/BankingCustomers.sql")
    repository = AccountsRepository(db_connection)
    result = repository.all()
    
    expected_accounts = [
        Accounts(1, 'Premier', 2009223, '£', 3000.00, 1),
        Accounts(2, 'Savings', 3009004, '£', 5000.00, 2),
        Accounts(3, 'Black', 4332367, '£', 10000.00, 3),
        Accounts(4, 'Ruby', 2076554, '£', 11245.20, 1)
    ]

    differences_found = False

    for i, (result_account, expected_account) in enumerate(zip(result, expected_accounts)):
        if result_account != expected_account:
            print(f"Difference at index {i}:")
            print(f"Result: {result_account.__dict__}")
            print(f"Expected: {expected_account.__dict__}")
            differences_found = True

    if differences_found:
        assert result == expected_accounts
