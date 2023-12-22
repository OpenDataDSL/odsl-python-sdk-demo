from odsl import sdk

odsl = sdk.ODSL()
odsl.setStage('dev')
odsl.login()

# Test GET
obj = odsl.get('object', 'public', '#ECB')
print(obj['description'])
ts = odsl.get('data', 'public', '#ABN_FX.EURUSD:SPOT')
print(ts)

# Test LIST
objects = odsl.list('object', source='public', filter='source=ECB')
print(objects[0])

# Test UPDATE
var = {
    '_id': 'AAA.PYTHON',
    'name': 'Python Example'
}
odsl.update('object', 'private', var)

# Test READ and UPDATE
po = odsl.get('object', 'private', 'AAA.PYTHON')
po['description'] = 'Updated from Python'
odsl.update('object', 'private', po)