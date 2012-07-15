#!/usr/bin/env python
#coding:UTF-8

suitable = [];
nums = "123456789"

# x / y
for x in nums:
    for y in nums:
        for z in nums:
            # xz / zy
            numerator   = int(x + z)
            denominator = int(z + y)
            if numerator < denominator:
                if int(x)*denominator == int(y)*numerator:
                    suitable.append( (numerator, denominator) )

            # zx / yz patterns is covered by the former patterns

print suitable;

