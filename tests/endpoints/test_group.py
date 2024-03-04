import pytest
from pytest_mock import MockerFixture
from datetime import datetime
from unittest.mock import MagicMock

import pytz

from pyfivetran.shed import ApiError
from pyfivetran.endpoints.group import Group, GroupEndpoint, BASE_API_URL, API_VERSION, GeneralApiResponse


class TestGroup:
    @pytest.fixture
    def group_endpoint_mock(self):
        return MagicMock(spec=GroupEndpoint)

    def test_as_url(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        expected_url = f'{BASE_API_URL}/{API_VERSION}/groups/123'
        assert group.as_url == expected_url

    def test_raw(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        group._raw = {'id': '123', 'name': 'Test Group', 'created_at': '2022-01-01'}
        assert group.raw == {'id': '123', 'name': 'Test Group', 'created_at': '2022-01-01'}

    def test_public_key(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        group.endpoint._request.return_value.json.return_value = {'data': {'public_key': '123'}}
        assert group.public_key == '123'
        group.endpoint._request.assert_called_once_with(
            method='GET',
            url=f'{group.as_url}/public-key'
        )

    def test_service_account(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        group.endpoint._request.return_value.json.return_value = {'data': {'service_account': '123'}}
        assert group.service_account == '123'
        group.endpoint._request.assert_called_once_with(
            method='GET',
            url=f'{group.as_url}/service-account'
        )

    def test__from_dict(self, group_endpoint_mock):
        group_dict = {
            'id': '123',
            'name': 'Test Group',
            'created_at': datetime(2022, 1, 1).strftime('%Y-%m-%dT%H:%M:%SZ')
        }
        group = Group._from_dict(group_endpoint_mock, group_dict)
        assert group.fivetran_id == '123'
        assert group.name == 'Test Group'
        assert group.created_at == datetime(2022, 1, 1, tzinfo=pytz.utc)
        assert group._raw == group_dict

    def test_delete(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        group.endpoint._request.return_value.json.return_value = {'status': 'success'}
        response = group.delete()
        assert response == {'status': 'success'}
        group.endpoint._request.assert_called_once_with(
            method='DELETE',
            url=group.as_url
        )

    def test_modify(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        group.endpoint._request.return_value.json.return_value = {'status': 'success'}
        response = group.modify(name='New Group Name')
        assert response == {'status': 'success'}
        group.endpoint._request.assert_called_once_with(
            method='PATCH',
            url=group.as_url,
            json={'name': 'New Group Name'}
        )

    def test_add_user(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        group.endpoint._request.return_value.json.return_value = {'status': 'success'}
        response = group.add_user(email='test@example.com', role='admin')
        assert response == {'status': 'success'}
        group.endpoint._request.assert_called_once_with(
            method='POST',
            url=f'{group.as_url}/users',
            json={'email': 'test@example.com', 'role': 'admin'}
        )

    def test_list_connectors(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        group.endpoint._paginate.return_value = [
            MagicMock(json=lambda: {'connector_id': '1'}),
            MagicMock(json=lambda: {'connector_id': '2'})
        ]
        connectors = group.list_connectors(schema='public', limit=10)
        assert connectors == [{'connector_id': '1'}, {'connector_id': '2'}]
        group.endpoint._paginate.assert_called_once_with(
            first_response=group.endpoint._request.return_value,
            endpoint=f'{group.as_url}/connectors',
            limit=10
        )

    def test_list_users(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        group.endpoint._paginate.return_value = [
            MagicMock(json=lambda: {'user_id': '1'}),
            MagicMock(json=lambda: {'user_id': '2'})
        ]
        users = group.list_users(limit=10)
        assert users == [{'user_id': '1'}, {'user_id': '2'}]
        group.endpoint._paginate.assert_called_once_with(
            first_response=group.endpoint._request.return_value,
            endpoint=f'{group.as_url}/users',
            limit=10
        )

    def test_remove_user(self, group_endpoint_mock):
        group = Group(
            endpoint=group_endpoint_mock,
            fivetran_id='123',
            name='Test Group',
            created_at=datetime.now()
        )
        group.endpoint._request.return_value.json.return_value = {'status': 'success'}
        response = group.remove_user(user_id='456')
        assert response == {'status': 'success'}
        group.endpoint._request.assert_called_once_with(
            method='DELETE',
            url=f'{group.as_url}/users/456'
        )

# Generated by CodiumAI


class TestGroupEndpoint:

    # can create a new group with valid name
    def test_create_group_with_valid_name(self, mocker: MockerFixture):
        client = mocker.Mock()
        group_endpoint = GroupEndpoint(client)
        group_name = "New Group"
        mock_response = mocker.Mock()
        mock_response.json.return_value = {'data': {'id': '123', 'name': group_name, 'created_at': '2022-01-01T00:00:00Z'}}
        mocker.patch.object(group_endpoint, '_request', return_value=mock_response)
        group = group_endpoint.create_group(group_name)
        assert group.name == group_name
        assert group.fivetran_id == '123'
        assert group.created_at == datetime(2022, 1, 1, 0, 0, 0, tzinfo=pytz.utc)

    # can list groups with valid limit (fixed)
    def test_list_groups_with_valid_limit_fixed(self, mocker):
        client = mocker.Mock()
        group_endpoint = GroupEndpoint(client)
        limit = 10
        groups = [{'id': str(i), 'name': f"Group {i}", 'created_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')} for i in range(limit)]
        mocker.patch.object(group_endpoint, '_request', return_value=mocker.Mock(json=lambda: {'data': {'items': groups}}))
        result = group_endpoint.list_groups(limit=limit)
        assert len(result) == limit
        assert all(isinstance(group, Group) for group in result)

    # can get a group with valid group_id
    def test_get_group_with_valid_group_id(self, mocker):
        client = mocker.Mock()
        group_endpoint = GroupEndpoint(client)
        group_id = "12345"
        group_name = "Test Group"
        group_data = {
            'id': group_id,
            'name': group_name,
            'created_at': '2023-12-21T10:11:08Z'
        }
        response_mock = mocker.MagicMock()
        response_mock.json.return_value = GeneralApiResponse(code=200, message=None, data=group_data)
        mocker.patch.object(group_endpoint, '_request', return_value=response_mock)
        result = group_endpoint.get_group(group_id)
        assert result.fivetran_id == group_id
        assert result.name == group_name

    # returns empty list when no groups exist
    def test_returns_empty_list_when_no_groups_exist(self, mocker):
        client = mocker.Mock()
        group_endpoint = GroupEndpoint(client)
        mocker.patch.object(group_endpoint, '_paginate', return_value=[])
        result = group_endpoint.list_groups()
        assert len(result) == 0


    # raises ApiError when creating a group with invalid name
    def test_raises_ApiError_when_creating_group_with_invalid_name(self, mocker):
        client = mocker.Mock()
        group_endpoint = GroupEndpoint(client)
        invalid_name = ""
        mocker.patch.object(group_endpoint, '_request', side_effect=ApiError("Invalid name"))
        with pytest.raises(ApiError):
            group_endpoint.create_group(invalid_name)