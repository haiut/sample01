from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_trdemo_client(unittest.TestCase):

    @clear_session({'spanId': 1})
    def test_01_get_(self):
        # GET http://trdemo-client/ (endp 1)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        resp = trdemo_client.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @clear_session({'spanId': 2})
    def test_02_get_cart(self):
        # GET http://trdemo-client/cart (endp 2)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        resp = trdemo_client.get('/cart')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @json_dataset('data/dataset_3.json')
    @clear_session({'spanId': 3})
    def test_03_get_cart_remove_flight_id(self, data_row):
        flight_id, = data_row

        # GET http://trdemo-client/cart/remove/{flight_id} (endp 3)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        resp = trdemo_client.get(f'/cart/remove/{flight_id}')
        resp.assert_ok()
        # resp.assert_status_code(302)

    @json_dataset('data/dataset_4.json')
    @clear_session({'spanId': 4})
    def test_04_get_flight(self, data_row):
        flight_id, = data_row

        # GET http://trdemo-client/flight (endp 4)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        qstr = '?' + urlencode([('flight_id', flight_id)])
        resp = trdemo_client.get('/flight' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    # authentication-related test
    @clear_session({'spanId': 5})
    def test_05_get_login(self):
        # GET http://trdemo-client/login (endp 5)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', dummy_auth)
        resp = trdemo_client.get('/login')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div#logreg-forms h1.h3.font-weight-normal', expected_value=' Select user (temp) ')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    # authentication-related test
    @json_dataset('data/dataset_6.json')
    @clear_session({'spanId': 6})
    def test_06_post_login(self, data_row):
        user, = data_row

        # POST http://trdemo-client/login (endp 6)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', dummy_auth)
        resp = trdemo_client.post('/login', data=[('user', user)])
        resp.assert_ok()
        # resp.assert_status_code(302)

    # authentication-related test
    @clear_session({'spanId': 7})
    def test_07_get_logout(self):
        # GET http://trdemo-client/logout (endp 7)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', dummy_auth)
        resp = trdemo_client.get('/logout')
        resp.assert_ok()
        # resp.assert_status_code(302)

    @json_dataset('data/dataset_8.json')
    @clear_session({'spanId': 8})
    def test_08_get_search(self, data_row):
        destination, source, startDate = data_row

        # GET http://trdemo-client/search (endp 8)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        qstr = '?' + urlencode([('destination', destination), ('endDate', ''), ('source', source), ('startDate', startDate)])
        resp = trdemo_client.get('/search' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_9.json')
    @clear_session({'spanId': 9})
    def test_09_get_cart_add(self, data_row):
        product_id, = data_row

        # GET http://trdemo-client/cart/add (endp 9)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        qstr = '?' + urlencode([('product_id', product_id)])
        resp = trdemo_client.get('/cart/add' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(302)

    @clear_session({'spanId': 10})
    def test_10_get_cart_create(self):
        # GET http://trdemo-client/cart/create (endp 10)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        resp = trdemo_client.get('/cart/create')
        resp.assert_ok()
        # resp.assert_status_code(302)


@data_driven_tests
class Tests_trdemo_flights(unittest.TestCase):

    @json_dataset('data/dataset_11.json')
    @clear_session({'spanId': 11})
    def test_11_get_flight_product_id_param(self, data_row):
        param, product_id = data_row

        # GET http://trdemo-flights/flight/{product_id}/{param} (endp 11)
        trdemo_flights = get_http_target('TARGET_TRDEMO_FLIGHTS', authenticate)
        resp = trdemo_flights.get(f'/flight/{product_id}/{param}')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_12.json')
    @clear_session({'spanId': 12})
    def test_12_get_flight_product_id(self, data_row):
        product_id, = data_row

        # GET http://trdemo-flights/flight/{product_id} (endp 12)
        trdemo_flights = get_http_target('TARGET_TRDEMO_FLIGHTS', authenticate)
        resp = trdemo_flights.get(f'/flight/{product_id}')
        resp.assert_ok()
        # resp.assert_status_code(200)


@data_driven_tests
class Tests_trdemo_shoppingcart(unittest.TestCase):

    @json_dataset('data/dataset_15.json')
    @clear_session({'spanId': 15})
    def test_15_get_cart_email(self, data_row):
        email_, = data_row

        # GET http://trdemo-shoppingcart/cart/{email} (endp 15)
        trdemo_shoppingcart = get_http_target('TARGET_TRDEMO_SHOPPINGCART', authenticate)
        resp = trdemo_shoppingcart.get(f'/cart/{email_}')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_16.json')
    @clear_session({'spanId': 16})
    def test_16_delete_cart_email_product_id(self, data_row):
        email_, product_id = data_row

        # DELETE http://trdemo-shoppingcart/cart/{email}/{product_id} (endp 16)
        trdemo_shoppingcart = get_http_target('TARGET_TRDEMO_SHOPPINGCART', authenticate)
        resp = trdemo_shoppingcart.delete(f'/cart/{email_}/{product_id}')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_17.json')
    @clear_session({'spanId': 17})
    def test_17_post_cart_email(self, data_row):
        email_, = data_row

        # POST http://trdemo-shoppingcart/cart/{email} (endp 17)
        trdemo_shoppingcart = get_http_target('TARGET_TRDEMO_SHOPPINGCART', authenticate)
        resp = trdemo_shoppingcart.post(f'/cart/{email_}')
        resp.assert_ok()
        # resp.assert_status_code(201)

    @json_dataset('data/dataset_18.json')
    @clear_session({'spanId': 18})
    def test_18_put_cart_email(self, data_row):
        email_, product_id = data_row

        # PUT http://trdemo-shoppingcart/cart/{email} (endp 18)
        trdemo_shoppingcart = get_http_target('TARGET_TRDEMO_SHOPPINGCART', authenticate)
        with open('data/payload_for_endp_18.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.product_id', product_id)
        resp = trdemo_shoppingcart.put(f'/cart/{email_}', json=json_payload)
        resp.assert_ok()
        # resp.assert_status_code(201)


@data_driven_tests
class Tests_trdemo_users(unittest.TestCase):

    @json_dataset('data/dataset_13.json')
    @clear_session({'spanId': 13})
    def test_13_get_user_email(self, data_row):
        email_, = data_row

        # GET http://trdemo-users/user/{email} (endp 13)
        trdemo_users = get_http_target('TARGET_TRDEMO_USERS', authenticate)
        resp = trdemo_users.get(f'/user/{email_}')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 14})
    def test_14_get_user_all(self):
        # GET http://trdemo-users/user/all (endp 14)
        trdemo_users = get_http_target('TARGET_TRDEMO_USERS', authenticate)
        resp = trdemo_users.get('/user/all')
        resp.assert_ok()
        # resp.assert_status_code(200)
