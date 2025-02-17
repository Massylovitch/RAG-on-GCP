import datetime as dt
from google.cloud.aiplatform.matching_engine import matching_engine_index_endpoint

def convert_filters_datetime_to_timestamp(filters):
    for key, value in filters.items():
        if isinstance(value, dt.date):
            filters[key] = int(dt.datetime.combine(value, dt.datetime.min.time()).timestamp())
    return filters

def get_namespace_from_filters(filters):
    filter = [
        matching_engine_index_endpoint.Namespace(
            "space_key",
            [space_name for space_name, value in filters.items() if value is True],
            [space_name for space_name, value in filters.items() if value is False],
        ),
    ]
    print(f"Filter values: {filter}")

    numeric_filter = [
        matching_engine_index_endpoint.NumericNamespace(
            "modified_at",
            value_int=filters["docs_start_date"],
            op="GREATER_EQUAL"
        ),
    ]
    print(f"Numeric filter values: {numeric_filter}")
    return filter, numeric_filter