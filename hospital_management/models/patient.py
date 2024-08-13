from odoo import fields, models, api

class Patient(models.Model):
    _name = 'wb.patient'
    _description = 'This is a patient model'

    name = fields.Char(string="Name")
    last_name = fields.Char(string="Last Name")
    date_of_birth = fields.Date(string="Date of Birth")
    phone = fields.Char(string="Phone")
    blood_group = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('0+', '0+'),
        ('0-', '0-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-')
    ], string="Blood Group")
    gender = fields.Selection([
        ('female', 'Female'),
        ('male', 'Male')
    ], string="Gender")
    marital_status = fields.Selection([
        ('married', 'Married'),
        ('unmarried', 'Unmarried'),
        ('widow', 'Widow'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string="Marital Status")

    # Socioeconomic
    socioeconomic = fields.Selection([
        ('low', 'Lower Class'),
        ('med', 'Medium Class'),
        ('high', 'High Class')
    ], string='Socioeconomic')
    education = fields.Selection([
        ('post', 'Post Graduation'),
        ('grad', 'Graduation'),
        ('pre', 'Pre Graduation')
    ], string='Education Level')
    house = fields.Selection([
        ('good', 'Good'),
        ('bad', 'Bad'),
        ('poor', 'Poor')
    ], string='House Condition')
    occupation = fields.Char(string='Occupation')
    work_home = fields.Boolean(string='Work At Home')
    hours_out = fields.Integer(string='Hours Stay Outside Home')

    # LifeStyle
    exercises = fields.Boolean(string='Exercise')
    day_sleep = fields.Boolean(string="Sleep At Daytime")
    sleep_hours = fields.Integer(string="Sleep Hours")
    meals_per_day = fields.Integer(string="Meals/Day")
    diet = fields.Boolean(string="Currently on diet")
    coffee = fields.Boolean(string="Coffee")
    soft_drinks = fields.Boolean(string="Soft Drinks")

    # Addictions
    alcoholic = fields.Boolean(string='Alcoholic')
    ex_alcoholic = fields.Boolean(string='Ex-Alcoholic')
    smoker = fields.Boolean(string='Smoker')
    ex_smoker = fields.Boolean(string='Ex-Smoker')
    passive_smoker = fields.Boolean(string='Passive Smoker')
    drug_user = fields.Boolean(string='Drug User')
    ex_drug = fields.Boolean(string='Ex Drug User')
    iv_drug = fields.Boolean(string='IV Drug User')

    # Sexuality
    orientation = fields.Selection([
        ('straight', 'Straight'),
        ('homosexual', 'Homosexual'),
        ('lesbian', 'Lesbian')
    ], string='Orientation')
    age_encounter = fields.Integer(string='Age of First Encounter')
    no_partners = fields.Integer(string='No of partners')
    contraceptive_methods = fields.Selection([
        ('pills', 'Contraceptive Pills'),
        ('ring', 'Contraceptive Ring'),
        ('injection', 'Contraceptive Injection')
    ], string='Contraceptive Methods')
    oral_sex = fields.Boolean(string='Oral Sex')
    anal_sex = fields.Boolean(string='Anal Sex')
    prostitute = fields.Boolean(string='Prostitute')
    sex_with_prostitute = fields.Boolean(string='Sex with Prostitute')

    # Family
    ethnic_group = fields.Selection([
        ('hindu', 'Hindu'),
        ('muslim', 'Muslim'),
        ('christian', 'Christian')
    ], string='Ethnic Group')
    genetic_risks = fields.Text(string='Genetic Risks')

    #Analysis
    file = fields.Binary(string='Analysis File')
    file_name = fields.Char(string='Binary File Name')
    #file = fields.Many2one('wb.answer', string='Analysis')

    # One2many relationship
    family_ids = fields.One2many('wb.family', 'family_id', string='Family Members')

    doctor_id = fields.Many2one('wb.doctor', string='Doctor', help='This is the doctor responsible for this patient')
    partner_id = fields.Many2one('res.partner', string='Related Contact', ondelete='cascade', required=True, delegate=True)

    @api.model
    def create(self, vals):
        # Ensure name and last_name are strings
        name = vals.get('name', '') or ''
        last_name = vals.get('last_name', '') or ''

        partner_vals = {
            'name': name + ' ' + last_name,
            'phone': vals.get('phone'),
            'is_company': False,
            'type': 'contact',
        }
        partner = self.env['res.partner'].create(partner_vals)
        vals['partner_id'] = partner.id
        return super(Patient, self).create(vals)


