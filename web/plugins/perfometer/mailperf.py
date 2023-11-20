#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.plugins.metrics import perfometer_info


perfometer_info.append(
    {
        "type": "dual",
        "perfometers": [
            {
                "type": "logarithmic",
                "metric": "received",
                "half_value": 100,
                "exponent": 5,
            },
            {
                "type": "logarithmic",
                "metric": "sent",
                "half_value": 100,
                "exponent": 5,
            },
        ],
    }
)
