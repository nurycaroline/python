# packing e unpacking

from datetime import date
d = (2013, 3, 15)
print date(d[0], d[1], d[2])
print date(*d)

# ---------------------------------------------------
# Packing
def new_user (active=False, admin=True):
	print active
	print admin

config = {"active": True, "admin": False}

new_user(**config)


# ---------------------------------------------------
# Unpacking

def unpacking_experiment_args(*args):
	arg1 = args[0]
	arg2 = args[1]
	others = args[2:]
	print arg1
	print arg2
	print others
	
unpacking_experiment_args(1,2,3,4,5,6)


def unpacking_experiment_kwargs(**kwargs):
	print kwargs

unpacking_experiment_kwargs(name="teste", other="outros")