from julian import isLeapYear

def test_leap_year_divisible_by_4_and_not_100():
    assert isLeapYear(2000) == True

def test_leap_year_divisible_with_by_400():
    assert isLeapYear(2012) == True

def test_leap_year_divisible_by_100_and_400():
    assert isLeapYear(1700) == False

def test_not_leap_year_not_divisible_by_4():
    assert isLeapYear(1891) == False
    assert isLeapYear(1957) == False
