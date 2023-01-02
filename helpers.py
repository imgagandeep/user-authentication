from datetime import datetime

date_format = "%Y-%m-%d"


def params_validator(params, required_params):
    if not isinstance(params, dict):
        params = params.dict()
    # checks parameters exist in params
    for parameter in required_params:
        field = params.get(parameter)
        # checks field is non empty
        if not field:
            return False
    return True


def date_converter(date_param):
    # checks date_param is non empty
    if date_param:
        date_param = datetime.strptime(date_param, date_format).date()
    else:
        date_param = None

    return date_param
