import pytest

from ..views.units import UnitListView


@pytest.mark.django_db
def test_unit_list(test_unit, test_unit2, general_admin, rf):
    test_unit2.data_source = 'external_source'
    test_unit2.save()
    request = rf.get('/')
    request.user = general_admin
    response = UnitListView.as_view()(request)
    assert response.status_code == 200
    assert len(response.context_data['units']) == 2
    response.render()
    assert 'Can be edited' in str(response.content)
    assert 'Can not be edited' in str(response.content)



