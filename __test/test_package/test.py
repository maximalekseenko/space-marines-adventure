import os


PACKAGE_FOLDER = os.path.dirname(__file__)


DATA1 = list()
DATA2 = list()
DATA3 = list()


# import
for package in os.listdir("."):

    # validate path
    if package.startswith('_'): continue
    if not os.path.isdir(os.path.join(PACKAGE_FOLDER, package)): continue

    # import
    try: package_module = __import__(package)
    except: continue

    # pull datas
    DATA1 += package_module.DATA1
    DATA2 += package_module.DATA2
    DATA3 += package_module.DATA3


# result
print(DATA1)
print(DATA2)
print(DATA3)