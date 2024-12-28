from odoo import models, fields

class LibraryCategory(models.Model):
    _name = 'library.category'

    name = fields.Char(string='Category Name', required=True)
    con_book = fields.Many2many('library.book', string='Books')
