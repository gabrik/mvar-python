# Copyright (c) 2018 Gabriele Baldoni.
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: Apache-2.0
#
# Contributors: Gabriele Baldoni MVar implementation in Python

import unittest
from mvar import MVar
from threading import Thread
from random import randint
import time


class MVarTests(unittest.TestCase):

    def test_get_put(self):

        def worker(var):
            time.sleep(randint(1, 3))
            var.put(1)

        def worker2(var):
            var.put(3)

        local_var = MVar()
        Thread(target=worker, args=(local_var,), daemon=True).start()
        res = local_var.take()

        local_var.put(2)
        Thread(target=worker2, args=(local_var,), daemon=True).start()
        res2 = local_var.take()
        res3 = local_var.take()

        self.assertEqual(res, 1)
        self.assertEqual(res2, 2)
        self.assertEqual(res3, 3)
