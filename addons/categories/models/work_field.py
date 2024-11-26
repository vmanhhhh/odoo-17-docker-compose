from odoo import models, fields


class WorkField(models.Model):
    _name = "dh.categories.work_field"
    _description = "Thông tin mảng công tác"

    name = fields.Char(string="Tên mảng công tác", required=True)
