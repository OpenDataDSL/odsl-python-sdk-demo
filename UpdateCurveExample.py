from odsl import sdk

odsl = sdk.ODSL()
odsl.login()

# Read a curve
base = odsl.get('data', 'public', '#MIBGAS.ES.PVB.FUT.CURVE:LAST:2023-12-20')
print("Got curve: " + base['_id'])

# Create our new curve
curve = {
	'_id': 'CURVE',
	'_type': 'VarCurve',
 	'ondate': {
		'curveDate': '2023-12-20',
		'expiryCalendar': '#REOMB'
	},
  	'contracts': []
}

# Multiply each contract by 1.1 and add to our curve
for c in base['contracts']:
    c['value'] = c['value'] * 1.1
    curve['contracts'].append(c)

# Update the curve
var = {
    '_id': 'AAA.PYTHON',
    'name': 'Python Example',
    'CURVE': curve
}
odsl.update('object', 'private', var)
