from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBorrow(models.Model):
    _name = 'library.borrow'

    member_id = fields.Many2one('library.member', string='Member', required=True)
    book_id = fields.Many2one('library.book', string='Book', required=True)
    quantity_borrowed = fields.Integer(string='Quantity Borrowed', default=1)
    borrow_date = fields.Date(string='Borrow Date', default=fields.Date.today())

    @api.constrains('quantity_borrowed', 'book_id')
    def _check_book_quantity(self):
        for record in self:
            if record.book_id and record.quantity_borrowed > record.book_id.quantity:
                raise ValidationError("Not enough copies available to borrow.")

    def borrow_book(self):
        for record in self:
            book = record.book_id
            book.quantity -= record.quantity_borrowed
            record.member_id.write({
                'con_books': [(4, record.book_id.id)]
            })

    def return_book(self):
        for record in self:
            book = record.book_id
            book.quantity += record.quantity_borrowed
            record.member_id.write({
                'con_books': [(3, record.book_id.id)]
            })
            record.unlink()