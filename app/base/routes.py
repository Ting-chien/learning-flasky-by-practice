from app.base import blueprint


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return "This is login page."