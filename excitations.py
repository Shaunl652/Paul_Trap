#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Want to see how the potential moves with the changing pot difference
# =============================================================================

import numpy as np


EC_Bot = -100
EC_Top = np.linspace(-100,-300,100)

with open('endcaps.Excitation','w') as file:
    for i,V in enumerate(EC_Top):
        file.write(f'EXCITATION ECV_{i}\n')
        file.write(f'   End_Cap_Bot {EC_Bot}\n')
        file.write(f'   Wehnelt     {V}\n')
        file.write('ENDEXCITATION\n')
        file.write('\n')
        file.write('\n')
        
        