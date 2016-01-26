# -*- coding: utf-8 -*-

from openerp import api, fields, models

class GsosSupplierProfile(models.Model):
    _name = 'gsos.supplier.profile'
    _description = 'Supplier Profile'
    _inherit = ['mail.thread']

    _rec_name = 'facility_name'

    user_id = fields.Many2one(comodel_name='res.users', string='User')
    facility_name = fields.Char(string='Name')
    facility_street = fields.Char(string='Street')
    facility_street2 = fields.Char(string='Street2')
    facility_city = fields.Char(string='City')
    facility_state_id = fields.Many2one(comodel_name='res.country.state', string='State')
    facility_country_id = fields.Many2one(comodel_name='res.country', string="Country")
    facility_zipcode = fields.Char(string='ZIP')
    facility_phone = fields.Char(string='Phone')
    facility_fax = fields.Char(string='Fax')
    facility_email = fields.Char(string='Email')
    facility_contact_ids = fields.One2many(comodel_name='gsos.supplier.profile.contact',
        inverse_name='supplier_profile_id', string='Facility Contacts',
        domain=[('tag', '=', 'facility_contact')])
    corporate_office_contact_ids = fields.One2many(comodel_name='gsos.supplier.profile.contact',
        inverse_name='supplier_profile_id', string='Corporate Office Contacts',
        domain=[('tag', '=', 'corporate_contact')])
    products_currently_manufactured_ids = fields.One2many(comodel_name='gsos.supplier.profile.product',
        inverse_name='supplier_profile_id', string='Products Currently Manufactured',
        domain=[('tag', '=', 'currently_manufactured')])
    products_potencially_manufactured_ids = fields.One2many(comodel_name='gsos.supplier.profile.product',
        inverse_name='supplier_profile_id', string='Products Potencially Manufactured',
        domain=[('tag', '=', 'potencially_manufactured')])
    raw_material_ids = fields.One2many(comodel_name='gsos.supplier.profile.raw.material',
        inverse_name='supplier_profile_id', string='Raw Materials')
    customer_contact_ids = fields.One2many(comodel_name='gsos.supplier.profile.contact',
        inverse_name='supplier_profile_id', string='Primary Customer Contacts',
        domain=[('tag', '=', 'customer_contact')])

    fda_registration_number = fields.Char(string='FDA Registration Number',
        help='FDA registration number (bioterrorism)')
    third_party_audits = fields.Char(string='Third Party Audits',
        help='List all third party audits performed at this facility (e.g., AIB, GMA-SAFE, Silliker, etc.)')
    certifications = fields.Char(string='Certifications',
        help='List all certifications for the facility (e.g., ISO, HACCP, Kosher, Halal, Organic, etc.)')
    allergens = fields.Char(string='Allergens',
        help='List any Big 8 allergens, sulfites, or FD&C Yellow No. 5 that could be present at this facility')
    lot_numbers_assigned_description = fields.Text(string='Description of Lot Numbers',
        help='Describe how lot numbers are assigned to finished product')
    source_process_water = fields.Text(string='Description of Process Water',
        help='Describe the source of process water (eall, munipality, condensate), as well as effluent treatment and destination')

    audit_count = fields.Integer(compute='_get_audit_count', string='Number audits attached')
    complaint_count = fields.Integer(compute='_get_complaint_count', string='Number complaints attached')
    document_count = fields.Integer(compute='_get_document_count', string='Number documents attached')

    invitation_email = fields.Char(string='Email')
    invitation_notes = fields.Text(string='Notes')

    state = fields.Selection(
        selection=[
          ('draft', 'Draft'),
          ('sent', 'Sent'),
          ('cancelled', 'Cancelled'),
          ('active', 'Active')
        ],
        string='State',
        default='draft')

    # Compute and search fields
    def _get_audit_count(self):
        self.ensure_one()
        audits = self.env['gsos.audit'].search([['supplier_id', '=', self.id]])
        self.audit_count = len(audits)

    def _get_complaint_count(self):
        self.ensure_one()
        complaints = self.env['gsos.complaint'].search([['supplier_id', '=', self.id]])
        self.complaint_count = len(complaints)

    def _get_document_count(self):
        self.ensure_one()

    # Actions
    @api.multi
    def action_invitation_send(self):
        return True

class GsosSupplierProfileContact(models.Model):
    _name = 'gsos.supplier.profile.contact'
    _description = 'Supplier Profile Contact'

    supplier_profile_id = fields.Many2one(comodel_name='gsos.supplier.profile', string='Supplier Profile')
    tag = fields.Char(string="Tag")
    name = fields.Char(string='Name')
    job_position = fields.Char(string='Title/Job Position')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')

class GsosSupplierProfileProduct(models.Model):
    _name = 'gsos.supplier.profile.product'
    _description = 'Supplier Profile Product'

    _rec_name = 'type_material'

    supplier_profile_id = fields.Many2one(comodel_name='gsos.supplier.profile', string='Supplier Profile')
    tag = fields.Char(string="Tag")
    type_material = fields.Char(string='Type of Material')
    description = fields.Char(string='Description of Ingredient/Package')
    container_type = fields.Char(string='Container Type')
    ship_to_location = fields.Char(string='Ship-To Location(s)')

class GsosSupplierProfileRawMaterial(models.Model):
    _name = 'gsos.supplier.profile.raw.material'
    _description = 'Supplier Profile Raw Material'

    _rec_name = 'material_description'

    supplier_profile_id = fields.Many2one(comodel_name='gsos.supplier.profile', string='Supplier Profile')
    material_description = fields.Char(string='Material Description')
    supplier_company = fields.Char(string='Supplier Company')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    phone = fields.Char(string='Phone')
