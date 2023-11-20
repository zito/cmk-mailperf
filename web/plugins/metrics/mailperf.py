#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _l
from cmk.gui.plugins.metrics.utils import graph_info, metric_info, unit_info


unit_info["1/min"] = {
    "title": _("per minute"),
    "description": _("Frequency (displayed in events/min)"),
    "symbol": _("/min"),
    "render": lambda v: "{}{}".format(cmk.utils.render.scientific(v, 1), _("/min")),
    "js_render": "v => cmk.number_format.scientific(v, 1) + '/min'",
}

# Colors: See indexed_color() in cmk/gui/plugins/metrics/utils.py

metric_info["bounced"] = {
    "title": _l("Bounced messages"),
    "unit": "1/min",
    "color": "22/a",
}

metric_info["deferred"] = {
    "title": _l("Deferred messages"),
    "unit": "1/min",
    "color": "23/a",
}

metric_info["forwarded"] = {
    "title": _l("Forwarded messages"),
    "unit": "1/min",
    "color": "24/a",
}

metric_info["greylisted"] = {
    "title": _l("Greylisted messages"),
    "unit": "1/min",
    "color": "51/a",
}

metric_info["received"] = {
    "title": _l("Received messages"),
    "unit": "1/min",
    "color": "31/a",
}

metric_info["rejected"] = {
    "title": _l("Rejected messages"),
    "unit": "1/min",
    "color": "13/a",
}

metric_info["sent"] = {
    "title": _l("Sent messages"),
    "unit": "1/min",
    "color": "41/a",
}

metric_info["spam"] = {
    "title": _l("Spam messages"),
    "unit": "1/min",
    "color": "15/a",
}

metric_info["virus"] = {
    "title": _l("Virus messages"),
    "unit": "1/min",
    "color": "16/a",
}


graph_info["traffic_normal"] = {
    "title": _l("Mail system sent/received messages"),
    "metrics": [
        ("sent", "area"),
        ("received", "line"),
    ]
}

graph_info["traffic_disrupted"] = {
    "title": _l("Mail system disrupted messages"),
    "metrics": [
        ("bounced", "line"),
        ("deferred", "line"),
        ("forwarded", "line"),
        ("greylisted", "line"),
        ("rejected", "line"),
        ("spam", "line"),
        ("virus", "line")
    ],
    "optional_metrics": [
        "bounced",
        "deferred",
        "forwarded",
        "greylisted",
        "rejected",
        "spam",
        "virus",
    ],
    "omit_zero_metrics": True,
}
