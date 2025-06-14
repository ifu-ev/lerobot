#!/usr/bin/env python

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass, field

from ..config import TeleoperatorConfig


@TeleoperatorConfig.register_subclass("panda_leader")
@dataclass
class PandaTeleoperatorConfig(TeleoperatorConfig):
    ip: str  # Port to connect to the arm

    # not sure if its needed here, but manual says TeleoperatorConfig
    # Default bounds for the end-effector position (in meters)
    # end_effector_bounds: dict[str, list[float]] = field(
    #     default_factory=lambda: {
    #         "min": [0.37, -0.19, 0.27],  # min x, y, z
    #         "max": [0.71, 0.20, 0.61],  # max x, y, z
    #     }
    # )
    
