# PyFivetran

A simple Python wrapper around the Fivetran REST API.

----------------------------------------------------------------
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/kharigardner/pyfivetran/test.yml?label=tests)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/kharigardner/pyfivetran/build.yml?label=build)
![License](https://img.shields.io/pypi/l/pyfivetran)


## Installation

```bash
pip install pyfivetran
```

## Usage

```python
from pyfivetran import FivetranClient

ftran = FivetranClient(api_key, api_secret)

# create endpoint objects
connector_endpoint = ftran.connector_endpoint
certificate_endpoint = ftran.certificate_endpoint
```

For more examples, see the [examples](https://github.com/kharigardner/pyfivetran/examples) directory.

## Development

```bash
pip install poetry

git clone https://github.com/kharigardner/pyfivetran.git

cd pyfivetran

poetry install
poetry install --with dev

# run tests
pytest tests

# create feature branch
git checkout -b feature/my-feature
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT. Fivetran API is subject to licensing, usage, and other terms and conditions not covered by this project. For more information, see the [Fivetran API documentation](https://fivetran.com/docs/rest-api).