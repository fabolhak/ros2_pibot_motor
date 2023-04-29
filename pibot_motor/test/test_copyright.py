# Copyright 2015 Open Source Robotics Foundation, Inc.
# SPDX-FileCopyrightText: 2015 Open Source Robotics Foundation, Inc.
#
# SPDX-License-Identifier: Apache-2.0

from ament_copyright.main import main
import pytest


@pytest.mark.copyright
@pytest.mark.linter
def test_copyright():
    rc = main(argv=['.'])
    assert rc == 0, 'Found errors'
