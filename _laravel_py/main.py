from write_migration import writeMigration
from write_model import writeModel
from write_dashboard import writeDashboard
from write_dashboard_view import writeDashboardView
from write_create import writeCreate
nameModel = 'Beneficiary'
namePlural = 'beneficiaries'
nameView = 'beneficiary'
nombre = 'Beneficiario'

# calling functions

writeMigration('beneficiaries')
writeModel('Beneficiary')
writeDashboard('Beneficiary', 'beneficiary')
writeDashboardView('beneficiary', 'beneficiario')
writeCreate(nameModel, nameView)
