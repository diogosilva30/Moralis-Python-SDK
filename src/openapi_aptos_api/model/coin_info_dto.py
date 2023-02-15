# coding: utf-8

"""
    aptos-api

    The aptos-api provider  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_aptos_api import schemas  # noqa: F401


class CoinInfoDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "supply_aggregator_table_handle",
            "symbol",
            "transaction_version_created",
            "coin_type_hash",
            "coin_type",
            "decimals",
            "transaction_created_timestamp",
            "name",
            "creator_address",
            "supply_aggregator_table_key",
        }
        
        class properties:
            
            
            class coin_type(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 5000
                    min_length = 1
            
            
            class coin_type_hash(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 64
            
            
            class creator_address(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 66
                    min_length = 66
            decimals = schemas.NumberSchema
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
                    min_length = 1
            supply_aggregator_table_handle = schemas.StrSchema
            supply_aggregator_table_key = schemas.StrSchema
            
            
            class symbol(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 10
                    min_length = 1
            transaction_created_timestamp = schemas.StrSchema
            transaction_version_created = schemas.StrSchema
            __annotations__ = {
                "coin_type": coin_type,
                "coin_type_hash": coin_type_hash,
                "creator_address": creator_address,
                "decimals": decimals,
                "name": name,
                "supply_aggregator_table_handle": supply_aggregator_table_handle,
                "supply_aggregator_table_key": supply_aggregator_table_key,
                "symbol": symbol,
                "transaction_created_timestamp": transaction_created_timestamp,
                "transaction_version_created": transaction_version_created,
            }
    
    supply_aggregator_table_handle: MetaOapg.properties.supply_aggregator_table_handle
    symbol: MetaOapg.properties.symbol
    transaction_version_created: MetaOapg.properties.transaction_version_created
    coin_type_hash: MetaOapg.properties.coin_type_hash
    coin_type: MetaOapg.properties.coin_type
    decimals: MetaOapg.properties.decimals
    transaction_created_timestamp: MetaOapg.properties.transaction_created_timestamp
    name: MetaOapg.properties.name
    creator_address: MetaOapg.properties.creator_address
    supply_aggregator_table_key: MetaOapg.properties.supply_aggregator_table_key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coin_type"]) -> MetaOapg.properties.coin_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coin_type_hash"]) -> MetaOapg.properties.coin_type_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator_address"]) -> MetaOapg.properties.creator_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decimals"]) -> MetaOapg.properties.decimals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supply_aggregator_table_handle"]) -> MetaOapg.properties.supply_aggregator_table_handle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supply_aggregator_table_key"]) -> MetaOapg.properties.supply_aggregator_table_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_created_timestamp"]) -> MetaOapg.properties.transaction_created_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_version_created"]) -> MetaOapg.properties.transaction_version_created: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["coin_type", "coin_type_hash", "creator_address", "decimals", "name", "supply_aggregator_table_handle", "supply_aggregator_table_key", "symbol", "transaction_created_timestamp", "transaction_version_created", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coin_type"]) -> MetaOapg.properties.coin_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coin_type_hash"]) -> MetaOapg.properties.coin_type_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator_address"]) -> MetaOapg.properties.creator_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decimals"]) -> MetaOapg.properties.decimals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supply_aggregator_table_handle"]) -> MetaOapg.properties.supply_aggregator_table_handle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supply_aggregator_table_key"]) -> MetaOapg.properties.supply_aggregator_table_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_created_timestamp"]) -> MetaOapg.properties.transaction_created_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_version_created"]) -> MetaOapg.properties.transaction_version_created: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["coin_type", "coin_type_hash", "creator_address", "decimals", "name", "supply_aggregator_table_handle", "supply_aggregator_table_key", "symbol", "transaction_created_timestamp", "transaction_version_created", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        supply_aggregator_table_handle: typing.Union[MetaOapg.properties.supply_aggregator_table_handle, str, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        transaction_version_created: typing.Union[MetaOapg.properties.transaction_version_created, str, ],
        coin_type_hash: typing.Union[MetaOapg.properties.coin_type_hash, str, ],
        coin_type: typing.Union[MetaOapg.properties.coin_type, str, ],
        decimals: typing.Union[MetaOapg.properties.decimals, decimal.Decimal, int, float, ],
        transaction_created_timestamp: typing.Union[MetaOapg.properties.transaction_created_timestamp, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        creator_address: typing.Union[MetaOapg.properties.creator_address, str, ],
        supply_aggregator_table_key: typing.Union[MetaOapg.properties.supply_aggregator_table_key, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CoinInfoDto':
        return super().__new__(
            cls,
            *args,
            supply_aggregator_table_handle=supply_aggregator_table_handle,
            symbol=symbol,
            transaction_version_created=transaction_version_created,
            coin_type_hash=coin_type_hash,
            coin_type=coin_type,
            decimals=decimals,
            transaction_created_timestamp=transaction_created_timestamp,
            name=name,
            creator_address=creator_address,
            supply_aggregator_table_key=supply_aggregator_table_key,
            _configuration=_configuration,
            **kwargs,
        )