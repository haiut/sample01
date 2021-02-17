from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_trdemo_client(unittest.TestCase):

    @clear_session({'spanId': 1})
    def test_1_get_(self):
        # GET http://trdemo-client/ (endp 1)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        resp = trdemo_client.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @clear_session({'spanId': 2})
    def test_2_get_cart(self):
        # GET http://trdemo-client/cart (endp 2)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        resp = trdemo_client.get('/cart')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.container-fluid div h2', expected_value='Cart for alex.haiut@testr.io')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @json_dataset('data/dataset_3.json')
    @clear_session({'spanId': 3})
    def test_3_get_flight(self, data_row):
        flight_id, = data_row

        # GET http://trdemo-client/flight (endp 3)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        qstr = '?' + urlencode([('flight_id', flight_id)])
        resp = trdemo_client.get('/flight' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @json_dataset('data/dataset_4.json')
    @clear_session({'spanId': 4})
    def test_4_get_search(self, data_row):
        startDate, = data_row

        # GET http://trdemo-client/search (endp 4)
        trdemo_client = get_http_target('TARGET_TRDEMO_CLIENT', authenticate)
        qstr = '?' + urlencode([('destination', '*'), ('endDate', ''), ('source', '*'), ('startDate', startDate)])
        resp = trdemo_client.get('/search' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)


@data_driven_tests
class Tests_trdemo_flights(unittest.TestCase):

    @json_dataset('data/dataset_5.json')
    @clear_session({'spanId': 5})
    def test_5_get_flight_product_id_param(self, data_row):
        param, product_id = data_row

        # GET http://trdemo-flights/flight/{product_id}/{param} (endp 5)
        trdemo_flights = get_http_target('TARGET_TRDEMO_FLIGHTS', authenticate)
        resp = trdemo_flights.get(f'/flight/{product_id}/{param}')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_6.json')
    @clear_session({'spanId': 6})
    def test_6_get_flight_product_id(self, data_row):
        product_id, = data_row

        # GET http://trdemo-flights/flight/{product_id} (endp 6)
        trdemo_flights = get_http_target('TARGET_TRDEMO_FLIGHTS', authenticate)
        resp = trdemo_flights.get(f'/flight/{product_id}')
        resp.assert_ok()
        # resp.assert_status_code(200)


@data_driven_tests
class Tests_trdemo_shoppingcart(unittest.TestCase):

    @json_dataset('data/dataset_8.json')
    @clear_session({'spanId': 8})
    def test_8_get_cart_param(self, data_row):
        param, = data_row

        # GET http://trdemo-shoppingcart/cart/{param} (endp 8)
        trdemo_shoppingcart = get_http_target('TARGET_TRDEMO_SHOPPINGCART', authenticate)
        resp = trdemo_shoppingcart.get(f'/cart/{param}')
        resp.assert_ok()
        # resp.assert_status_code(200)


@data_driven_tests
class Tests_trdemo_users(unittest.TestCase):

    @json_dataset('data/dataset_7.json')
    @clear_session({'spanId': 7})
    def test_7_get_user_param(self, data_row):
        param, = data_row

        # GET http://trdemo-users/user/{param} (endp 7)
        trdemo_users = get_http_target('TARGET_TRDEMO_USERS', authenticate)
        resp = trdemo_users.get(f'/user/{param}')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.airport', expected_value='TLV')
