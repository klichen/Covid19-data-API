import app, os

flask_app = app.app
#testing_client = flask_app.test_client()

def test_post_new_time_series():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(dir_path, "sample_time_series.csv")

    with flask_app.test_client() as test_client:
        data = {
            'fileupload': (open(data_path, 'rb'), data_path)
        }
        test_client.post('/clear_data')
        response = test_client.post('/time_series/confirmed', data=data, content_type='multipart/form-data')
        assert response.status_code == 201