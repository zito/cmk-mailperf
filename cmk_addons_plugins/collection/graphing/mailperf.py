#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.graphing.v1 import graphs, perfometers, Title
from cmk.graphing.v1.metrics import (
    Color,
    CriticalOf,
    DecimalNotation,
    Metric,
    Unit,
    WarningOf,
)


UNIT_PER_MINUTE = Unit(DecimalNotation("/min"))


metric_mailperf_bounced = Metric(
    name="mailperf_bounced",
    title=Title("Bounced messages"),
    unit=UNIT_PER_MINUTE,
    color=Color.ORANGE,
)

metric_mailperf_deferred = Metric(
    name="mailperf_deferred",
    title=Title("Deferred messages"),
    unit=UNIT_PER_MINUTE,
    color=Color.YELLOW,
)

metric_mailpef_forwarded = Metric(
    name="mailpef_forwarded",
    title=Title("Forwarded messages"),
    unit=UNIT_PER_MINUTE,
    color=Color.LIGHT_YELLOW,
)

metric_mailpef_greylisted = Metric(
    name="mailpef_greylisted",
    title=Title("Greylisted messages"),
    unit=UNIT_PER_MINUTE,
    color=Color.GRAY,
)

metric_mailpef_received = Metric(
    name="mailpef_received",
    title=Title("Received messages"),
    unit=UNIT_PER_MINUTE,
    color=Color.GREEN,
)

metric_mailpef_rejected = Metric(
    name="mailpef_rejected",
    title=Title("Rejected messages"),
    unit=UNIT_PER_MINUTE,
    color=Color.RED,
)

metric_mailpef_sent = Metric(
    name="mailpef_sent",
    title=Title("Sent messages"),
    unit=UNIT_PER_MINUTE,
    color=Color.BLUE,
)

metric_mailpef_spam = Metric(
    name="mailpef_spam",
    title=Title("Spam messages"),
    unit=UNIT_PER_MINUTE,
    color=Color.LIGHT_RED,
)

metric_mailpef_virus = Metric(
    name="mailpef_virus",
    title=Title("Virus messages"),
    unit=UNIT_PER_MINUTE,
    color=Color.DARK_RED,
)


graph_traffic_normal = graphs.Graph(
    name="traffic_normal",
    title=Title("Messages sent/received"),
    compound_lines=["sent"],
    simple_lines=[
        "received",
        WarningOf("sent"),
        CriticalOf("sent"),
        WarningOf("received"),
        CriticalOf("received"),
    ],
)


graph_traffic_disrupted = graphs.Graph(
    name="traffic_disrupted",
    title=Title("Messages disrupted"),
    simple_lines=[
        "bounced",
        "deferred",
        "forwarded",
        "greylisted",
        "rejected",
        "spam",
        "virus",
        WarningOf("bounced"),
        CriticalOf("bounced"),
        WarningOf("deferred"),
        CriticalOf("deferred"),
        WarningOf("forwarded"),
        CriticalOf("forwarded"),
        WarningOf("greylisted"),
        CriticalOf("greylisted"),
        WarningOf("rejected"),
        CriticalOf("rejected"),
        WarningOf("spam"),
        CriticalOf("spam"),
        WarningOf("virus"),
        CriticalOf("virus"),
    ],
    optional=[
        "bounced",
        "deferred",
        "forwarded",
        "greylisted",
        "rejected",
        "spam",
        "virus",
    ],
)


perfometer_sent_received = perfometers.Bidirectional(
    name="sent_received",
    left=perfometers.Perfometer(
        name="received",
        focus_range=perfometers.FocusRange(
            perfometers.Closed(0),
            perfometers.Open(100)
        ),
        segments=["received"],
    ),
    right=perfometers.Perfometer(
        name="sent",
        focus_range=perfometers.FocusRange(
            perfometers.Closed(0),
            perfometers.Open(100)
        ),
        segments=["sent"],
    ),
)
