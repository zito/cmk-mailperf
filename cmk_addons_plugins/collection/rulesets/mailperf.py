#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.rulesets.v1 import (
    rule_specs,
    Title,
)
from cmk.rulesets.v1.form_specs import (
    DefaultValue,
    DictElement,
    Dictionary,
    Integer,
    LevelDirection,
    SimpleLevels,
    SimpleLevelsConfigModel,
)


def _parameter_valuespec() -> Dictionary:
    return Dictionary(
        elements={
            f"levels_{metric}": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels[int](
                    title=Title(f"Levels {metric}"),
                    form_spec_template=Integer(unit_symbol="/min"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=DefaultValue(value=(1000, 2000)),
                )
            )
            for metric in ("bounced", "deferred", "forwarded", "greylisted", "received", "rejected", "sent", "spam", "virus")
        },
    )


rule_spec_check_parameters = rule_specs.CheckParameters(
    name="mailperf",
    title=Title("Mail performance"),
    topic=rule_specs.Topic.APPLICATIONS,
    parameter_form=_parameter_valuespec,
    condition=rule_specs.HostCondition(),
)
