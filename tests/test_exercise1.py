import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even_at_1():
    assert is_even(1) == False

def test_r1_rectangle_area_2_3():
    assert rectangle_area(2, 3) == 6

def test_r1_double_2():
    assert double(2) == 4


# bug report 2
def test_r2_rectangle_area_2_3():
    assert rectangle_area(2, 3) == 6


# bug report 3
def test_r3_double_5():
    assert double(5) == 10
