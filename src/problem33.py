#!/usr/bin/env python
#coding:UTF-8

suitable = [];
nums = "123456789"

# x / y
for x in nums:
    for y in nums:
        for z in nums:
            # xz / zy
            xz = int(x + z)
            zy = int(z + y)
            if xz < zy:
                if int(x)*zy == int(y)*xz:
                    suitable.append( (xz, zy) )

            # zx / zy patterns is covered by the former patterns

print suitable;

