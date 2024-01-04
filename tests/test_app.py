def test_post_create_customers(db_connection, web_client):
    db_connection.seed('seeds/BankingCustomers.sql')
    post_response = web_client.post("/customers", data={
        "firstname": "Leah",
        "lastname": "Hartley",
        "contactnumber": "+447732443654"
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get('/customers')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == (
    "Customers(1, Leah, Southern, +447732443654)\n"
    "Customers(2, John, Doe, +447932445396)\n"
    "Customers(3, Alan, Carr, +447921124786)\n"
    "Customers(4, Leah, Hartley, +447732443654)"
)
def test_no_data(db_connection, web_client):
    db_connection.seed('seeds/BankingCustomers.sql')
    post_response = web_client.post("/customers")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == \
        "You need to input customer Data"
    
    get_response = web_client.get('/customers')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == (
    "Customers(1, Leah, Southern, +447732443654)\n"
    "Customers(2, John, Doe, +447932445396)\n"
    "Customers(3, Alan, Carr, +447921124786)"
)