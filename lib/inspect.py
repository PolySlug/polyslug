import pkgutil

'''
recupererSousModules

@return {Liste}     Liste des noms des modules de `package`

@see http://stackoverflow.com/questions/1707709/list-all-the-modules-that-are-part-of-a-python-package
'''
def recupererSousModules(package) :
    result = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        result.append(modname)

    return result
