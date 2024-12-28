from odoo import models, fields

class LibraryMember(models.Model):
    _name = 'library.member'

    name = fields.Char(String='Full Name', required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string='Phone')
    membership_date = fields.Date(string='Membership Date')
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status')
    con_books = fields.Many2many('library.book', string='Borrowed Books')
