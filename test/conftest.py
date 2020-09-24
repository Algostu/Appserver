import sys
import pytest

sys.path.insert(0, '/var/www/Appserver/')
from main import create_app


@pytest.fixture(scope="module")
def setup():
    app = create_app('test')
    app.config['test'] = True
    return app.test_client()
