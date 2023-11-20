#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _
from cmk.gui.plugins.wato.utils import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)
from cmk.gui.valuespec import (
    Alternative,
    Dictionary,
    FixedValue,
    Integer,
    ListOf,
    TextInput,
    Tuple,
)


def _parameter_valuespec() -> Dictionary:
    return Dictionary(
        title=_("Set Levels"),
        elements=[
            (
                "levels_" + metric,
                Tuple(
                    title=_("Levels " + metric),
                    elements=[
                        Integer(title=_("Warning at")),
                        Integer(title=_("Critical at")),
                    ],
                ),
            )
            for metric in ("bounced", "deferred", "forwarded", "greylisted", "received", "rejected", "sent", "spam", "virus")
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="mailperf",
        group=RulespecGroupCheckParametersApplications,
        parameter_valuespec=_parameter_valuespec,
        title=lambda: _("Mail performance"),
    )
)
