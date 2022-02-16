from Tests.testLogic import testAdaugaRezervare, testStergeRezervare, testclasasuperioara, testIeftinereProcent, \
    testgetById, testModificare, testPretMaxim, testOrdo, testUndoRedo
from Tests.testDomain import testDomain


def alltests():
    testDomain()
    testAdaugaRezervare()
    testStergeRezervare()
    testclasasuperioara()
    testIeftinereProcent()
    testgetById()
    testModificare()
    testPretMaxim()
    testOrdo()
    testUndoRedo()