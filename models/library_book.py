from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char(string='Book Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN')
    publisher = fields.Char(string='Publisher')
    published_date = fields.Date(string='Published Date')
    price = fields.Float(string='Price', digits=(6, 2))
    quantity = fields.Integer(string="Quantity", default=1)

    con_category = fields.Many2many('library.category', string='Categories')
