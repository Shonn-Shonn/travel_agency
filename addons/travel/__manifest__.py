{
    'name':'Travelling',
    'depends' : ['mail'],
    'data': [

        #data
        "data/sequence.xml",

        #security
        "security/ir.model.access.csv",

        #views
        "views/township.xml",
        "views/transpotation_route.xml",
        "views/travel_gate.xml",
        "views/travel_agency.xml",
        "views/travel_driver_history.xml",
        "views/travel_car.xml",
        "views/menus.xml",
        
        #wizard
        "wizard/changedriverwizard.xml"
    ]
}