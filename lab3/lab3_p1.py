# smile: 426 - =-{P
# some other smiles: :-( :-) :-O X<| X-{P =-O ;<{/ 8<{)
import re

test_exps = ['', '=-{P=-{P8<{):-O=-{PX<|=-{P', ':-(:-(:-)X-{P=-O', '8<{)=-{PX<|X<|=-O', 'X<|X-{P=-O;<{/8<{)=-{P:-(:-):-OX<|']

for i in test_exps:
    print(len(re.findall('=-{P', i)))