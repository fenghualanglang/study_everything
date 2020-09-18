# -*- coding: utf-8 -*-
from handler import BaseHandler


class ErrorHandler(BaseHandler):

    def get(self):
        self.set_status(404)
        self.out(404)

    def post(self):
        self.set_status(404)
        self.out(404)

    def put(self):
        self.set_status(404)
        self.out(404)