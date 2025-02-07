# Copyright (C) 2020-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""PyTorch optimizers package."""
import pkgutil

if pkgutil.find_loader('torch'):
    from .fedprox import FedProxOptimizer # NOQA
    from .fedprox import FedProxAdam # NOQA
