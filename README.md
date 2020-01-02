# KBase Elasticsearch Config

This repo holds configuration files that can be used in other KBase search codebases.

* ES type mappings for each index
* Mapping of KBase Workspace type names to index names in ES.

## Validation

Run `python validate.py` to validate the yaml syntax in the config file.

## KBase Search Stack

* [Index Runner](https://github.com/kbaseIncubator/index_runner_deluxe) - Kafka consumer to construct indexes and documents.
* [Search API](https://github.com/kbaseIncubator/search_api_deluxe) - HTTP API for performing search queries.
* [Search Config](https://github.com/kbaseIncubator/search_config) - Global search configuration.
