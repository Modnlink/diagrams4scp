# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _Scp


class _Appservice(_Scp):
    _type = "appservice"
    _icon_dir = "resources/scp/appservice"


class Apigateway(_Appservice):
    _icon = "APIGateway.png"


class Mail(_Appservice):
    _icon = "Mail.png"


class Push(_Appservice):
    _icon = "Push.png"


class Sms(_Appservice):
    _icon = "SMS.png"


# Aliases
