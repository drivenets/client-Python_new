from logging import Logger
from typing import Dict, List, Text, Union

logger: Logger

def generate_uuid() -> Text: ...

def convert_string(value: Text) -> Text: ...

def dict_to_payload(value: Dict) -> List[Dict]: ...

def gen_attributes(rp_attributes: List[Dict]) -> List[Dict]: ...

def get_launch_sys_attrs() -> Dict[Text]: ...

def get_package_version(package_name: Text) -> Text: ...

def verify_value_length(
        attributes: Union[List[Dict], None]) -> Union[List[Dict], None]: ...

def timestamp() -> str: ...
