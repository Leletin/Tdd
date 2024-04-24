from Media import Media

def test_media():
    result = Media.media(5, 7)
    assert result == 6

def test_media2():
    result = Media.media(3, 5)
    assert result == 4
