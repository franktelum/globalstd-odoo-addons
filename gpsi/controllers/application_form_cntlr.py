# -*- coding: utf-8 -*-

from openerp import http

class ApplicationFormCntlr(http.Controller):
    @http.route("/gstd/store/products", auth="public", methods=['GET'])
    def index(self, **kw):
        return "Hello World"
