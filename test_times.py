from times import compute_overlap_time, time_range

def test_compute_overlap_within():
    long_time_range = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short_time_range = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(long_time_range, short_time_range)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_workshop_morning_times():
    # replace ... with your code for the additional test here
    # the structure should be very similar to the test above!
    new_range = time_range("2021-04-30 10:00:00", "2021-04-30 13:00:00")
    other_range = time_range("2021-04-30 10:05:00", "2021-04-30 12:55:00", 2, 600)
    result = compute_overlap_time(new_range, other_range)
    #print result
    expected = [('2021-04-30 10:05:00', '2021-04-30 11:25:00'),('2021-04-30 11:35:00','2021-04-30 12:55:00')]
    assert result == expected

def test_no_overlap():
    range1 = time_range("2021-04-30 10:00:00", "2021-04-30 12:00:00")
    range2 = time_range("2021-04-30 14:00:00", "2021-04-30 16:00:00")
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected

def test_partial_olap():
    range1 = time_range("2021-04-30 10:00:00", "2021-04-30 14:00:00")
    range2 = time_range("2021-04-30 12:00:00", "2021-04-30 16:00:00")
    result = compute_overlap_time(range1, range2)
    expected = [('2021-04-30 12:00:00','2021-04-30 14:00:00')]
    assert result == expected

def test_adjacent():
    range1 = time_range("2021-04-30 10:00:00", "2021-04-30 13:00:00")
    range2 = time_range("2021-04-30 13:00:00", "2021-04-30 16:00:00")
    result = compute_overlap_time(range1, range2)
    expected = [('2021-04-30 13:00:00','2021-04-30 13:00:00')]
    assert result == expected

def test_total_olap():
    range1 = time_range("2021-04-30 12:00:00", "2021-04-30 14:00:00")
    range2 = time_range("2021-04-30 12:00:00", "2021-04-30 14:00:00")
    result = compute_overlap_time(range1, range2)
    expected = [('2021-04-30 12:00:00','2021-04-30 14:00:00')]
    assert result == expected

def test_subintervals():
    range1 = time_range("2021-04-30 10:00:00", "2021-04-30 13:50:00", 4, 600)
    range2 = time_range("2021-04-30 12:00:00", "2021-04-30 15:50:00", 4, 600)
    result = compute_overlap_time(range1, range2)
    #print(range1)
    #print(range2)
    print(result)
    expected = [('2021-04-30 12:00:00','2021-04-30 12:50:00'),('2021-04-30 13:00:00','2021-04-30 13:50:00')]
    assert result == expected
