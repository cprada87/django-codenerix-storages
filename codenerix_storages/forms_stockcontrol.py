# -*- coding: utf-8 -*-
#
# django-codenerix-storages
#
# Copyright 2017 Centrologic Computational Logistic Center S.L.
#
# Project URL : http://www.codenerix.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# from django.utils.translation import ugettext_lazy as _

from codenerix.forms import GenModelForm
from codenerix_storages.models_stockcontrol import Inventory, InventoryLine, InventoryIn, InventoryInLine, InventoryOut, InventoryOutLine, Distribution, DistributionLine


class InventoryForm(GenModelForm):

    class Meta:
        model = Inventory
        exclude = ['end']

    def __groups__(self):
        g = []
        # (
        #     _('Details'), 12,
        #     ['name', 6],
        # ),
        return g

    @staticmethod
    def __groups_details__():
        g = []
        # (
        #    _('Details'), 12,
        #    ['name', 6],
        # ),
        return g


class InventoryLineForm(GenModelForm):

    class Meta:
        model = InventoryLine
        exclude = ['inventory', 'operator']

    def __groups__(self):
        g = []
        return g

    @staticmethod
    def __groups_details__():
        g = []
        return g


class DistributionForm(GenModelForm):

    class Meta:
        model = Distribution
        exclude = ['end']

    def __groups__(self):
        g = []
        # (
        #     _('Details'), 12,
        #     ['name', 6],
        # ),
        return g

    @staticmethod
    def __groups_details__():
        g = []
        # (
        #    _('Details'), 12,
        #    ['name', 6],
        # ),
        return g


class DistributionLineForm(GenModelForm):

    class Meta:
        model = DistributionLine
        exclude = ['distribution']

    def __groups__(self):
        g = []
        return g

    @staticmethod
    def __groups_details__():
        g = []
        return g


class InventoryInForm(GenModelForm):

    class Meta:
        model = InventoryIn
        exclude = ['end']

    def __groups__(self):
        g = []
        # (
        #     _('Details'), 12,
        #     ['name', 6],
        # ),
        return g

    @staticmethod
    def __groups_details__():
        g = []
        # (
        #    _('Details'), 12,
        #    ['name', 6],
        # ),
        return g


class InventoryInLineForm(GenModelForm):

    class Meta:
        model = InventoryInLine
        exclude = ['inventory', 'operator']

    def __groups__(self):
        g = []
        return g

    @staticmethod
    def __groups_details__():
        g = []
        return g


class InventoryOutForm(GenModelForm):

    class Meta:
        model = InventoryOut
        exclude = ['end']

    def __groups__(self):
        g = []
        # (
        #     _('Details'), 12,
        #     ['name', 6],
        # ),
        return g

    @staticmethod
    def __groups_details__():
        g = []
        # (
        #    _('Details'), 12,
        #    ['name', 6],
        # ),
        return g


class InventoryOutLineForm(GenModelForm):

    class Meta:
        model = InventoryOutLine
        exclude = ['inventory', 'operator']

    def __groups__(self):
        g = []
        return g

    @staticmethod
    def __groups_details__():
        g = []
        return g
