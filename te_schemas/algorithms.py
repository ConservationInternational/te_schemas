from dataclasses import (
    field,
    dataclass
)
import enum
import typing
import uuid
import re

import marshmallow_dataclass

from marshmallow import pre_load

from te_schemas import SchemaBase


class AlgorithmRunMode(enum.Enum):
    NOT_APPLICABLE = 0
    LOCAL = "local"
    REMOTE = "remote"
    BOTH = "both"


@marshmallow_dataclass.dataclass
class ExecutionScript(SchemaBase):
    class Meta:
        unknown = 'EXCLUDE'

    id: typing.Union[uuid.UUID, str]
    run_mode: typing.Optional[AlgorithmRunMode] = field(
        default=None,
        metadata={"by_value": True}
    )
    name: typing.Optional[str] = field(default="")
    slug: typing.Optional[str] = field(default="")
    execution_callable: typing.Optional[str] = field(default="")
    version: typing.Optional[str] = field(default="")
    description: typing.Optional[str] = field(default="")
    name_readable: typing.Optional[str] = field(default="")
    additional_configuration: typing.Optional[dict] = field(
            default_factory=dict)

    @pre_load
    def set_id(self, data, **kwargs):
        if not data.get('id', None):
            data['id'] = data['name']

        return data

    @pre_load
    def set_slug(self, data, **kwargs):
        if not data.get('slug', None):
            data['slug'] = data['name'].replace(" ", "-").lower()

        return data
