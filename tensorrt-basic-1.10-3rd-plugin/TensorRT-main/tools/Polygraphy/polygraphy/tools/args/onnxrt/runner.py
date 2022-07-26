#
# Copyright (c) 2021, NVIDIA CORPORATION. All rights reserved.
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
#
from polygraphy import mod
from polygraphy.tools.args.base import BaseArgs
from polygraphy.tools.script import make_invocable


@mod.export()
class OnnxrtRunnerArgs(BaseArgs):
    def register(self, maker):
        from polygraphy.tools.args.onnxrt.loader import OnnxrtSessionArgs

        if isinstance(maker, OnnxrtSessionArgs):
            self.session_args = maker

    def check_registered(self):
        assert self.session_args is not None, "OnnxrtSessionArgs is required!"

    def add_to_script(self, script):
        script.add_import(imports=["OnnxrtRunner"], frm="polygraphy.backend.onnxrt")
        script.add_runner(make_invocable("OnnxrtRunner", self.session_args.add_onnxrt_session(script)))
