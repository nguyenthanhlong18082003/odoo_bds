

from odoo import models, fields, api


class Product(models.Model):

    _inherit = "product.template" #khi kết thừa dùng _inherit thay cho _name



    square = fields.Char(string="Diện tích")
    image = fields.Binary(string='Logo', attachmaent = True)
    address = fields.Char(string='Địa chỉ')

    
 