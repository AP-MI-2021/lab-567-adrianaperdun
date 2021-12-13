from Test.domainTest import testRezervare
from Test.logicTest import testAdaugareRezervare, testStergereRezervare, testModificaRezervare, \
    testTrecereaClasaSuperioaraDupaNume, testIeftinirePretRezervariDupaCheckin, \
    testOrdoneazaRezervarileDescrescDupaPret, testSumaPreturiPerNume
from Test.testUndoRedo import testUndoRedo, testUndoRedoTrecereClasaSuperioara, testUndoRedoIeftinire


def runAllTests():
    testRezervare()
    testAdaugareRezervare()
    testStergereRezervare()
    testModificaRezervare()
    testTrecereaClasaSuperioaraDupaNume()
    testIeftinirePretRezervariDupaCheckin()
    testOrdoneazaRezervarileDescrescDupaPret()
    testSumaPreturiPerNume()
    testUndoRedo()
    testUndoRedoTrecereClasaSuperioara()
    testUndoRedoIeftinire()