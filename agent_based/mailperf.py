#!/usr/bin/env python3
# Copyright (C) 2022 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
from collections import defaultdict
import time
from typing import Any, Iterable, Iterator, Mapping, NamedTuple, Optional, Sequence

from .agent_based_api.v1 import check_levels, get_rate, get_value_store, register, Service
from .agent_based_api.v1.type_defs import CheckResult, DiscoveryResult, StringTable

Section = Mapping[str, Any]


# <<<mailperf>>>
# bounced 0
# deferred 0
# forwarded 0
# greylisted 0
# received 72
# rejected 10
# sent 82
# spam 0
# time_since 2023-11-20T17:23:05.460035+01:00
# virus 0


def parse(string_table: StringTable) -> Optional[Section]:
    if not string_table:
        return None
    section = {}
    for k, v in string_table:
        if k.startswith('time_'):
            section[k] = v
        else:
            section[k] = int(v)
    return section


register.agent_section(name="mailperf", parse_function=parse)


def discovery_stat(section: Section) -> DiscoveryResult:
    if section:
        yield Service()


def check_stat(params: Mapping[str, Any], section: Section) -> CheckResult:
    store = get_value_store()
    if 'time_since' not in store or store['time_since'] != section['time_since']:
        store.clear()
        store['time_since'] = section['time_since']
    for k, v in section.items():
        if k.startswith('time_'):
            continue
        if v is not None:
            rate = get_rate(store, k, time.time(), v) * 60     # msgs / min
            yield from check_levels(
                    rate,
                    levels_upper=params.get("levels_"+k),
                    metric_name=k,
                    render_func=lambda v: f"{v:.1f} msg/min",
                    label=k,
                )


register.check_plugin(
    name="mailperf",
    service_name="Mail rate",
    discovery_function=discovery_stat,
    check_function=check_stat,
    check_default_parameters={},
    check_ruleset_name="mailperf",
)
