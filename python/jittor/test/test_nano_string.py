# ***************************************************************
# Copyright (c) 2020 Jittor. Authors: Dun Liang <randonlang@gmail.com>. All Rights Reserved.
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
# ***************************************************************
import unittest
import jittor as jt
import time
from .test_core import expect_error
import os

mid = 0
if os.uname()[1] == "jittor-ce":
    mid = 1

class TestNanoString(unittest.TestCase):
    def test(self):
        dtype = jt.NanoString
        t = time.time()
        n = 1000000
        for i in range(n):
            dtype("float")
        t = (time.time() - t)/n
        # t is about 0.01 for 100w loop
        # 92ns one loop
        assert t < [1.5e-7, 1.7e-7][mid], t

        assert (jt.hash("asdasd") == 4152566416)
        assert str(jt.NanoString("float"))=="float"
        # pybind11: 7
        # Tuple call: 1.3
        # fast call (with or with not): 0.9
        # init call 1.5
        # int init: 1.2
        # dtype init(cache): 0.75
        # final: 1.0

if __name__ == "__main__":
    unittest.main()