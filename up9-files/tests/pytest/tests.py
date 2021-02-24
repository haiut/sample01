from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_carts_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_4.json')
    @clear_session({'spanId': 4})
    def test_04_get_carts_id_items(self, data_row):
        id_, = data_row

        # GET http://carts.sock-shop/carts/{id}/items (endp 4)
        carts_sock_shop = get_http_target('TARGET_CARTS_SOCK_SHOP', authenticate)
        resp = carts_sock_shop.get(f'/carts/{id_}/items', headers=dict([('accept', 'application/json')]))
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_10.json')
    @clear_session({'spanId': 10})
    def test_10_delete_carts_id(self, data_row):
        id_, = data_row

        # DELETE http://carts.sock-shop/carts/{id} (endp 10)
        carts_sock_shop = get_http_target('TARGET_CARTS_SOCK_SHOP', authenticate)
        resp = carts_sock_shop.delete(f'/carts/{id_}')
        resp.assert_ok()
        # resp.assert_status_code(202)

    @json_dataset('data/dataset_11.json')
    @clear_session({'spanId': 11})
    def test_11_post_carts_id_items(self, data_row):
        id_, itemId, unitPrice = data_row

        # POST http://carts.sock-shop/carts/{id}/items (endp 11)
        carts_sock_shop = get_http_target('TARGET_CARTS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_11.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.itemId', itemId)
        apply_into_json(json_payload, '$.unitPrice', unitPrice)
        resp = carts_sock_shop.post(f'/carts/{id_}/items', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_ok()
        # resp.assert_status_code(201)

    @json_dataset('data/dataset_12.json')
    @clear_session({'spanId': 12})
    def test_12_patch_carts_id_items(self, data_row):
        id_, itemId, quantity, unitPrice = data_row

        # PATCH http://carts.sock-shop/carts/{id}/items (endp 12)
        carts_sock_shop = get_http_target('TARGET_CARTS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_12.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.itemId', itemId)
        apply_into_json(json_payload, '$.quantity', quantity)
        apply_into_json(json_payload, '$.unitPrice', unitPrice)
        resp = carts_sock_shop.patch(f'/carts/{id_}/items', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_ok()
        # resp.assert_status_code(202)

    @json_dataset('data/dataset_13.json')
    @clear_session({'spanId': 13})
    def test_13_delete_carts_id_items_itemId(self, data_row):
        id_, itemId = data_row

        # DELETE http://carts.sock-shop/carts/{id}/items/{itemId} (endp 13)
        carts_sock_shop = get_http_target('TARGET_CARTS_SOCK_SHOP', authenticate)
        resp = carts_sock_shop.delete(f'/carts/{id_}/items/{itemId}')
        resp.assert_ok()
        # resp.assert_status_code(202)

    @json_dataset('data/dataset_14.json')
    @clear_session({'spanId': 14})
    def test_14_get_carts_id_merge(self, data_row):
        id_, sessionId = data_row

        # GET http://carts.sock-shop/carts/{id}/merge (endp 14)
        carts_sock_shop = get_http_target('TARGET_CARTS_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('sessionId', sessionId)])
        resp = carts_sock_shop.get(f'/carts/{id_}/merge' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(202)


@data_driven_tests
class Tests_catalogue_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_1.json')
    @clear_session({'spanId': 1})
    def test_01_get_catalogue_id(self, data_row):
        id_, = data_row

        # GET http://catalogue.sock-shop/catalogue/{id} (endp 1)
        catalogue_sock_shop = get_http_target('TARGET_CATALOGUE_SOCK_SHOP', authenticate)
        resp = catalogue_sock_shop.get(f'/catalogue/{id_}')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_2.json')
    @clear_session({'spanId': 2})
    def test_02_get_catalogue(self, data_row):
        size, tags = data_row

        # GET http://catalogue.sock-shop/catalogue (endp 2)
        catalogue_sock_shop = get_http_target('TARGET_CATALOGUE_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('page', '1'), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = catalogue_sock_shop.get('/catalogue' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 6})
    def test_06_get_catalogue_size(self):
        # GET http://catalogue.sock-shop/catalogue/size (endp 6)
        catalogue_sock_shop = get_http_target('TARGET_CATALOGUE_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('tags', '')])
        resp = catalogue_sock_shop.get('/catalogue/size' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 8})
    def test_08_get_tags(self):
        # GET http://catalogue.sock-shop/tags (endp 8)
        catalogue_sock_shop = get_http_target('TARGET_CATALOGUE_SOCK_SHOP', authenticate)
        resp = catalogue_sock_shop.get('/tags')
        resp.assert_ok()
        # resp.assert_status_code(200)


@data_driven_tests
class Tests_front_end_sock_shop(unittest.TestCase):

    @clear_session({'spanId': 3})
    def test_03_get_(self):
        # GET http://front-end.sock-shop/ (endp 3)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')


@data_driven_tests
class Tests_orders_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_21.json')
    @clear_session({'spanId': 21})
    def test_21_post_orders(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 21)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_21.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_ok()
        # resp.assert_status_code(201)
        # resp.assert_jsonpath('$.address.city', expected_value='NYC')

    @json_dataset('data/dataset_22.json')
    @clear_session({'spanId': 22})
    def test_22_get_orders_id(self, data_row):
        id_, = data_row

        # GET http://orders.sock-shop/orders/{id} (endp 22)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        resp = orders_sock_shop.get(f'/orders/{id_}')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.address.city', expected_value='NYC')

    @json_dataset('data/dataset_23.json')
    @clear_session({'spanId': 23})
    def test_23_get_orders_search_customerId(self, data_row):
        custId, = data_row

        # GET http://orders.sock-shop/orders/search/customerId (endp 23)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('custId', custId), ('sort', 'date')])
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$._embedded.customerOrders.[*].address.city', expected_value='NYC')


@data_driven_tests
class Tests_payment_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_26.json')
    @clear_session({'spanId': 26})
    def test_26_post_paymentAuth(self, data_row):
        amount, ccv, expires, id_, id1, id2, longNum, number, postcode = data_row

        # POST http://payment.sock-shop/paymentAuth (endp 26)
        payment_sock_shop = get_http_target('TARGET_PAYMENT_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_26.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address.id', id_)
        apply_into_json(json_payload, '$.address.number', number)
        apply_into_json(json_payload, '$.address.postcode', postcode)
        apply_into_json(json_payload, '$.amount', amount)
        apply_into_json(json_payload, '$.card.ccv', ccv)
        apply_into_json(json_payload, '$.card.expires', expires)
        apply_into_json(json_payload, '$.card.id', id1)
        apply_into_json(json_payload, '$.card.longNum', longNum)
        apply_into_json(json_payload, '$.customer.id', id2)
        resp = payment_sock_shop.post('/paymentAuth', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_ok()
        # resp.assert_status_code(200)


@data_driven_tests
class Tests_shipping_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_27.json')
    @clear_session({'spanId': 27})
    def test_27_post_shipping(self, data_row):
        id_, name = data_row

        # POST http://shipping.sock-shop/shipping (endp 27)
        shipping_sock_shop = get_http_target('TARGET_SHIPPING_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_27.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', id_)
        apply_into_json(json_payload, '$.name', name)
        resp = shipping_sock_shop.post('/shipping', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_ok()
        # resp.assert_status_code(201)


@data_driven_tests
class Tests_user_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_15.json')
    @clear_session({'spanId': 15})
    def test_15_post_addresses(self, data_row):
        number, postcode, userID = data_row

        # POST http://user.sock-shop/addresses (endp 15)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_15.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.number', number)
        apply_into_json(json_payload, '$.postcode', postcode)
        apply_into_json(json_payload, '$.userID', userID)
        resp = user_sock_shop.post('/addresses', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_16.json')
    @clear_session({'spanId': 16})
    def test_16_post_cards(self, data_row):
        ccv, expires, longNum, userID = data_row

        # POST http://user.sock-shop/cards (endp 16)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_16.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.ccv', ccv)
        apply_into_json(json_payload, '$.expires', expires)
        apply_into_json(json_payload, '$.longNum', longNum)
        apply_into_json(json_payload, '$.userID', userID)
        resp = user_sock_shop.post('/cards', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_17.json')
    @clear_session({'spanId': 17})
    def test_17_get_customers_id(self, data_row):
        id_, = data_row

        # GET http://user.sock-shop/customers/{id} (endp 17)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        resp = user_sock_shop.get(f'/customers/{id_}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.username', expected_value='alex')

    @json_dataset('data/dataset_18.json')
    @clear_session({'spanId': 18})
    def test_18_get_customers_id_addresses(self, data_row):
        id_, = data_row

        # GET http://user.sock-shop/customers/{id}/addresses (endp 18)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        resp = user_sock_shop.get(f'/customers/{id_}/addresses')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$._embedded.address.[*].city', expected_value='NYC')

    @json_dataset('data/dataset_19.json')
    @clear_session({'spanId': 19})
    def test_19_get_customers_id_cards(self, data_row):
        id_, = data_row

        # GET http://user.sock-shop/customers/{id}/cards (endp 19)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        resp = user_sock_shop.get(f'/customers/{id_}/cards')
        resp.assert_ok()
        # resp.assert_status_code(200)

    # authentication-related test
    @clear_session({'spanId': 20})
    def test_20_post_register(self):
        # POST http://user.sock-shop/register (endp 20)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', dummy_auth)
        with open('data/payload_for_endp_20.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        resp = user_sock_shop.post('/register', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_24.json')
    @clear_session({'spanId': 24})
    def test_24_get_addresses_addresseId(self, data_row):
        addresseId, = data_row

        # GET http://user.sock-shop/addresses/{addresseId} (endp 24)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        resp = user_sock_shop.get(f'/addresses/{addresseId}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.city', expected_value='NYC')

    @json_dataset('data/dataset_25.json')
    @clear_session({'spanId': 25})
    def test_25_get_cards_cardId(self, data_row):
        cardId, = data_row

        # GET http://user.sock-shop/cards/{cardId} (endp 25)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        resp = user_sock_shop.get(f'/cards/{cardId}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_ok()
        # resp.assert_status_code(200)
