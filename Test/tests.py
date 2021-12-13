from Test.domainTest import testDomain
from Test.logicTest import testgetById, testOrdo, testmax, testmodify, testreduce, testupgrade, testdelete, testadd
from Test.testUndoRedo import testUndoRedoTrecereClasaSuperioara, testUndoRedo, testUndoRedoIeftinire


def alltest():
    testDomain()
    testadd()
    testdelete()
    testupgrade()
    testreduce()
    testgetById()
    testmodify()
    testmax()
    testOrdo()
    testUndoRedo()
    testUndoRedoTrecereClasaSuperioara()
    testUndoRedoIeftinire()