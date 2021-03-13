from models.guardian import Guardian


def test_construction():
    g = Guardian('GFName1', 'GLName1')
    assert "GFName1" == g.first_name
    assert "GLName1" == g.last_name
