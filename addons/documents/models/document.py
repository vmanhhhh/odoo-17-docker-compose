from odoo import fields, models


class Document(models.Model):
    _name = "dh.documents.document"
    _description = "Văn bản"

    name = fields.Char(string="Tên văn bản", required=True)
    number = fields.Char(string="Số văn bản", required=True)
    file = fields.Binary(string="File Upload")
    work_field = fields.Many2one(comodel_name="dh.categories.work_field", string = "Mảng công tác", required=True)
