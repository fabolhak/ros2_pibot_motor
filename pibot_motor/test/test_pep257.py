# Copyright 2015 Open Source Robotics Foundation, Inc.
# SPDX-FileCopyrightText: 2015 Open Source Robotics Foundation, Inc.
#
# SPDX-License-Identifier: Apache-2.0

from ament_pep257.main import main
import pytest


@pytest.mark.linter
@pytest.mark.pep257
def test_pep257():
    rc = main(argv=['.'])
    assert rc == 0, 'Found code style errors / warnings'
