from format_name import get_formatted_name

def test_get_formatted_name():
    """Test get_formatted_name()"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"