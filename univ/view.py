import json, time
import pandas as pd

from flask import send_file
from flask import escape, Blueprint, request, session, current_app as app
from sqlalchemy import text

from main.extensions import *
from main.model import *

univ_api = Blueprint('univ', __name__, url_prefix='/univ')

@univ_api.route('/logoImage', methods=['GET'])
@login_required
def get_logImage():
    # this is server-side query.
    # trim 고,등,학,교 off
    univ_id = int(request.args.get('univID'))
    print(univ_id)
    univ = UnivInfo.query.filter_by(univID=univ_id).first()
    if not univ.logoPossible:
        return response_with_code("<fail>:2:no logo are prepared")

    signiture_path = 'crawler/data/signiture/' + univ.univName + ".png" # point to your image location
    signiture_img = get_response_image(signiture_path)
    symbol_path = 'crawler/data/symbol/' + univ.univName + ".png" # point to your image location
    symbol_img = get_response_image(symbol_path)

    return response_with_code("<success>", {'symbol': symbol_img, 'signiture': signiture_img})
